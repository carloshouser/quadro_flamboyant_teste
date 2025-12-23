import streamlit as st

BASE_CSS = """
    <style>
    /* ===== BOTÕES ===== */
    .stButton > button {
        border-radius: 12px;
        font-weight: 600;
    }

    .stButton > button[kind="secondary"] {
        background: linear-gradient(135deg, #4b9be0, #1c6ec8);
        color: white;
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #ff9800, #f57c00);
        color: white;
        box-shadow: 0 0 14px rgba(255,152,0,.8);
    }

    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab"] {
        padding: 12px 20px;
        font-weight: 600;
    }

    /* ===== LINKS ===== */
    a {
        text-decoration: none;
        font-weight: bold;
    }
    </style>
"""


def apply_css():
    st.markdown(BASE_CSS, unsafe_allow_html=True)
