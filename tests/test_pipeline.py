from pathlib import Path
import pandas as pd
import pyarrow.parquet as pq
import pytest
from producer import load_orders, to_event
from consumer import parse_order, snapshot, update_metrics, write_snapshot

def state():
    return {"total_revenue":0.0,"processed_events":0,"product_sales":{},"country_revenue":{},"customer_spending":{}}

def test_sample_contract():
    frame=load_orders(Path("data/sample_orders.csv"))
    assert len(frame)==12
    assert set(frame.columns)>={"InvoiceNo","Description","Quantity","UnitPrice","CustomerID","Country"}

def test_missing_source_column(tmp_path):
    path=tmp_path/"bad.csv"; pd.DataFrame({"InvoiceNo":["1"]}).to_csv(path,index=False)
    with pytest.raises(ValueError,match="Missing columns"): load_orders(path)

def test_event_normalization():
    row=pd.Series({"InvoiceNo":100,"Description":"Item","Quantity":2,"UnitPrice":3.5,"CustomerID":12,"Country":"US"})
    event=to_event(row)
    assert event["InvoiceNo"]=="100" and event["CustomerID"]=="12"

def test_rejects_invalid_order():
    with pytest.raises(ValueError,match="positive"):
        parse_order({"InvoiceNo":"1","Description":"Item","Quantity":0,"UnitPrice":2,"CustomerID":"C","Country":"US"})

def test_metrics_and_parquet(tmp_path):
    metrics=state()
    order=parse_order({"InvoiceNo":"1","Description":"Item","Quantity":2,"UnitPrice":3,"CustomerID":"C","Country":"US"})
    update_metrics(metrics,order); row=snapshot(metrics); target=write_snapshot(row,tmp_path)
    loaded=pq.read_table(target).to_pylist()[0]
    assert loaded["processed_events"]==1
    assert loaded["total_revenue"]==6
    assert loaded["top_product"]=="Item"
