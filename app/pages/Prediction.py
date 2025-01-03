# Import libraries
import streamlit as st
import pandas as pd
import requests

# Load custom CSS
with open("app/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <h1>House price prediction </h1>
    <h2> Features </h2>

    We have the following features : <br>
    - **Longitude**: Geographical longitude of the block group's centroid.
    - **Latitude**: Geographical latitude of the block group's centroid.
    - **Housing median age**: Median age of houses in the block group.
    - **Total rooms**: Total rooms of the block group.
    - **Total bedrooms**: Total bedrooms of the block group.
    - **Population**:Total population of the block group.
    - **Households**: Total households of the block group.
    - **Median income**: Median income of households in the block group (**in tens of thousands of dollars**).
    - **Ocean proximity**: Proximity from ocean.
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h2> Data inputs </h2>
    """,
    unsafe_allow_html=True
)

# Coordinates input
col1, col2 = st.columns(2)
with col1:
    longitude = st.number_input(label = "**Longitude**")
with col2:
    latitude = st.number_input(label = "**Latitude**")

# House median age
housing_median_age = st.number_input(label = "**Housing median age**", min_value=0, step=1)

# Census info
col1, col2 = st.columns(2)
with col1:
    total_rooms = st.number_input(label = "**Total rooms**", min_value=0, step=1)
with col2:
    total_bedrooms = st.number_input(label="**Total bedrooms**",min_value=0, step=1)

# Population info
col1, col2 = st.columns(2)
with col1:
    population = st.number_input(label = "**Population**", min_value=0, step=1)
with col2:
    households = st.number_input(label="**Households**",min_value=0, step=1)

# Median income
median_income = st.number_input(label = "**Median income** (**in tens of thousands of dollars**)", min_value=0, step=1)

# Ocean proximity
options = ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"]
ocean_proximity = st.radio("**Ocean proximity** :", options)

st.markdown(
    """
    <h3> Summary </h3>
    """,
    unsafe_allow_html=True
)

params = {
            "longitude" : longitude,
            "latitude" : latitude,
            "housing_median_age" : housing_median_age,
            "total_rooms" : total_rooms,
            "total_bedrooms" : total_bedrooms,
            "population" : population,
            "households" : households,
            "median_income" : median_income,
            "ocean_proximity" : ocean_proximity
         }

input_df = pd.DataFrame(params, index=[0])

st.dataframe(data = input_df, hide_index=True)

st.markdown(
    """
    <h3> Prediction </h3>
    """,
    unsafe_allow_html=True
)

# API endpoint
URL = "https://house-pricing-project-image-q7vjkyyeda-od.a.run.app/predict"

# Button to trigger the POST request
if st.button("Predict"):
    try:
        # Make the POST request with parameters
        r = requests.post(url=URL, params=params)

        # Display the response
        if r.status_code == 200:
            st.success(f"Response: {r.json()}")
            response = r.json()

            # Get the predicted price
            st.write(f"Predicted price : {response['prediction']['0']} USD")

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
