"""Print the latest generated metric snapshots."""
from pathlib import Path
import duckdb
files=list(Path("data_lake").glob("*.parquet"))
if not files: raise SystemExit("No Parquet snapshots found. Run the consumer and producer first.")
frame=duckdb.query("SELECT * FROM read_parquet('data_lake/*.parquet') ORDER BY processed_events DESC").df()
print(frame.head(20).to_string(index=False))
