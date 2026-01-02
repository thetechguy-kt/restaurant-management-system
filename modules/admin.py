import streamlit as st
from utils.storage import load_json, save_json

def admin_panel():
    st.header("Admin Panel")

    tables = load_json("tables.json", {})

    new_count = st.number_input("Number of Tables", min_value=1, value=len(tables))

    if st.button("Update Tables"):
        tables = {str(i): "available" for i in range(1, new_count + 1)}
        save_json("tables.json", tables)
        st.success("Tables updated")
