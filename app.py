import streamlit as st
from khin_yi_module.ssism_cttm_v4.1 import SSISMCttmTruthEngine

st.set_page_config(page_title="SS'ISM CTTM AI for Justice v4.1", layout="wide")

engine = SSISMCttmTruthEngine()
ai_justice = engine.train_ai_ethical_core()  # Auto-trains AI
engine.activate_human_dashboard()  # Shows dashboard for humans
