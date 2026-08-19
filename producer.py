"""Publish validated order events to Kafka."""
from __future__ import annotations
import json, os, time
from pathlib import Path
import pandas as pd
from kafka import KafkaProducer

REQUIRED_COLUMNS={"InvoiceNo","Description","Quantity","UnitPrice","CustomerID","Country"}

def load_orders(path: str | Path) -> pd.DataFrame:
    frame=pd.read_csv(path,encoding="utf-8-sig")
    missing=REQUIRED_COLUMNS-set(frame.columns)
    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")
    frame=frame.dropna(subset=["Description","CustomerID"]).copy()
    return frame[(frame["Quantity"]>0)&(frame["UnitPrice"]>0)]

def to_event(row: pd.Series) -> dict:
    event=row.to_dict()
    event["InvoiceNo"]=str(event["InvoiceNo"]); event["CustomerID"]=str(event["CustomerID"])
    event["Quantity"]=float(event["Quantity"]); event["UnitPrice"]=float(event["UnitPrice"])
    return event

def main() -> None:
    source=Path(os.getenv("ORDER_SOURCE","data/sample_orders.csv"))
    producer=KafkaProducer(bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092"),key_serializer=lambda v:v.encode(),value_serializer=lambda v:json.dumps(v).encode())
    for _,row in load_orders(source).iterrows():
        event=to_event(row); producer.send(os.getenv("ORDER_TOPIC","orders"),key=event["InvoiceNo"],value=event)
        time.sleep(float(os.getenv("EVENT_INTERVAL_SECONDS","0.02")))
    producer.flush(); print("Order events published")

if __name__=="__main__": main()
