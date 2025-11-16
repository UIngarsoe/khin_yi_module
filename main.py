import sys
import os
sys.path.append(os.path.abspath("khin_yi_module"))
# === KHIN YI MODULE IMPORT (FIXED) ===
import sys
import os
if 'khin_yi_module' not in sys.path:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'khin_yi_module'))
import SSISMCttmTruthEngine
# === KHIN YI EXPOSÉ DASHBOARD ===
khin_engine = SSISMCttmTruthEngine()
khin_engine.dashboard()
# app/main.py
import streamlit as st
import numpy as np
import random
from datetime import datetime

# === YOUR EXISTING CODE ===
# (keep everything you already had)

# === FIX: CORRECT IMPORT FOR KHIN YI ===
import sys
import os
sys.path.append(os.path.abspath("khin_yi_module"))
from ssism_cttm_v4.1 import SSISMCttmTruthEngine

# === YOUR EXISTING PAGE CODE ===
st.set_page_config(page_title="SS'ISM Paññā Shield v3.0", layout="wide")
# ... (your existing dashboard code)

# === ADD KHIN YI DASHBOARD AT THE END ===
khin_engine = SSISMCttmTruthEngine()
khin_engine.dashboard()
# === KHIN YI DASHBOARD (ACTIVATE) ===
if __name__ == "__main__":
    khin_engine = SSISMCttmTruthEngine()
    khin_engine.dashboard()
  
