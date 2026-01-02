import streamlit as st
from utils.storage import load_json, save_json
from utils.menu_loader import load_menu

def take_order():
    st.header("Take Order")

    tables = load_json("tables.json", {})
    orders = load_json("orders.json", {})
    menu = load_menu()

    if not menu:
        st.error("Menu Excel file not found or empty!")
        return

    occupied = [t for t, s in tables.items() if s == "occupied"]
    if not occupied:
        st.warning("No occupied tables.")
        return

    table = st.selectbox("Select Table", occupied)

    if table not in orders:
        orders[table] = {"items": [], "status": "pending"}

    st.subheader("Menu")
    for item in menu:
        c1, c2, c3 = st.columns([3, 1, 1])
        with c1:
            st.write(f"{item['name']} — ₹{item['price']}")
        with c2:
            qty = st.number_input("Qty", 1, key=f"q{item['id']}")
        with c3:
            if st.button("Add", key=f"a{item['id']}"):
                orders[table]["items"].append({
                    "name": item["name"],
                    "qty": qty,
                    "price": item["price"]
                })
                save_json("orders.json", orders)
                st.rerun()

    st.subheader("Current Order")
    total = 0
    for it in orders[table]["items"]:
        t = it["qty"] * it["price"]
        total += t
        st.write(f"{it['name']} x {it['qty']} = ₹{t}")

    st.success(f"Total: ₹{total}")
