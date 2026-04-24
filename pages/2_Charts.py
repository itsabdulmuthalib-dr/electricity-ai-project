import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Advanced Charts")

# Sample data
data = pd.DataFrame({
    "Hour": range(1, 25),
    "Usage": np.random.uniform(2, 8, 24),
    "Voltage": np.random.uniform(220, 240, 24)
})

st.subheader("Hourly Usage Chart")
st.line_chart(data.set_index("Hour")["Usage"])

st.subheader("Voltage Chart")
st.bar_chart(data.set_index("Hour")["Voltage"])

st.subheader("Data Table")
st.dataframe(data)