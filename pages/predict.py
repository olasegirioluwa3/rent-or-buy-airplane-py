import streamlit as st
from dashboard import Dashboard
import pandas as pd
from pycaret.classification import *
from datetime import datetime

# Create a function to run the prediction Streamlit app
def run_prediction_app():
    # Define the CSS for the background image
    sd = st.sidebar
    sd.image("assets/logo.png", width='100%', use_column_width=True)

    st.title("Prediction Page")
    data = get_user_input()
    
    data["timestamp"] = data["timestamp"].astype(str)
    
    data["timestamp"] = pd.to_datetime(data["timestamp"], unit='s')
    st.write(data)
    
    # # Upload a CSV file
    # csv_file = st.file_uploader("Upload a CSV file", type=["csv"])

    # if csv_file is not None:
    #     # Read the CSV file into a DataFrame
    #     df = pd.read_csv(csv_file)

    #     # Show the DataFrame
    #     st.write("CSV Data")
    #     st.write(df)

    #     # Select a key column for visualization
    #     key_column = st.selectbox("Select a key column for visualization", df.columns)

    #     # Visualization options
    #     visualization_option = st.selectbox("Select a visualization type", ["Bar Chart", "Line Chart"])

    #     if visualization_option == "Bar Chart":
    #         # Group the data by the selected key column and count the occurrences
    #         data = df[key_column].value_counts()

    #         # Create a bar chart
    #         st.bar_chart(data)

    #     elif visualization_option == "Line Chart":
    #         # Assuming the selected key column contains numeric data
    #         if df[key_column].dtype in [int, float]:
    #             # Create a line chart
    #             st.line_chart(df[key_column])
    #         else:
    #             st.warning("Selected key column must contain numeric data for a line chart.")
    # Upload a CSV file
    # Specify the path to the CSV file in the root directory

    # Read the CSV file into a DataFrame
    try:
        # df = pd.read_csv(csv_file_path)
        # st.write("CSV Data")
        df = data
        st.write(data)

        # Select a key column for visualization
        key_column = st.selectbox("Select a key column for visualization", df.columns)
        st.write(df.columns)
        df['Amount Per Gallon'] = df['Amount Per Gallon'].astype(float)
        print(df['Amount Per Gallon'])
        # Visualization options
        visualization_option = st.selectbox("Select a visualization type", ["Bar Chart", "Line Chart"])

        if visualization_option == "Bar Chart":
            # Group the data by the selected key column and count the occurrences
            data = df[key_column].value_counts()

            # Create a bar chart
            st.bar_chart(data)

        elif visualization_option == "Line Chart":
            try:
                # Convert the selected column to float and filter out complex numbers
                numeric_column = df[key_column].apply(pd.to_numeric, errors='coerce')
                numeric_column = numeric_column.dropna()
                st.write(numeric_column)
                if not numeric_column.empty:
                    st.line_chart(numeric_column)
                else:
                    st.warning("Selected key column contains complex or non-convertible data.")
            except ValueError:
                st.warning("Selected key column contains data that cannot be converted to float values.")
            except pd.errors.OutOfBoundsDatetime:
                st.warning("Selected key column contains date or time values, which cannot be plotted as a line chart.")

    except FileNotFoundError:
        st.error(f"CSV file not found at path: {csv_file_path}")


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
