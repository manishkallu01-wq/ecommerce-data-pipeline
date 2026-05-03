import duckdb

print("\n📊 Reading Parquet Data...\n")

# Read ALL parquet files
df = duckdb.query("""
    SELECT * 
    FROM 'data_lake/*.parquet'
""").df()

print(df.head)
