import streamlit as st
import pandas as pd
from gpt4all import GPT4All

# --------- Model and Data Setup ---------

# Path to your local GGUF model file
model_path = "C:/Users/dasra/OneDrive/Desktop/ai_dashboard_project/models/mistral-7b-openorca.Q4_K_M.gguf"

# Load GPT4All model without trying to fetch config online
model = GPT4All(model_path, model_type="llama", allow_download=False)

# Load dummy business data from CSV
data = pd.read_csv("dummy_business_data.csv")

# --------- Streamlit App UI Setup ---------
st.set_page_config(page_title="AI Business Insights Dashboard", layout="wide")

st.title("📊 AI-Powered Business Insights Dashboard")
st.markdown("Leverage your local AI model to generate business insights from your data. No cloud APIs, everything runs locally.")

# --------- Sidebar Filters ---------
st.sidebar.header("🔍 Filter Data")
categories = data['Category'].unique()
selected_category = st.sidebar.multiselect("Select Categories:", categories, default=list(categories))

# Filter data based on user selection
filtered_data = data[data['Category'].isin(selected_category)]

# --------- Summary Business Metrics ---------
st.subheader("📈 Business Summary Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", f"{len(filtered_data)}")
col2.metric("Total Revenue", f"₹{filtered_data['Revenue'].sum():,.0f}")
col3.metric("Avg Order Value", f"₹{filtered_data['Revenue'].mean():,.0f}")

# --------- Data Table ---------
with st.expander("📋 View Business Data Table"):
    st.dataframe(filtered_data)

# --------- AI Insights Section ---------
st.subheader("🤖 AI-Generated Business Insight")

# Dropdown for metric selection
metric_option = st.selectbox("Select a metric for AI analysis:", ['Revenue', 'Quantity', 'Discount'])

# AI insight generation button
if st.button("🧠 Generate AI Insight"):
    # Prepare a better prompt for GPT4All
    prompt = f"""
    You are a sharp business analyst AI. Given the sales data sample below, analyze trends and provide a crisp, actionable one-paragraph insight about the '{metric_option}' metric.
    Focus on patterns, best-performing categories, and suggest one recommendation to improve.

    Data sample (OrderID, Category, Revenue, Quantity, Discount):
    {filtered_data[['OrderID','Category','Revenue','Quantity','Discount']].head(20).to_string(index=False)}
    """

    with st.spinner("AI is analyzing the data locally..."):
        ai_response = model.generate(prompt, max_tokens=400, temp=0.2)

    st.success("✅ Insight generated!")
    st.write(ai_response)

# --------- Footer ---------
st.markdown("---")
st.caption("🦙 Built locally with GPT4All + 📊 Streamlit | No cloud APIs, 100% offline dashboard.")
