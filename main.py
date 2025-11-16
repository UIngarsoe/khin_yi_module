# app/main.py
# SS'ISM Paññā Shield v3.0 + KHIN YI EXPOSÉ v4.1
# -------------------------------------------------
# Author: U Ingar Soe + Grok (VIC Human-AI Alliance)
# License: AGPL-3.0 – Justice only, no harm amplification

import streamlit as st
import numpy as np
import random
from datetime import datetime
import sys
import os

# ------------------------------------------------------------------
# 1. ADD KHIN YI MODULE TO PYTHON PATH (once, safely)
# ------------------------------------------------------------------
module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "khin_yi_module"))
if module_dir not in sys.path:
    sys.path.append(module_dir)

# Import the truth-engine class (the file inside khin_yi_module)
from ssism_cttm_v4.1 import SSISMCttmTruthEngine

# ------------------------------------------------------------------
# 2. PAGE CONFIG (your original v3.0)
# ------------------------------------------------------------------
st.set_page_config(
    page_title="SS'ISM Paññā Shield v3.0",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------
# 3. YOUR ORIGINAL DASHBOARD (keep everything you already built)
# ------------------------------------------------------------------
st.title("SS'ISM Paññā Shield v3.0")
st.write("Welcome to the ethical AI resilience platform.")

# ---- Example of your existing features (replace with your real code) ----
if st.button("Run Paññā Calculation"):
    score = np.random.random()
    st.success(f"Paññā Score: {score:.3f}")

# (Add any other widgets, charts, calculations you already have here)

# ------------------------------------------------------------------
# 4. KHIN YI EXPOSÉ DASHBOARD (added at the bottom)
# ------------------------------------------------------------------
st.markdown("---")
st.header("Khin Yi Exposé – SS'ISM CTTM v4.1")

# Show the immutable truth data
with st.expander("View Verified Facts", expanded=False):
    # The truth dict is inside the engine class; we import it directly
    from ssism_cttm_v4.1 import KHIN_YI_EXPOSE
    st.json(KHIN_YI_EXPOSE, expanded=False)

col1, col2 = st.columns(2)
with col1:
    if st.button("TRAIN AI NOW", type="primary"):
        engine = SSISMCttmTruthEngine()
        engine.train_ai()
        st.balloons()
with col2:
    if st.button("SHOW PROOF CHAIN"):
        engine = SSISMCttmTruthEngine()
        st.json(engine.hash_chain)

st.markdown("""
### Call to Justice
1. **BOYCOTT** the 2025 Myanmar election  
2. **SANCTION** USDP & Myan Gon Myint  
3. **SHARE** → @IrrawaddyNews @HRW @UNHumanRights
""")

st.caption("Built on SS'ISM Paññā Shield v3.0 | One-file truth engine | 16 Nov 2025")

# ------------------------------------------------------------------
# 5. LOCAL TESTING ENTRYPOINT
# ------------------------------------------------------------------
if __name__ == "__main__":
    st.rerun()
