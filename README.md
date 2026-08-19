# Real-Time E-Commerce Data Engineering Pipeline

> End-to-end streaming data platform demonstrating **event ingestion → validation → processing → data-lake storage → analytical SQL → business-facing serving** with Apache Kafka, Python, Parquet, DuckDB, and Streamlit.

## Executive Summary

This project simulates a production-style transaction data platform. Records from the UCI Online Retail dataset are published as Kafka events, processed by a Python streaming consumer, written as columnar Parquet data-lake outputs, queried with DuckDB, and surfaced through an interactive Streamlit dashboard.

The portfolio focus is the **data platform**, not the dashboard alone: ingestion reliability, transformation boundaries, storage format, analytical access, and serving are treated as separate engineering concerns.

## What The implementation covers

- Event-driven ingestion with Apache Kafka
- Streaming-style transaction processing in Python
- Validation and normalization before analytical consumption
- Columnar Parquet data-lake storage
- SQL analytics over data-lake files with DuckDB
- Business KPI serving through Streamlit
- Containerized local Kafka infrastructure
- Clear separation between ingestion, processing, storage, analytics, and presentation

## Architecture

```text
UCI Online Retail Dataset
          │
          ▼
   Kafka Producer
          │
          ▼
    Kafka Topic
          │
          ▼
 Streaming Consumer
   ├── validation
   ├── cleaning
   ├── revenue calculation
   └── running aggregates
          │
          ▼
   Parquet Data Lake
          │
      ┌───┴────┐
      ▼        ▼
   DuckDB   Streamlit
     SQL     Dashboard
      │        │
      └──► Business KPIs
```

## Data Flow

1. Read transaction records from the Online Retail source dataset.
2. Validate and normalize records before publishing events.
3. Publish records to a Kafka topic.
4. Consume events and calculate transaction-level revenue.
5. Persist processed records as Parquet files.
6. Query the data lake with DuckDB.
7. Serve KPIs and trends through Streamlit.

## Technology Stack

| Layer | Technology | Responsibility |
|---|---|---|
| Language | Python | Pipeline implementation |
| Streaming | Apache Kafka | Event transport |
| Processing | Python / Pandas | Validation and transformation |
| Data Lake | Parquet / PyArrow | Columnar persistence |
| Analytics | DuckDB | SQL over analytical files |
| Serving | Streamlit | Interactive business dashboard |
| Infrastructure | Docker Compose | Local Kafka environment |
| Source | UCI Online Retail | Transaction source data |

## Business Metrics

The analytical layer supports questions such as:

- What is total revenue over time?
- Which products generate the most revenue?
- Which countries contribute the most sales?
- Which customers have the highest transaction value?
- How many events have been processed?
- How does transaction activity change over time?

## Data Engineering Controls

The processing layer is designed around common pipeline controls:

- Input validation before publishing/processing
- Type and value normalization
- Transaction-level revenue calculation
- Separation of raw input from generated data-lake output
- Columnar storage for analytical scans
- SQL-based downstream consumption

For a production implementation, these controls would be expanded into schema contracts, automated data-quality tests, dead-letter handling, durable offsets, and observability.

## Repository Structure

```text
ecommerce-data-pipeline/
├── data/             # Raw source data; local execution only
├── data_lake/        # Generated Parquet outputs
├── producer.py       # Kafka event producer
├── consumer.py       # Streaming processing and aggregation
├── dashboard.py      # Streamlit serving layer
├── query.py          # DuckDB analytical SQL
├── requirements.txt
└── README.md
```

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

Verify the containers:

```bash
docker ps
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

## Engineering Decisions

### Kafka as the ingestion boundary

Kafka decouples the source producer from downstream processing and provides the event-streaming abstraction required to evolve the pipeline toward multiple consumers.

### Parquet as the data-lake format

Parquet provides columnar storage that is well suited to analytical workloads and reduces the need to reload or recompute the original transaction stream for every query.

### DuckDB for local analytical SQL

DuckDB provides an efficient analytical SQL layer over local Parquet outputs without requiring a separate warehouse for the portfolio implementation.

### Streamlit as the serving layer

The dashboard demonstrates how processed data can be exposed to business users after the ingestion and analytical layers have completed their work.

This is a **local portfolio implementation**, not a production deployment. Large raw datasets and generated data-lake files should remain local rather than being committed to Git.

A production-grade evolution could add:

- Kafka consumer groups and durable offsets
- Schema Registry with Avro or Protobuf
- Dead-letter topics for invalid events
- Checkpointed/stateful processing
- Airflow orchestration
- Cloud object storage such as Amazon S3
- Automated data-quality tests
- Warehouse/star-schema modeling
- CI/CD and observability

## Data Engineer Interview Talking Points

This project gives a strong interview narrative around:

1. **Ingestion:** why Kafka is useful between producers and consumers.
2. **Data quality:** where validation should occur and how bad events should be isolated.
3. **Storage:** why Parquet is preferable for analytical scans.
4. **Analytics:** how DuckDB can query columnar data without a heavyweight warehouse.
5. **Scalability:** how the Python consumer could evolve toward Spark/Flink-based processing.
6. **Productionization:** how orchestration, schema management, monitoring, and cloud storage would be introduced.

## Future Enhancements

- Add Airflow orchestration and scheduled quality checks.
- Add S3-compatible cloud data-lake storage.
- Introduce schema validation and versioning.
- Add automated unit/integration tests and CI/CD.
- Introduce a warehouse/star schema for BI workloads.
- Add pipeline latency, throughput, freshness, and failure metrics.

**Manish Kallu** — Data Engineering portfolio focused on streaming pipelines, distributed processing, SQL analytics, and production-oriented data platforms.

- GitHub: [manishkallu01-wq](https://github.com/manishkallu01-wq)
- Email: manishkallu01@gmail.com

**Built an end-to-end real-time e-commerce data pipeline using Kafka and Python, implementing event ingestion, validation, streaming aggregation, Parquet data-lake storage, DuckDB analytical SQL, and Streamlit-based operational reporting.**

## Reproducibility contract

The local workflow is complete when Kafka accepts generated order events, the consumer validates and persists them, the query layer returns the stored records, and the dashboard can read the same sink.

| Boundary | Contract |
|---|---|
| Event key | Stable order identifier |
| Event payload | Valid JSON with required commerce fields |
| Delivery | At-least-once; consumers must tolerate duplicate events |
| Storage | Cassandra table keyed for the documented query pattern |
| Observability | Producer/consumer failures must be visible in logs |
| Validation | Static checks and unit tests pass before services start |

Use `python scripts/validate_project.py` for a dependency-free repository smoke test. It checks required files, Python syntax, and documentation/run-contract completeness. Infrastructure services still require Kafka and Cassandra; the README does not claim an embedded production deployment.

## Production methodology

1. Capture immutable order events at the source boundary.
2. Validate schema and attach event metadata before publishing.
3. Partition by a stable business key to preserve per-order ordering.
4. Consume idempotently and store with query-driven keys.
5. Separate operational ingestion from analytical presentation.
6. Monitor lag, throughput, dead letters, duplicate rate, and sink latency.
7. Protect schema evolution with compatibility checks and CI.
