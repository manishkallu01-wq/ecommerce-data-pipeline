from kafka import KafkaConsumer
import json
from datetime import datetime
import os

# 🔥 NEW imports (must be at top)
import pyarrow as pa
import pyarrow.parquet as pq

# Kafka Consumer
consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='127.0.0.1:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# State variables
total_revenue = 0.0
product_sales = {}
country_revenue = {}
customer_spending = {}

counter = 0

print("Processing e-commerce stream...\n")

for message in consumer:
    data = message.value

    try:
        quantity = float(data.get("Quantity", 0))
        price = float(data.get("UnitPrice", 0))
        country = data.get("Country", "Unknown")
        product = data.get("Description", "Unknown")
        customer = str(data.get("CustomerID", "Unknown"))

        revenue = quantity * price
        total_revenue += revenue

        product_sales[product] = product_sales.get(product, 0) + revenue
        country_revenue[country] = country_revenue.get(country, 0) + revenue
        customer_spending[customer] = customer_spending.get(customer, 0) + revenue

        counter += 1

        if counter % 100 == 0:

            top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]
            top_country = max(country_revenue, key=country_revenue.get)
            top_customer = max(customer_spending, key=customer_spending.get)
            top_product = top_products[0][0]

            print("\n========== LIVE BUSINESS METRICS ==========")
            print(f"Total Revenue: {round(total_revenue,2)}")
            print(f"Top Product: {top_product}")
            print(f"Top Country: {top_country}")
            print(f"Top Customer ID: {top_customer}")

            # 🔥 PARQUET STORAGE

            timestamp = datetime.now()

            row = {
                "timestamp": str(timestamp),
                "total_revenue": round(total_revenue, 2),
                "top_product": top_product,
                "top_country": top_country,
                "top_customer": top_customer
            }

            table = pa.Table.from_pylist([row])

            if not os.path.exists("data_lake"):
                os.makedirs("data_lake")

            file_path = f"data_lake/data_{int(timestamp.timestamp())}.parquet"
            pq.write_table(table, file_path)

    except Exception as e:
        print("Error:", e)
