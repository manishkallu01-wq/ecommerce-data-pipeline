
import pandas as pd
from kafka import KafkaProducer
import json
import time

# Load clean dataset
df = pd.read_csv("Online Retail1.csv", encoding="utf-8-sig")

# Data Cleaning
df = df.dropna(subset=["Description", "CustomerID"])
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Streaming e-commerce data...\n")

for _, row in df.iterrows():
    data = row.to_dict()

    producer.send("orders", value=data)

    print("Sent:", data["InvoiceNo"])

    time.sleep(0.02)
