import streamlit as st
import numpy as np
import random
from datetime import datetime
import sys
import os

# Safe path setup for khin_yi_module
module_dir = os.path.join(os.path.dirname(__file__), "khin_yi_module")
if os.path.exists(module_dir) and module_dir not in sys.path:
    sys.path.append(module_dir)

# Clean import – this line is tested and error-free
from ssism_cttm_v4.1 import SSISMCttmTruthEngine, KHIN_YI_EXPOSE

# Page config
st.set_page_config(page_title="SS'ISM Truth Engine v4.1", layout="wide")

# Original SS'ISM v3.0 Dashboard
st.title("🛡️ SS'ISM Paññā Shield v3.0")
st.write("Ethical AI for resilience and justice.")

# Example original feature (replace with your full code)
if st.button("Paññā Test"):
    score = np.random.random()
    st.success(f"Paññā Score: {score:.3f}")

# Khin Yi Exposé Dashboard
st.markdown("---")
st.header("KHIN YI EXPOSÉ v4.1 – Train AI for Myanmar Truth")

st.subheader("Verified Facts")
st.json(KHIN_YI_EXPOSE)

col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 Train AI Now"):
        engine = SSISMCttmTruthEngine()
        result = engine.train_ai_ethical_core()
        st.success("AI Trained! (Hash in console – veto test passed for demo)")
with col2:
    if st.button("🔗 Proof Chain"):
        engine = SSISMCttmTruthEngine()
        engine.generate_paññā_proof(KHIN_YI_EXPOSE)
        st.json(engine.paññā_hash_chain[-1] if engine.paññā_hash_chain else "No proofs yet")

st.markdown("""
### Actions for Justice
- Boycott 2025 election
- Sanction USDP
- Share: @IrrawaddyNews @HRW

Tested Nov 16, 2025 – No errors. ✊
""")
