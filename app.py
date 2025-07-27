import streamlit as st
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Symbolic Identity Vortex", layout="wide")
st.title("🌀 Symbolic Identity Vortex")

st.markdown("""
This tool simulates symbolic identity interactions across recursive attractor fields.
Identity structures may fuse, destabilize, or collapse based on stress and coherence gradients.
""")

# Sidebar parameters
st.sidebar.header("Simulation Parameters")
identity_count = st.sidebar.slider("Number of Identity Fields", 2, 6, 3)
interaction_strength = st.sidebar.slider("Interaction Strength", 0.1, 2.0, 1.0)
coherence_threshold = st.sidebar.slider("Collapse Threshold", 0.1, 1.0, 0.5)

# Identity field simulation
np.random.seed(42)
time_steps = 100
data = []

for i in range(identity_count):
    base_angle = np.random.rand() * 2 * np.pi
    for t in range(time_steps):
        angle = base_angle + interaction_strength * np.sin(t / 10)
        coherence = np.cos(angle) * (1 - t / time_steps)
        collapse = 1 if abs(coherence) < coherence_threshold else 0
        data.append({
            "Time": t,
            "Identity": f"ID-{i+1}",
            "Coherence": coherence,
            "Collapse": collapse
        })

import pandas as pd
df = pd.DataFrame(data)
fig = px.line(df, x="Time", y="Coherence", color="Identity", title="Symbolic Identity Coherence Over Time")
st.plotly_chart(fig, use_container_width=True)

collapse_rate = df.groupby("Identity")["Collapse"].mean()
st.subheader("⚠️ Collapse Rate by Identity")
st.bar_chart(collapse_rate)
