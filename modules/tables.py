import streamlit as st
from utils.storage import load_json, save_json

def show_tables():
    st.header("Tables")

    tables = load_json("tables.json", {str(i): "available" for i in range(1, 11)})

    cols = st.columns(5)
    i = 0

    for tid, status in tables.items():
        with cols[i]:
            if status == "available":
                if st.button(f"Table {tid}\n🟢 Available", key=tid):
                    tables[tid] = "occupied"
                    save_json("tables.json", tables)
                    st.rerun()
            else:
                st.button(f"Table {tid}\n🔴 Occupied", disabled=True)
        i = (i + 1) % 5
