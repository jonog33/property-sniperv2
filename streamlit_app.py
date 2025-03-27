
import streamlit as st
import pandas as pd

# Load mock data
df = pd.read_csv("mock_data.csv")

# Page title
st.title("📊 Property Sniper Dashboard")

# Sidebar filters
st.sidebar.header("Filter Properties")
state = st.sidebar.selectbox("State", df["State"].unique())
budget = st.sidebar.slider("Max Budget", 300000, 500000, 500000)

# Filter logic
filtered = df[(df["State"] == state) & (df["Price"] <= budget) & (df["Investment Score"] >= 16.0)]

# Display table
st.subheader(f"Top Picks in {state} under ${budget:,}")
st.dataframe(filtered)

# Export option
st.download_button("📥 Download as CSV", filtered.to_csv(index=False), "filtered_properties.csv", "text/csv")
