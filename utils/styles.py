import streamlit as st

def apply_touch_mode(enabled):
    if enabled:
        st.markdown("""
        <style>
        button {
            min-height: 60px !important;
            font-size: 20px !important;
        }
        input {
            font-size: 18px !important;
        }
        </style>
        """, unsafe_allow_html=True)
