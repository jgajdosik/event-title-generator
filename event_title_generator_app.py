
import streamlit as st
from datetime import date

st.set_page_config(page_title="Event Title Generator", layout="centered")
st.title("📋 SASE Activation Event Title Generator")

# Input fields
event_type = st.selectbox("Event Type", [
    "Stage 1 Node Activation", 
    "Stage 2 Migration", 
    "Stage 1 + 2 Combined"
])

service_id = st.text_input("Service ID")
customer_name = st.text_input("Customer Name")
address = st.text_input("Physical Address")
activation_date = st.date_input("Activation Date", value=date.today())
attempt_input = st.text_input("Attempt (e.g., 1, 2, 3)")
device_type = st.selectbox("Device Type", ["Single", "HA"])

# Generate title
if st.button("Generate Event Title"):
    attempt = f"Attempt: {attempt_input}"
    title = f"{event_type} | {service_id} | {customer_name} | {address} | {activation_date.strftime('%m/%d/%Y')} | {attempt} | {device_type}"
    st.success("🎉 Event title generated!")
    st.code(title)
    st.caption("You can copy and paste this title into your workflow.")
