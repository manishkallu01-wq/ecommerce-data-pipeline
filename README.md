## 🚀 Real-Time E-commerce Data Pipeline

> Built to replicate real-time analytics pipelines used in production data systems.

- An end-to-end data engineering project that streams transaction data using Kafka, processes it in real time, stores it in a Parquet-based data lake for efficient analytics, and visualizes insights through an interactive dashboard.
- Designed to simulate real-world streaming pipelines used in modern data platforms.
  
---

## 🧱 Architecture

CSV (batch source) → Kafka (ingestion) → Consumer (processing) → Parquet Data Lake (storage) → DuckDB (analytics) → Streamlit (visualization)

---
## 🔄 Data Flow

1. Producer streams transaction records from CSV to Kafka  
2. Consumer processes messages in real time  
3. Aggregated results are written to Parquet files (data lake)  
4. DuckDB enables fast analytical queries  
5. Streamlit dashboard visualizes live metrics

---

## 📥 Dataset

Dataset used: Online Retail Dataset  
Download from: https://archive.ics.uci.edu/ml/datasets/online+retail

---
### 📦 Install Dependencies

```
pip install -r requirements.txt
```
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
## 📁 Project Structure

```
ecommerce-data-pipeline/
│
├── data/             # Raw dataset
├── data_lake/        # Parquet files
├── producer.py       # Kafka producer
├── consumer.py       # Stream processing logic
├── dashboard.py      # Streamlit dashboard
├── query.py          # SQL queries (DuckDB)
├── requirements.txt  # Project dependencies
├── README.md
```
---

## ▶️ How to Run

### 1. Start Kafka (Docker)

Ensure Docker is running and Kafka is configured.

```
docker-compose up -d
```

### 2. Run Consumer

```
python consumer.py
```

### 3. Run Producer

```
python producer.py
```

### 4. Launch Dashboard

```
streamlit run dashboard.py
```
---

## 📊 Dashboard Output

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

![Dashboard 1](https://github.com/user-attachments/assets/b55ca0dc-a4ed-4d27-b81b-673c14e85499)
![Dashboard 2](https://github.com/user-attachments/assets/28334f61-d9d8-4c52-ae41-6fc474fbd2da)
![Dashboard 3](https://github.com/user-attachments/assets/acb67cd3-564c-4f86-80c4-0e905b84582a)

### Pipeline Running

![Pipeline](https://github.com/user-attachments/assets/c328e6f9-f8a9-4f5d-a907-53d0e3f37d94)

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
