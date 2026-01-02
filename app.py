import streamlit as st
from utils.styles import apply_touch_mode

from modules.tables import show_tables
from modules.orders import take_order
from modules.kitchen import kitchen_view
from modules.billing import billing
from modules.admin import admin_panel

st.set_page_config(layout="wide", page_title="Restaurant System")

st.sidebar.title("Restaurant System")
touch = st.sidebar.toggle("Touch Mode")
apply_touch_mode(touch)

page = st.sidebar.radio(
    "Navigate",
    ["Tables", "Order", "Kitchen", "Billing", "Admin"]
)

if page == "Tables":
    show_tables()
elif page == "Order":
    take_order()
elif page == "Kitchen":
    kitchen_view()
elif page == "Billing":
    billing()
elif page == "Admin":
    admin_panel()
