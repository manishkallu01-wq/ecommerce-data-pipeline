# 🚀 Real-Time E-commerce Data Pipeline

## 📌 Overview

This project demonstrates an end-to-end data engineering pipeline that processes real-time e-commerce transactions and generates business insights.

---

## 🧱 Architecture

CSV Dataset → Kafka → Consumer → Parquet Data Lake → SQL (DuckDB) → Streamlit Dashboard

---

## ⚙️ Tech Stack

* Kafka (streaming)
* Python
* DuckDB (SQL analytics)
* Parquet (data lake)
* Streamlit (dashboard)

---

## 📊 Features

* Real-time revenue calculation
* Top product tracking
* Country-wise performance analysis
* High-value customer identification
* Persistent storage using Parquet
* Interactive dashboard visualization

---

## ▶️ How to Run

### 1. Start Kafka

docker-compose up -d

### 2. Run Consumer

python consumer.py

### 3. Run Producer

python producer.py

### 4. Launch Dashboard

streamlit run dashboard.py

---

## 📸 Output

* Live business metrics
* Revenue trends
* Top products visualization
* Country performance

---

## 💡 Key Learnings

* Built real-time streaming pipeline
* Implemented data cleaning and aggregation
* Designed data lake storage using Parquet
* Enabled SQL analytics using DuckDB
* Created interactive dashboard

---

## 🎯 Use Case

This pipeline simulates how companies like Amazon or Flipkart process transaction data to generate real-time insights.

---

## 🚀 Future Improvements

* Add batch + streaming hybrid architecture
* Deploy on cloud (AWS / GCP)
* Integrate Airflow for orchestration
