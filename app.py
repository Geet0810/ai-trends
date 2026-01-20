import streamlit as st
from utils.data_loader import load_data
from utils.visualizations import *
from utils.models import *
from utils.finance_metrics import *
from utils.what_if import *

st.set_page_config(layout="wide", page_title="CFO–CTO AI Workforce Dashboard")

data = load_data()

st.title("AI Workforce Intelligence Dashboard (CFO–CTO View)")

tab1, tab2, tab3, tab4 = st.tabs([
    "Executive Overview",
    "Risk & Value Analysis",
    "Predictive & Trust",
    "What-If Scenarios"
])

with tab1:
    pareto_skills(data)
    growth_trends(data)
    cumulative_performance(data)

with tab2:
    raroc_waterfall(data)
    dual_axis_model_trust(data)
    outlier_detection(data)

with tab3:
    historical_prediction(data)
    roc_hvc_curve(data)
    shap_feature_impact(data)

with tab4:
    stress_test_slider(data)
    what_if_heatmap(data)
