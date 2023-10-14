import streamlit as st
import pandas as pd
import os
import csv
from pages.predict import run_prediction_app
from dashboard import Dashboard


def starter_data(data):
    # # Create the CSV file and write new data to it
    csv_file = "data.csv"
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
    
        # Write the header row with the keys from the JSON data
        writer.writerow(data.keys())
        
        # Write the data row with the values from the JSON data
        writer.writerow(data.values())
    return;


def create_fullraw(data):
    # # Create the CSV file and write new data to it
    csv_file = "fullraw.csv"
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
    
        # Write the header row with the keys from the JSON data
        writer.writerow(data.keys())
        
        # Write the data row with the values from the JSON data
        writer.writerow(data.values())
    return;


def add_to_fullraw(raw):
    # # Create the CSV file and write new data to it
    csv_file = "fullraw.csv"
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the data row with the values from the JSON data
        writer.writerow(raw.values())
    return;


def create_raw(data):
    # # Create the CSV file and write new data to it
    csv_file = "raw.csv"
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
    
        # Write the header row with the keys from the JSON data
        writer.writerow(data.keys())
        
        # Write the data row with the values from the JSON data
        writer.writerow(data.values())
    return;


def add_to_raw(raw):
    # # Create the CSV file and write new data to it
    csv_file = "raw.csv"
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Write the data row with the values from the JSON data
        writer.writerow(raw.values())
    return;


