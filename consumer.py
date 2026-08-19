"""Consume orders and write deterministic metric snapshots to Parquet."""
from __future__ import annotations
import json, os
from datetime import datetime, timezone
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
from kafka import KafkaConsumer

def parse_order(data: dict) -> dict:
    required={"InvoiceNo","Description","Quantity","UnitPrice","CustomerID","Country"}
    missing=required-data.keys()
    if missing: raise ValueError(f"Missing fields: {sorted(missing)}")
    quantity=float(data["Quantity"]); price=float(data["UnitPrice"])
    if quantity<=0 or price<=0: raise ValueError("Quantity and UnitPrice must be positive")
    return {**data,"Quantity":quantity,"UnitPrice":price,"revenue":quantity*price}

def update_metrics(state: dict, order: dict) -> None:
    state["total_revenue"]+=order["revenue"]; state["processed_events"]+=1
    for bucket,key in [("product_sales","Description"),("country_revenue","Country"),("customer_spending","CustomerID")]:
        name=str(order[key]); state[bucket][name]=state[bucket].get(name,0)+order["revenue"]

def snapshot(state: dict) -> dict:
    top=lambda key:max(state[key],key=state[key].get) if state[key] else None
    return {"timestamp":datetime.now(timezone.utc).isoformat(),"processed_events":state["processed_events"],"total_revenue":round(state["total_revenue"],2),"top_product":top("product_sales"),"top_country":top("country_revenue"),"top_customer":top("customer_spending")}

def write_snapshot(row: dict, output: Path) -> Path:
    output.mkdir(parents=True,exist_ok=True); target=output/f"metrics_{row['processed_events']:09d}.parquet"
    pq.write_table(pa.Table.from_pylist([row]),target); return target

def main() -> None:
    consumer=KafkaConsumer(os.getenv("ORDER_TOPIC","orders"),bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092"),group_id="analytics-writer",enable_auto_commit=True,value_deserializer=lambda x:json.loads(x.decode()))
    state={"total_revenue":0.0,"processed_events":0,"product_sales":{},"country_revenue":{},"customer_spending":{}}
    interval=int(os.getenv("SNAPSHOT_INTERVAL","10")); output=Path(os.getenv("DATA_LAKE_PATH","data_lake"))
    for message in consumer:
        try:
            order=parse_order(message.value); update_metrics(state,order)
            if state["processed_events"]%interval==0: print(f"Wrote {write_snapshot(snapshot(state),output)}")
        except (TypeError,ValueError) as exc: print(f"Rejected event: {exc}")

if __name__=="__main__": main()
