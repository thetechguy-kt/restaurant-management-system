import streamlit as st
from utils.storage import load_json, save_json

def billing():
    st.header("Billing")

    orders = load_json("orders.json", {})
    tables = load_json("tables.json", {})

    ready = [t for t, o in orders.items() if o["status"] == "ready"]
    if not ready:
        st.info("No bills to generate.")
        return

    table = st.selectbox("Select Table", ready)

    total = 0
    for it in orders[table]["items"]:
        total += it["qty"] * it["price"]
        st.write(f"{it['name']} x {it['qty']}")

    st.success(f"Total Bill: ₹{total}")

    if st.button("Close Bill"):
        del orders[table]
        tables[table] = "available"
        save_json("orders.json", orders)
        save_json("tables.json", tables)
        st.rerun()