def main_stack(csv_file):

    # ds = new Dashboard
    # Initialize an empty dictionary to store the data
    data_dict = {}

    # Read the CSV file and convert it to a dictionary
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header row
        data = next(reader)    # Read the data row
        data_dict = dict(zip(header, data))


    
    st.title("RENT OR BUY CALCULATOR")
    sd = st.sidebar

    data = {}
    sd.title("INPUT")
    sd.subheader("Operating Costs | Variable")
    # data["timestamp"] = 
    import time

    current_timestamp = int(time.time())  # Get the current timestamp as an integer

    data["timestamp"] = current_timestamp
    data["Aircraft Reg No"] = sd.text_input("What is your Aircraft Registration Number (N- number)?", value=data_dict["Aircraft Reg No"])
    data["Amount Per Gallon"] = float(sd.text_input("How much do you pay for a gallon of aviation fuel?", value=data_dict["Amount Per Gallon"]))
    data["Average Fuel Consumption"] = float(sd.text_input("What is the average fuel consumption (in gallons/hour) for this aircraft?", value=data_dict["Average Fuel Consumption"]))
    data["Cost of Oil Change"] = float(sd.text_input("What is the cost per oil change (parts & labor, oil analysis)?", value=data_dict["Cost of Oil Change"]))
    data["Hours Between Oil Change"] = sd.text_input("How many hours between oil changes?", value=data_dict["Hours Between Oil Change"])
    data["Average Oil Consumption"] = sd.text_input("What is the average oil consumption (in quarts/hour) for this aircraft?", value=data_dict["Average Oil Consumption"])
    data["Average Cost of Oil"] = sd.text_input("What is the average cost for a quart of oil?", value=data_dict["Average Cost of Oil"])
    data["Cost of Overhaul"] = sd.text_input("How much does a factory overhaul cost for this engine?", value=data_dict["Cost of Overhaul"])
    data["Time Different Overhaul"] = sd.text_input("What is the factory recommended time between engine overhaul (hours)?", value=data_dict["Time Different Overhaul"])

    sd.subheader("Ownership Costs | Fixed")
    data["Annual Insurance Premium"] = sd.text_input("What is the Annual Insurance Premium?", value=data_dict["Annual Insurance Premium"])
    data["Cost of Hanger"] = sd.text_input("How much are the monthly hanger or Tie Down Costs?", value=data_dict["Cost of Hanger"])
    data["Annual Inspection Maintenance"] = sd.text_input("Estimate cost for annual inspection plus any misc. unscheduled maintenance during the year", value=data_dict["Annual Inspection Maintenance"])
    data["Avionic Database"] = sd.text_input("Annual Subscription costs for Avionics databases (Garmin/Sandel/Avidyne)?", value=data_dict["Avionic Database"])
    data["Annual Taxes Reg Fee"] = sd.text_input("Annual State Taxes and Registration Fee. (.005 of value + 5.00)", value=data_dict["Annual Taxes Reg Fee"])
    data["Value of Aircraft"] = float(sd.text_input("What is the value of the aircraft?", key="Value of Aircraft", value=data_dict["Value of Aircraft"]))
    data["Money Down"] = float(data.get("Value of Aircraft", 0)) * 0.15
    data["Loan Balance"] = float(data["Value of Aircraft"]) - float(data["Money Down"])
    data["Loan Interest Rate"] = float(sd.text_input("What is the loan interest rate?", value=data_dict["Loan Interest Rate"]))
    data["Years of Loan"] = float(sd.text_input("How many years is the loan for?", value=data_dict["Years of Loan"]))
    data["Engine Reserve Option"] = st.checkbox("Include Engine Reserve?", value=data_dict["Engine Reserve Option"])

    def calculate_monthly_payment(principal, annual_interest_rate, years):
        # Convert the annual interest rate to a monthly rate
        monthly_interest_rate = annual_interest_rate / 12 / 100

        # Convert the total number of years to months
        months = years * 12

        # Calculate the monthly payment using the formula
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**months) / ((1 + monthly_interest_rate)**months - 1)

        return monthly_payment
    
    data["Monthly Loan Payment"] = calculate_monthly_payment(data["Loan Balance"], data["Loan Interest Rate"], data["Years of Loan"])
    
    data["Rental Cost/HR"] = float(st.text_input("Rental Cost / HR", key="Rental Cost/HR", value=data_dict["Rental Cost/HR"]))
    data["Hours Intend to Fly This Year"] = float(st.text_input("How many years is the loan for?", key="Hours Intend to Fly This Year", value=data_dict["Hours Intend to Fly This Year"]))
        
    
    cal_button = st.button("CALCULATE")
    if cal_button:
        # Create an instance of the Dashboard class with the input data
        bs = Dashboard(data)
        
        # Calculate operation cost per hour
        operation_cost_per_hour = bs.get_operation_cost_per_hour()
        ownership_cost_per_year = bs.get_ownership_cost_per_year()
        others = bs.get_others()
        
        # Display the results
        others["Rental Cost/HR"] = data["Rental Cost/HR"]
        others["Hours Intend to Fly This Year"] = data["Hours Intend to Fly This Year"]

        st.write("Operation Cost Per Hour:")
        st.write(operation_cost_per_hour)
        st.write("Ownership Cost / Year:")
        st.write(ownership_cost_per_year)
        st.write("Others:")
        st.write(others)
        
        merged_data = {}
        merged_data.update(data)
        merged_data.update(operation_cost_per_hour)
        merged_data.update(ownership_cost_per_year)
        merged_data.update(others)
        st.write(merged_data)
        add_to_raw(data)
        add_to_fullraw(merged_data)
        starter_data(data)


