import streamlit as st

st.set_page_config(page_title="Password Toolkit")

st.title("🔐 Password Cracking Toolkit")

menu = st.sidebar.selectbox(
    "Choose Module",
    [
        "Home",
        "Dictionary Generator",
        "Password Analyzer",
        "Sample Hashes",
        "Report"
    ]
)

if menu == "Home":
    st.write("Welcome to the Password Security Toolkit.")

elif menu == "Dictionary Generator":
    st.write("Dictionary Generator Module")

elif menu == "Password Analyzer":
    st.write("Password Strength Analyzer")

elif menu == "Sample Hashes":
    st.write("Sample Password Hash Demonstration")

elif menu == "Report":
    st.write("Password Audit Report")
