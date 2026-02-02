import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Job Recommendation System",
    layout="wide"
)

# Title
st.title("💼 Job Recommendation System")
st.markdown("A data-driven system built using Upwork job postings")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("all_upwork_jobs_2024-02-07-2024-03-24.csv")

df = load_data()

# Show basic info
st.subheader("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Jobs", df.shape[0])
col2.metric("Total Columns", df.shape[1])
col3.metric("Missing Values", df.isna().sum().sum())

# Show preview
st.subheader("🔍 Dataset Preview")
st.dataframe(df.head(20), use_container_width=True)


import streamlit as st
import pandas as pd

st.title("Dataset Loading Example")

# Load CSV
df = pd.read_csv("all_upwork_jobs_2024-02-07-2024-03-24.csv")

st.write("Dataset loaded successfully!")
st.dataframe(df.head())

