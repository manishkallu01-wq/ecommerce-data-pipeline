# ⚡ Real-Time E-Commerce Data Pipeline

A local Kafka pipeline that publishes order events, validates and aggregates them, writes metric snapshots to Parquet, queries them with DuckDB, and serves them in Streamlit.

## Why it exists

Operations teams need current revenue and sales signals without coupling source applications directly to reporting. Kafka separates event production from processing. Parquet keeps the generated analytical output portable, while DuckDB and Streamlit provide a lightweight local query and presentation layer.

## Data flow

```text
sample order CSV → Kafka producer → orders topic → consumer
                                                ├─ validation
                                                ├─ revenue calculation
                                                └─ running aggregates
                                                          ↓
                                                Parquet snapshots
                                                   ├─ DuckDB
                                                   └─ Streamlit
```

## Technology

| Component | Use |
|---|---|
| Python and Pandas | Source loading and event creation |
| Apache Kafka | Event transport |
| PyArrow and Parquet | Analytical metric snapshots |
| DuckDB | SQL over Parquet |
| Streamlit | Local dashboard |
| Docker Compose | Single-node Kafka for development |
| pytest | Transformation and contract tests |

## Repository layout

```text
.
├── data/sample_orders.csv
├── tests/test_pipeline.py
├── producer.py
├── consumer.py
├── query.py
├── dashboard.py
├── docker-compose.yml
├── requirements.txt
└── scripts/validate_project.py
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
python consumer.py
```

In another terminal run `python producer.py`. The bundled sample has 12 valid orders. The default snapshot interval is 10, so one Parquet snapshot is written after the tenth event.

```bash
python query.py
streamlit run dashboard.py
```

Stop Kafka with `docker compose down`.

## Tests

```bash
python scripts/validate_project.py
pytest -q
```

Tests cover source columns, invalid values, event normalization, aggregation, snapshot contents, and Parquet persistence. CI installs pinned dependencies and runs both checks.

## Results

The dashboard shows cumulative revenue, processed-event count, top country, and top product. Values come from the bundled synthetic sample and verify pipeline behavior; they are not business performance claims.

## 📸 Pipeline output

### Streamlit dashboard

<img width="1396" height="666" alt="E-commerce pipeline dashboard overview" src="https://github.com/user-attachments/assets/b55ca0dc-a4ed-4d27-b81b-673c14e85499" />

<img width="1363" height="424" alt="E-commerce pipeline product and country analysis" src="https://github.com/user-attachments/assets/28334f61-d9d8-4c52-ae41-6fc474fbd2da" />

<img width="1407" height="408" alt="E-commerce pipeline dashboard detail" src="https://github.com/user-attachments/assets/acb67cd3-564c-4f86-80c4-0e905b84582a" />

### Kafka pipeline running

<img width="579" height="956" alt="Kafka producer and consumer processing order events" src="https://github.com/user-attachments/assets/c328e6f9-f8a9-4f5d-a907-53d0e3f37d94" />

## Delivery and recovery semantics

Events are keyed by invoice number. The consumer uses a named group and Kafka-managed offsets, but its in-memory aggregates are rebuilt after a restart. This implementation is for local development, not exactly-once financial reporting.

## Configuration

| Variable | Default |
|---|---|
| `ORDER_SOURCE` | `data/sample_orders.csv` |
| `KAFKA_BOOTSTRAP_SERVERS` | `localhost:9092` |
| `ORDER_TOPIC` | `orders` |
| `EVENT_INTERVAL_SECONDS` | `0.02` |
| `SNAPSHOT_INTERVAL` | `10` |
| `DATA_LAKE_PATH` | `data_lake` |

## Scope

This repository does not include a schema registry, distributed stream processor, cloud object storage, or production observability.
