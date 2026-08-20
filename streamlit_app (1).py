import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="European Banking Churn Analytics",
    page_icon="🏦",
    layout="wide"
)

df = pd.read_csv("data/european_banking_customer_churn_dataset.csv")

st.title("🏦 European Banking Customer Churn Analytics")
st.caption("Customer Segmentation & Churn Pattern Analytics")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Customers", f"{len(df):,}")

if "Churn" in df.columns:
    c2.metric("Churn Rate", f"{df['Churn'].mean()*100:.2f}%")
else:
    c2.metric("Churn Rate", "N/A")

if "Account_Balance_EUR" in df.columns:
    c3.metric("Avg Balance", f"€{df['Account_Balance_EUR'].mean():,.0f}")
else:
    c3.metric("Avg Balance", "N/A")

if "Satisfaction_Score" in df.columns:
    c4.metric("Avg Satisfaction", f"{df['Satisfaction_Score'].mean():.1f}/10")
else:
    c4.metric("Avg Satisfaction", "N/A")

if "Churn" in df.columns:
    st.subheader("Churn by Country")
    if "Country" in df.columns:
        st.bar_chart(df.groupby("Country")["Churn"].mean() * 100)

    st.subheader("Churn by Products")
    if "Products" in df.columns:
        st.bar_chart(df.groupby("Products")["Churn"].mean() * 100)

st.subheader("Customer Data")
st.dataframe(df, use_container_width=True)
