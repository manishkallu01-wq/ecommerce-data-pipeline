# Real-Time E-Commerce Data Engineering Pipeline

> End-to-end streaming data platform demonstrating event ingestion, validation, real-time processing, data-lake storage, analytical SQL, and business-facing data visualization.

## Overview

This project simulates a production-style e-commerce data platform. Transaction records move from a batch source through **Apache Kafka**, are processed by a Python streaming consumer, persisted as **Parquet** data-lake outputs, queried with **DuckDB**, and surfaced through an interactive **Streamlit** dashboard.

The project is intentionally designed around core Data Engineering responsibilities rather than only dashboard development: **ingestion → processing → storage → analytics → serving**.

## Architecture

```text
Online Retail CSV
       │
       ▼
Kafka Producer ───────► Kafka Topic
                           │
                           ▼
                  Streaming Consumer
                  ├─ validation
                  ├─ cleaning
                  └─ aggregation
                           │
                           ▼
                   Parquet Data Lake
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                 DuckDB       Streamlit
               SQL analytics   dashboard
```

## Data Flow

1. Read transaction records from the Online Retail source dataset.
2. Validate and normalize records before publishing them as Kafka events.
3. Stream events through the Kafka topic to the processing consumer.
4. Calculate transaction-level revenue and running business aggregates.
5. Persist processed results as columnar Parquet files.
6. Query the data lake with DuckDB for analytical workloads.
7. Serve operational KPIs and trends through Streamlit.

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Event Streaming | Apache Kafka |
| Processing | Python / Pandas |
| Data Lake | Parquet / PyArrow |
| Analytical SQL | DuckDB |
| Visualization | Streamlit |
| Infrastructure | Docker Compose |
| Source Data | UCI Online Retail Dataset |

## Engineering Capabilities Demonstrated

- Event-driven ingestion with Kafka
- Streaming-style transaction processing
- Data validation and cleaning
- Revenue and business KPI aggregation
- Columnar data-lake storage with Parquet
- SQL analytics directly over data-lake files
- Interactive analytical serving with Streamlit
- Containerized local infrastructure
- Separation of ingestion, processing, storage, and presentation concerns

## Business Metrics

The pipeline calculates:

- Total revenue
- Top-selling products
- Top-performing countries
- High-value customers
- Revenue trends
- Transaction/event processing counts

## Project Structure

```text
ecommerce-data-pipeline/
├── data/             # Raw source data (local)
├── data_lake/        # Generated Parquet outputs
├── producer.py       # Kafka event producer
├── consumer.py       # Streaming processing and aggregation
├── dashboard.py      # Streamlit serving layer
├── query.py          # DuckDB analytical SQL
├── requirements.txt  # Python dependencies
└── README.md
```

## Dataset

The project uses the **UCI Online Retail Dataset**.

Source: UCI Machine Learning Repository — Online Retail.

Place the downloaded source file in the location expected by `producer.py`. Raw and generated data directories are intended for local execution and should not be committed when they contain large datasets.

## Local Setup

### 1. Create the Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Start Kafka infrastructure

```bash
docker compose up -d
```

### 3. Start the consumer

```bash
python consumer.py
```

### 4. Start the producer

```bash
python producer.py
```

### 5. Launch the dashboard

```bash
streamlit run dashboard.py
```

## Screenshots

### Dashboard

![Dashboard 1](https://github.com/user-attachments/assets/b55ca0dc-a4ed-4d27-b81b-673c14e85499)
![Dashboard 2](https://github.com/user-attachments/assets/28334f61-d9d8-4c52-ae41-6fc474fbd2da)
![Dashboard 3](https://github.com/user-attachments/assets/acb67cd3-564c-4f86-80c4-0e905b84582a)

### Pipeline Running

![Pipeline](https://github.com/user-attachments/assets/c328e6f9-f8a9-4f5d-a907-53d0e3f37d94)

## Data Engineering Design Notes

This is a local portfolio implementation, not a production deployment. A production-grade version could add schema management with Avro/Protobuf, Kafka consumer groups and durable offsets, checkpointed state, orchestration with Airflow, automated data-quality tests, cloud object storage, observability, CI/CD, and warehouse modeling.

## Resume-Ready Description

**Built an end-to-end real-time e-commerce data pipeline using Kafka, Python, Parquet, DuckDB, and Streamlit, implementing event ingestion, validation, streaming aggregation, columnar data-lake storage, and SQL-based operational analytics.**

## Future Enhancements

- Add Airflow orchestration and scheduled data-quality checks
- Add cloud object storage such as Amazon S3
- Introduce schema validation and versioning
- Add automated tests and CI/CD
- Add warehouse/star-schema modeling for BI workloads
- Add monitoring and data observability
