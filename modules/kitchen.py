import streamlit as st
from utils.storage import load_json, save_json

def kitchen_view():
    st.header("Kitchen")

    orders = load_json("orders.json", {})

    if not orders:
        st.info("No orders.")
        return

    for table, data in orders.items():
        st.subheader(f"Table {table} — {data['status'].upper()}")
        for item in data["items"]:
            st.write(f"{item['name']} x {item['qty']}")

        if st.button("Mark Ready", key=table):
            data["status"] = "ready"
            save_json("orders.json", orders)
            st.rerun()
