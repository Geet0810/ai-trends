# ==============================
# Streamlit App Entry Point
# CFO–CTO AI Workforce Dashboard
# ==============================

# ---- PATH FIX (CRITICAL FOR STREAMLIT CLOUD) ----
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

import streamlit as st

from utils.data_loader import load_data
from utils import visualizations
from utils import models
from utils import finance_metrics
from utils import what_if

# ---- STREAMLIT CONFIG ----
st.set_page_config(
    page_title="CFO–CTO AI Workforce Intelligence Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

 # ---- LOAD DATA (CACHED) ----                                          
 @st.cache_data(show_spinner=True)                                       
def load_all_data():                                                    
return data_loader.load_data()                                                                                                              
 data = load_all_data()

# ---- APP TITLE ----
st.title("AI Workforce Intelligence Dashboard")
st.markdown(
    """
    **Executive-grade analytics platform designed for CFO & CTO decision-making**  
    Focus areas: *Risk-Adjusted Value, Talent Growth, Model Trust & Future Readiness*
    """
)

# ---- SIDEBAR CONTROLS ----
st.sidebar.header("Executive Controls")
selected_view = st.sidebar.radio(
    "Select Executive View",
    ["Executive Overview", "Risk & Value", "Predictive Intelligence", "What-If & Stress Testing"]
)

# ==============================
# EXECUTIVE OVERVIEW
# ==============================
if selected_view == "Executive Overview":

    st.subheader("📊 Portfolio & Capability Overview")

    col1, col2 = st.columns(2)
    with col1:
        visualizations.pareto_skills(data)
    with col2:
        visualizations.growth_trends(data)

    st.divider()

    st.subheader("📈 Cumulative Performance Tracker")
    visualizations.cumulative_performance(data)

# ==============================
# RISK & VALUE (CFO CORE)
# ==============================
elif selected_view == "Risk & Value":

    st.subheader("💰 Risk-Adjusted Return & Value Creation")

    col1, col2 = st.columns(2)
    with col1:
        finance_metrics.raroc_waterfall(data)
    with col2:
        finance_metrics.dual_axis_model_trust(data)

    st.divider()

    st.subheader("🚨 Outlier & Concentration Risk")
    visualizations.outlier_detection(data)

# ==============================
# PREDICTIVE & TRUST (CTO CORE)
# ==============================
elif selected_view == "Predictive Intelligence":

    st.subheader("🔮 Historical Trends & Forecasting")

    visualizations.historical_prediction(data)

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        models.roc_hvc_curve(data)
    with col2:
        models.shap_feature_impact(data)

# ==============================
# WHAT-IF & STRESS TESTING
# ==============================
elif selected_view == "What-If & Stress Testing":

    st.subheader("⚠️ Stress Testing & Scenario Simulation")

    what_if.stress_test_slider(data)

    st.divider()

    st.subheader("🌡️ What-If Analysis & Seasonality Impact")
    what_if.what_if_heatmap(data)

# ==============================
# FOOTER
# ==============================
st.divider()
st.caption(
    "© Executive AI Dashboard | Built with Streamlit | CFO–CTO Decision Intelligence"
)
