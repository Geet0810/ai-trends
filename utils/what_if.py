import plotly.express as px
import numpy as np
import streamlit as st

def stress_test_slider(data):
    shock = st.slider("Economic Shock %", -50, 50, 0)
    impact = np.random.rand(10) * (1 + shock/100)
    fig = px.line(impact, title="Stress Test Impact")
    st.plotly_chart(fig)

def what_if_heatmap(data):
    z = np.random.rand(5,5)
    fig = px.imshow(z, title="What-If Heatmap")
    st.plotly_chart(fig)
