# Import libraries
import streamlit as st
import pandas as pd

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
"""
    <h1>Bank Loan prediction </h1>
    <h2> Specific issues and objectives </h2>

    <h3> Nature of the problem </h3>
    This is a binary classification where the objective is to predict whether a customer will get a loan or not.<br>

    <h3> Impact of errors </h3>
    - False negatives (<b>eligible customers rejected</b>) can lead to <b>revenue losses</b> for the bank.<br>
    - False positives (<b>ineligible customers accepted</b>) can lead to <b>payment default risks</b>.<br>

    <h3> Priority criterion  </h3>
    <b>Recall</b> can be favored if the objective is to <b>minimize false negatives</b>, or the <b>F1-score</b> to <b>balance precision and recall</b>.<br>

    <h2> Data analysis </h2>
    <h3> Class balance </h3>
    Classes are <b>highly unbalanced</b> (majority of loan non-approvals). <br><br>
    """,
    unsafe_allow_html=True
)

st.image("data/piechart_Personal_Loan.png", caption="Target (i.e Personal_Loan) imbalance")

st.markdown(
"""
Models must be robust to this or require rebalancing techniques (e.g., <b>SMOTE</b>, class weighting).
    """,
    unsafe_allow_html=True
)

st.markdown(
"""
    <h3> Features </h3>
    - Categorical features (e.g., Family size, Education level).<br><br>
    """,
    unsafe_allow_html=True
)

st.image("data/count_plots_Categorical.png", caption="Examples of categorical features")

st.markdown(
"""
    - Numerical features (e.g., income, average credit card spending).<br><br>
    """,
    unsafe_allow_html=True
)
st.image("data/hist_plots_Numerical.png", caption="Examples of numerical features")

st.markdown(
"""
    <h3> Correlation between features </h3>
    """,
    unsafe_allow_html=True
)
st.image("data/correlation_numerical.png", caption="Correlation between numerical features")
