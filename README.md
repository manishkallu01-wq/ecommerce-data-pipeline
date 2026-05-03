## 🚀 Real-Time E-commerce Data Pipeline

- An end-to-end data engineering project that streams transaction data using Kafka, processes it in real time, stores it in a Parquet-based data lake, and visualizes insights through an interactive dashboard.
- Designed to simulate real-world streaming pipelines used in modern data platforms.

---

## 🧱 Architecture

CSV Dataset → Kafka → Consumer → Parquet Data Lake → SQL (DuckDB) → Streamlit Dashboard

---
## 📥 Dataset

Dataset used: Online Retail Dataset  
Download from: https://archive.ics.uci.edu/ml/datasets/online+retail

----

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
## 📁 Project Structure

```
ecommerce-data-pipeline/
│
├── data/           # Raw dataset
├── data_lake/      # Parquet files
├── producer.py     # Kafka producer
├── consumer.py     # Stream processing logic
├── dashboard.py    # Streamlit dashboard
├── query.py        # SQL queries (DuckDB)
├── README.md
```
---

## ▶️ How to Run

### 1. Start Kafka

cd kafka-project

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
## 📊 Metrics Computed

- Total Revenue (real-time)
- Top Selling Products
- Top Performing Country
- High-Value Customers
---

## 📸 Screenshots

### Dashboard
<img width="1396" height="666" alt="Screenshot 2026-05-03 at 1 45 05 PM" src="https://github.com/user-attachments/assets/b55ca0dc-a4ed-4d27-b81b-673c14e85499" />
<img width="1363" height="424" alt="Screenshot 2026-05-03 at 1 45 15 PM" src="https://github.com/user-attachments/assets/28334f61-d9d8-4c52-ae41-6fc474fbd2da" />
<img width="1407" height="408" alt="Screenshot 2026-05-03 at 1 45 22 PM" src="https://github.com/user-attachments/assets/acb67cd3-564c-4f86-80c4-0e905b84582a" />

### Pipeline Running
<img width="579" height="956" alt="Screenshot 2026-05-03 at 1 46 28 PM" src="https://github.com/user-attachments/assets/c328e6f9-f8a9-4f5d-a907-53d0e3f37d94" />

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
