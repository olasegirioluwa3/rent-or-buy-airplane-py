import streamlit as st
from dashboard import Dashboard
import pandas as pd
from pycaret.classification import *
from datetime import datetime

# Create a function to run the prediction Streamlit app
def run_prediction_app():
    
    sd = st.sidebar
    sd.image("assets/logo.png", width='100%', use_column_width=True)

    st.title("Prediction Page")
    data = get_user_input()
    clf = setup(data=data, target='timestamp')


    data["timestamp"] = data["timestamp"].astype(str)
    
    data["timestamp"] = pd.to_datetime(data["timestamp"], unit='s')
    st.write(data)
    
    cal_button = st.button("Predict")


    # if cal_button:
    #     bs = Dashboard(data)
    #     operation_cost_per_hour = bs.get_operation_cost_per_hour()
    #     ownership_cost_per_year = bs.get_ownership_cost_per_year()
    #     others = bs.get_others()

    #     st.write("Operation Cost Per Hour:")
    #     st.write(operation_cost_per_hour)
    #     st.write("Ownership Cost / Year:")
    #     st.write(ownership_cost_per_year)
    #     st.write("Others:")
    #     st.write(others)

# Helper function to get user input
def get_user_input():
    data = {}
    data = pd.read_csv("fullraw.csv")

    # ... (User input code for predictions, similar to the 'main' function)

    return data

if __name__ == "__main__":
    run_prediction_app()
