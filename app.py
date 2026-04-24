import streamlit as st
import time
import pandas as pd
from utils.live_data import generate_live_data
from models.forecast import predict_next_usage
from models.anomaly import detect_anomaly

st.set_page_config(page_title="Electricity AI Project", layout="wide")

st.title("⚡ Electricity Consumption Forecasting and Anomaly Detection")
st.subheader("IoT Simulated Live Data Dashboard")
st.sidebar.markdown("---")
st.sidebar.header("📌 Project Info")
st.sidebar.write("AI-based smart electricity monitoring system.")
st.sidebar.write("Developed by:")
st.sidebar.write("• Abdul Muthalib")
st.sidebar.write("• Varshini")

# Sidebar Controls
st.sidebar.header("⚙️ Controls")
refresh_speed = st.sidebar.slider("Refresh Speed (seconds)", 1, 5, 2)
threshold = st.sidebar.slider("Anomaly Threshold", 5, 10, 8)

if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame()

placeholder = st.empty()

for i in range(20):
    df = generate_live_data()

    st.session_state.history = pd.concat(
        [st.session_state.history, df],
        ignore_index=True
    )

    current_usage = df["Usage_kWh"][0]
    prediction = predict_next_usage(st.session_state.history)
    anomaly = current_usage > threshold

    with placeholder.container():
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Usage (kWh)", current_usage)

        with col2:
            st.metric("Voltage (V)", df["Voltage"][0])

        with col3:
            st.metric("Current (A)", df["Current"][0])

        with col4:
            st.metric("Predicted Next Usage", prediction)

        if anomaly:
            st.error("🚨 Anomaly Detected: High Electricity Usage!")
        else:
            st.success("✅ Normal Consumption")

        st.write("Usage Trend")
        st.line_chart(st.session_state.history["Usage_kWh"])

        st.write("Recent Readings")
        st.dataframe(st.session_state.history.tail(10))

        csv = st.session_state.history.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download Full Report CSV",
            data=csv,
            file_name="electricity_report.csv",
            mime="text/csv",
            key=f"download_{i}"
        )

    time.sleep(refresh_speed)