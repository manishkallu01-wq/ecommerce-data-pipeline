import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(page_title="E-commerce Dashboard", layout="wide")

st.title("📊 Real-Time E-commerce Analytics")

# Load data
df = duckdb.query("""
    SELECT *
    FROM 'data_lake/*.parquet'
""").df()

if df.empty:
    st.warning("No data available yet. Run pipeline first.")
    st.stop()

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# --- METRICS ---
st.subheader("📈 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("💰 Latest Revenue", f"{df['total_revenue'].iloc[-1]:,.2f}")
col2.metric("🌍 Top Country", df["top_country"].iloc[-1])
col3.metric("👤 Top Customer", df["top_customer"].iloc[-1])

# --- REVENUE TREND ---
st.subheader("📉 Revenue Over Time")

st.line_chart(df.set_index("timestamp")["total_revenue"])

# --- TOP PRODUCTS ---
st.subheader("🏆 Top Products")

top_products = df["top_product"].value_counts().head(10)
st.bar_chart(top_products)

# --- COUNTRY DISTRIBUTION ---
st.subheader("🌍 Country Distribution")

country_counts = df["top_country"].value_counts()
st.bar_chart(country_counts)
