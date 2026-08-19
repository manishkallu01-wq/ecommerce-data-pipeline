"""Streamlit view over generated Parquet metric snapshots."""
from pathlib import Path
import duckdb
import pandas as pd
import streamlit as st

st.set_page_config(page_title="E-commerce Dashboard",layout="wide")
st.title("📊 Real-Time E-commerce Analytics")
files=list(Path("data_lake").glob("*.parquet"))
if not files:
    st.info("No metric snapshots yet. Start Kafka, the consumer, and then the producer."); st.stop()
df=duckdb.query("SELECT * FROM read_parquet('data_lake/*.parquet') ORDER BY processed_events").df()
df["timestamp"]=pd.to_datetime(df["timestamp"]); latest=df.iloc[-1]
c1,c2,c3,c4=st.columns(4)
c1.metric("💰 Revenue",f"USD {latest['total_revenue']:,.2f}"); c2.metric("📦 Events",f"{int(latest['processed_events']):,}")
c3.metric("🌍 Top country",latest["top_country"]); c4.metric("🏆 Top product",latest["top_product"])
st.subheader("Revenue by processed event count"); st.line_chart(df.set_index("processed_events")["total_revenue"])
st.dataframe(df.sort_values("processed_events",ascending=False),use_container_width=True)
