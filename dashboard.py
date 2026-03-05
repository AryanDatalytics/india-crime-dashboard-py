import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="India Crime Dashboard", layout="wide")

st.title("📊 India Crime Analysis Dashboard")

df = pd.read_csv("crime_dataset_india.csv")

# Age Group
bins = [0, 18, 30, 45, 60, 100]
labels = ['0-18', '19-30', '31-45', '46-60', '60+']
df['Age Group'] = pd.cut(df['Victim Age'], bins=bins, labels=labels)

# 🔥 Top Metrics Row
col1, col2, col3 = st.columns(3)

col1.metric("Total Crimes", len(df))
col2.metric("Total Cities", df['City'].nunique())
col3.metric("Crime Types", df['Crime Domain'].nunique())

st.markdown("---")

# 🔥 Filters
col1, col2 = st.columns(2)

selected_city = col1.selectbox("Select City", df['City'].unique())
selected_domain = col2.selectbox("Select Crime Domain", df['Crime Domain'].unique())

filtered = df[(df['City'] == selected_city) & 
              (df['Crime Domain'] == selected_domain)]

# 🔥 Interactive Plotly Graph
fig = px.histogram(filtered,
                   x="Age Group",
                   color="Age Group",
                   title="Crime Distribution by Age Group",
                   text_auto=True)

st.plotly_chart(fig, use_container_width=True)
