"""
Author: keanteng
License: GNU GPLv3
"""

import streamlit as st
from backend.functions import *
import plotly.express as px

# setup
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# side bar setup
st.sidebar.title("EPF Projection Calculator")
st.sidebar.caption("Your Goal Towards Retirement")

nationality = st.sidebar.selectbox("Nationality", ["Malaysian", "Non-Malaysian"])
salary = st.sidebar.number_input("Your Monthly Salary", value=3000, step=100)
bonus = st.sidebar.number_input("Your Yearly Bonus", value=5000, step=100)
compound_rate = st.sidebar.number_input("Your Expected Compound Rate (%)", value=6.5, step=0.5)
goal = st.sidebar.slider("Your Saving Goal", min_value=1000000, max_value=10000000, step = 1000000)

st.sidebar.divider()
st.sidebar.caption("GPLv3 © Kean Teng 2024")

# main page setup
data = get_data()
df = get_schedule(nationality, data)
if salary > 20000:
    contribution = twenty_above_contribution(nationality, salary)
else:
    contribution = match_contribution(df, contribution_lookup(df, salary))
if bonus > 20000:
    bonus_contribution = twenty_above_bonus_contribution(nationality, bonus)
else:
    bonus_contribution = match_bonus_contribution(df, bonus_contribution_lookup(df, bonus))

# goal seek
years = goal_seek(goal, contribution, bonus_contribution, compound_rate)
total_by_year = year_total(years, contribution, compound_rate)

st.header("👋 Hi there!")
st.write("Based on your current salary, you will need to work for ", round(years, 2), " years to achieve your saving goal.")
with st.expander("📊 View Your Contribution Summary"):
    st.dataframe(salary_contribution_summary(df, contribution_lookup(df, salary), salary), hide_index=True)
    st.dataframe(bonus_contribution_summary(df, bonus_contribution_lookup(df, bonus), bonus), hide_index=True)

# plotly
fig = px.line(total_by_year, x=total_by_year.index, y="total", title="Your Contribution Schedule")
st.plotly_chart(fig)