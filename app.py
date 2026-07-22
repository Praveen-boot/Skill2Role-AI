import streamlit as st
import joblib

st.title("Test App")
st.success(f"Joblib imported successfully! Version: {joblib.__version__}")