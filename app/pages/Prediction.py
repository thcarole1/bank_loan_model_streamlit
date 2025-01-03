# Import libraries
import streamlit as st
import pandas as pd
import requests

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <h1>Bank Loan prediction </h1>
    <h2> Features </h2>

    We have the following features : <br>
    - **Experience**: #years of professional experience<br>
    - **Income**: Annual income of the customer (**in thousands of dollars**) <br>
    - **ZIP_Code**: Home Address ZIP code.<br>
    - **Family**: Family size of the customer <br>
    - **CCAvg**: Avg. spending on credit cards per month (**in thousands of dollars**)<br>
    - **Education**: Education Level. 1: Undergrad; 2: Graduate; 3: Advanced/Professional<br>
    - **Mortgage**: Value of house mortgage if any (**in thousands of dollars**).<br>
    - **Personal Loan**: Did this customer accept the personal loan offered in the last campaign?<br>
    - **Securities Account**: Does the customer have a securities account with the bank?<br>
    - **CD Account**: Does the customer have a certificate of deposit (CD) account with the bank?<br>
    - **Online**: Does the customer use internet banking facilities?<br>
    - **CreditCard**: Does the customer use a credit card issued by UniversalBank?<br>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h2> Data inputs </h2>
    """,
    unsafe_allow_html=True
)

# Education, Experience and Income input
col1, col2, col3 = st.columns(3)
with col1:
    options = ["Undergrad", "Graduate", "Advanced/Professional"]
    Education = st.radio("**Education Level** :", options)

    options_dict = {1 : "Undergrad", 2 : "Graduate", 3 : "Advanced/Professional"}
    for key, value in options_dict.items():
        if Education == value:
            Education_encoded = key
with col2:
    Experience = st.number_input(label = "**#years of professional experience**", min_value=0)
with col3:
    Income = st.number_input(label = "**Income (in thousands of USD)**", min_value=0)

# ZIP_Code and Family input
col1, col2 = st.columns(2)
with col1:
    ZIP_Code = st.number_input(label = "**Home Address ZIP code**", min_value=0)
with col2:
    Family = st.number_input(label = "**Family size of the customer**", min_value=1)

# Avg spending input
CCAvg = st.number_input(label = "**Avg. spending on credit cards per month (**in thousands of USD**)**", min_value=0)

# Mortgage input
Mortgage = st.number_input(label = "**Value of house mortgage if any (**in thousands of dollars**)**", min_value=0)

# Securities Account input
options = [0, 1]
Securities_Account = st.radio("**Does the customer have a securities account with the bank?**", options)

# CD Account input
options = [0, 1]
CD_Account  = st.radio("**Does the customer have a certificate of deposit (CD) account with the bank?**", options)

# Online input
options = [0, 1]
Online = st.radio("**Does the customer use internet banking facilities?**", options)

# CreditCard input
options = [0, 1]
CreditCard  = st.radio("**Does the customer use a credit card issued by UniversalBank?**", options)

st.markdown(
    """
    <h3> Summary </h3>
    """,
    unsafe_allow_html=True
)

params = {
            "Education" : Education_encoded,
            "Experience" : Experience,
            "Income" : Income,
            "ZIP_Code" : ZIP_Code,
            "Family" : Family,
            "CCAvg" : CCAvg,
            "Mortgage" : Mortgage,
            "Securities_Account" : Securities_Account,
            "CD_Account" : CD_Account,
            "Online" : Online,
            "CreditCard": CreditCard
         }

input_df = pd.DataFrame(params, index=[0])

st.dataframe(data = input_df, hide_index=True)

st.markdown(
    """
    <h3> Prediction : Is this customer likely to purchase a loan ?</h3>
    """,
    unsafe_allow_html=True
)

# API endpoint
URL = "https://bank-loan-model-image-l63mv2bm6q-od.a.run.app/predict"

# Button to trigger the POST request
if st.button("Predict"):
    try:
        # Make the POST request with parameters
        r = requests.post(url=URL, params=params)

        # Display the response
        if r.status_code == 200:
            # st.success(f"Response: {r.json()}")
            response = r.json()

            # Get the prediction
            if response['prediction']['0'] == 0:
                answer = "NO"
            else:
                answer = "YES"

            st.write(f"The answer is: {answer}")

            # Retrieve and display info from API
            dict = {}
            for key, value in response.items():
                dict[key] = value['0']
            response_df = pd.DataFrame(dict, index=[0])
            st.dataframe(data = response_df, hide_index=True)
        else:
            st.error(f"Error {r.status_code}: {r.text}")
            prediction_result = "ERROR"
    except Exception as e:
        st.error(f"Request failed: {e}")