def main():
    # pass

    st.title("RENT OR BUY CALCULATOR")
    sd = st.sidebar
    
    data = {}
    sd.title("INPUT")
    sd.subheader("Operating Costs | Variable")
    # data["timestamp"] = 
    import time

    current_timestamp = int(time.time())  # Get the current timestamp as an integer

    data["timestamp"] = current_timestamp
    data["Aircraft Reg No"] = sd.text_input("What is your Aircraft Registration Number (N- number)?")
    data["Amount Per Gallon"] = float(sd.text_input("How much do you pay for a gallon of aviation fuel?", value=4.75))
    data["Average Fuel Consumption"] = float(sd.text_input("What is the average fuel consumption (in gallons/hour) for this aircraft?", value=8))
    data["Cost of Oil Change"] = float(sd.text_input("What is the cost per oil change (parts & labor, oil analysis)?", value=100))
    data["Hours Between Oil Change"] = float(sd.text_input("How many hours between oil changes?", value=50))
    data["Average Oil Consumption"] = float(sd.text_input("What is the average oil consumption (in quarts/hour) for this aircraft?", value=0.15))
    data["Average Cost of Oil"] = float(sd.text_input("What is the average cost for a quart of oil?", value=7.50))
    data["Cost of Overhaul"] = float(sd.text_input("How much does a factory overhaul cost for this engine?", value=20000))
    data["Time Different Overhaul"] = float(sd.text_input("What is the factory recommended time between engine overhaul (hours)?", value=1200))

    sd.subheader("Ownership Costs | Fixed")
    data["Annual Insurance Premium"] = float(sd.text_input("What is the Annual Insurance Premium?", value=1200))
    data["Cost of Hanger"] = float(sd.text_input("How much are the monthly hanger or Tie Down Costs?", value=50))
    data["Annual Inspection Maintenance"] = float(sd.text_input("Estimate cost for annual inspection plus any misc. unscheduled maintenance during the year", value=1500))
    data["Avionic Database"] = float(sd.text_input("Annual Subscription costs for Avionics databases (Garmin/Sandel/Avidyne)?", value=500))
    data["Annual Taxes Reg Fee"] = float(sd.text_input("Annual State Taxes and Registration Fee. (.005 of value + 5.00)", value=255.0))
    data["Value of Aircraft"] = float(sd.text_input("What is the value of the aircraft?", key="Value of Aircraft", value=50000))
    data["Money Down"] = float(data.get("Value of Aircraft", 0)) * 0.15
    data["Loan Balance"] = float(data["Value of Aircraft"]) - float(data["Money Down"])
    data["Loan Interest Rate"] = float(sd.text_input("What is the loan interest rate?", value=4.0))
    data["Years of Loan"] = float(sd.text_input("How many years is the loan for?", value=20))
    data["Engine Reserve Option"] = st.checkbox("Include Engine Reserve?", value=False)
    def calculate_monthly_payment(principal, annual_interest_rate, years):
        # Convert the annual interest rate to a monthly rate
        monthly_interest_rate = annual_interest_rate / 12 / 100

        # Convert the total number of years to months
        months = years * 12

        # Calculate the monthly payment using the formula
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**months) / ((1 + monthly_interest_rate)**months - 1)

        return monthly_payment
    
    data["Monthly Loan Payment"] = calculate_monthly_payment(data["Loan Balance"], data["Loan Interest Rate"], data["Years of Loan"])
    
    data["Rental Cost/HR"] = float(st.text_input("Rental Cost / HR", key="Rental Cost/HR", value=135.00))
    data["Hours Intend to Fly This Year"] = float(st.text_input("How many hours do you intend to fly this year?", key="Hours Intend to Fly This Year", value=77))

    cal_button = st.button("CALCULATE")
    if cal_button:
        # Create an instance of the Dashboard class with the input data
        bs = Dashboard(data)
        
        # Calculate operation cost per hour
        operation_cost_per_hour = bs.get_operation_cost_per_hour()
        ownership_cost_per_year = bs.get_ownership_cost_per_year()
        others = bs.get_others()
        # Display the results
        st.write("All data")
        st.write(operation_cost_per_hour)
        st.write("Ownership Cost / Year:")
        st.write(ownership_cost_per_year)
        st.write("Others:")
        st.write(others)
        merged_data = {}
        merged_data.update(data)
        merged_data.update(operation_cost_per_hour)
        merged_data.update(ownership_cost_per_year)
        merged_data.update(others)
        create_raw(data)
        create_fullraw(merged_data)
        starter_data(data)


if __name__ == "__main__":
    
    sd = st.sidebar
    sd.image("assets/logo.png", width='100%', use_column_width=True)
    
    # Define the CSV file name
    csv_file = "data.csv"

    # Check if the CSV file exists
    if os.path.isfile(csv_file):
        # Check if the file is not empty
        if os.path.getsize(csv_file) > 0:
            main_stack(csv_file)
        else:
            print("CSV file is empty. Updating with new data.")
            main()

    else:
        main()
    # elif navigation == "Predict":
    #     st.markdown('<a href="/predict">Go to Prediction Page</a>', unsafe_allow_html=True)
