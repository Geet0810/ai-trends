import plotly.express as px
import streamlit as st

def pareto_skills(data):
    df = data["skills"].value_counts().head(10)
    fig = px.bar(df, title="Pareto: Top AI Skills")
    st.plotly_chart(fig)

def growth_trends(data):
    df = data["country"]
    fig = px.line(df, x="year", y="ai_adoption", title="Growth Trends")
    st.plotly_chart(fig)
