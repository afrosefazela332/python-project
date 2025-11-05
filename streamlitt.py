
import streamlit as st

st.set_page_config(page_title="Patient Form", layout="centered")

st.markdown("## 🩺 Patient Form")

# Input fields
name = st.text_input("Enter Name")
gender = st.text_input("Gender")
age = st.text_input("Age")
contact = st.text_input("Contact")
branch = st.selectbox("Select", ["Diabetes", "Blood Pressure", "Thyroid"])

# Submit button
if st.button("Submit"):
    if name and gender and age and contact and branch:
        st.success("✅ Data Submitted")
    else:
        st.warning("⚠️ Please Fill all the Fields")



