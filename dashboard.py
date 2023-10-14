# import streamlit as st
import pandas as pd

class Dashboard():
    def __init__(self, data):
        self.data = {}
        self.data = data
        
        
    def get_operation_cost_per_hour(self):
        data = {}
        cost_of_oil_change = float(self.data["Cost of Oil Change"]) if self.data["Cost of Oil Change"] else 0
        hours_between_oil_change = float(self.data["Hours Between Oil Change"]) if self.data["Hours Between Oil Change"] else 0
        average_oil_consumption = float(self.data["Average Oil Consumption"]) if self.data["Average Oil Consumption"] else 0
        average_cost_of_oil = float(self.data["Average Cost of Oil"]) if self.data["Average Cost of Oil"] else 0
        data["Fuel"] = self.data["Amount Per Gallon"] * self.data["Average Fuel Consumption"]
        if hours_between_oil_change == 0:
            data["Oil Change / Oil Adds"] = 0
        else:
            data["Oil Change / Oil Adds"] = (cost_of_oil_change / hours_between_oil_change) + (average_oil_consumption * average_cost_of_oil)
        cost_of_overhaul = float(self.data.get("Cost of Overhaul", 0))  # Replace 0 with an appropriate default value
        time_different_overhaul = float(self.data.get("Time Different Overhaul", 1))  # Replace 1 with an appropriate default value
        if time_different_overhaul == 0:
            data["Engine Reserve"] = 0
        else:
            data["Engine Reserve"] = cost_of_overhaul / time_different_overhaul

        engine_reserve_option = float(self.data.get("Engine Reserve Option", 0))  # Replace 1 with an appropriate default value
        if engine_reserve_option == 0:
            data["Total Variable Cost Per Hour"] = data["Fuel"] + data["Oil Change / Oil Adds"]
        else:
            data["Total Variable Cost Per Hour"] = data["Fuel"] + data["Oil Change / Oil Adds"] + data["Engine Reserve"]
        return data
    

    def get_lookup(self, data=135):
        import pandas as pd
        # from rent.xlsx import data
        file_path = 'data/rent-or-buy-calculator.xlsx'  # Replace 'your_file.xlsx' with the actual file path
        engine = 'openpyxl'
        import pandas as pd
        df = pd.read_excel(file_path, sheet_name='Input', engine=engine)
        new_column_names = ['Column_A', 'Column_B', 'Column_C', 'Column_D', 'Column_E', 'Column_F', 'Column_G', 'Column_H', 'Column_I', 'Column_J']
        df.columns = new_column_names
        lookup_value = data
        result = df[df["Column_H"] <= lookup_value]['Column_I'].iloc[-1]
        return result
    

    def get_lookup2(self, data=135):
        import pandas as pd
        # from rent.xlsx import data
        file_path = 'data/rent-or-buy-calculator.xlsx'  # Replace 'your_file.xlsx' with the actual file path
        engine = 'openpyxl'
        import pandas as pd
        df = pd.read_excel(file_path, sheet_name='Input', engine=engine)
        new_column_names = ['Column_A', 'Column_B', 'Column_C', 'Column_D', 'Column_E', 'Column_F', 'Column_G', 'Column_H', 'Column_I', 'Column_J']
        df.columns = new_column_names
        lookup_value = data
        # result = df[df["Column_H"] <= lookup_value]['Column_J'].iloc[-1]
        result = df[df['Column_I'] == lookup_value]['Column_J'].iloc[0]

        return result
    

    def get_ownership_cost_per_year(self):
        data = {}
        data["Insurance"] = float(self.data["Annual Insurance Premium"])
        data["Hanger / Tierdown"] = float(self.data["Cost of Hanger"]) * 12
        data["Annual Inspection"] = float(self.data["Annual Inspection Maintenance"])
        data["Avionics Database Subscriptions"] = float(self.data["Avionic Database"])
        data["Annual Loan Payment"] = float(self.data["Monthly Loan Payment"]) * 12
        data["Annual Taxes and Registration"] = float(self.data["Annual Taxes Reg Fee"])
        data["Total Fixed Cost Per Year"] = float(data.get("Insurance", 0)) + float(data.get("Hanger / Tierdown", 0)) + float(data.get("Annual Inspection", 0)) + float(data.get("Avionics Database Subscriptions", 0)) + float(data.get("Annual Loan Payment", 0)) + float(data.get("Annual Taxes and Registration", 0))
        data["Fixed Cost Per Month"] = data["Total Fixed Cost Per Year"] / 12
        return data
    

    def get_others(self):
        data = {}
        data["Break Even Hours"] = float(self.get_lookup(float(self.data["Rental Cost/HR"])))
        data["Total Cost to Breakeven"] = data["Break Even Hours"] * self.get_operation_cost_per_hour()["Total Variable Cost Per Hour"] + self.get_ownership_cost_per_year()["Total Fixed Cost Per Year"]
        data["Cost Per Hour To Fly"] = float(self.get_lookup2(float(self.data["Hours Intend to Fly This Year"])))
        data["Cost to Fly those Hours"] = self.data["Hours Intend to Fly This Year"] * self.get_operation_cost_per_hour()["Total Variable Cost Per Hour"] + self.get_ownership_cost_per_year()["Total Fixed Cost Per Year"]
        data["Money Saved or Lost by Buying"] = self.data["Hours Intend to Fly This Year"] * self.data["Rental Cost/HR"] - data["Cost to Fly those Hours"]
        return data
    


# data = {
#   "timestamp": 1697115026,
#   "Aircraft Reg No": "",
#   "Amount Per Gallon": "4.75",
#   "Average Fuel Consumption": "8",
#   "Cost of Oil Change": "100",
#   "Hours Between Oil Change": "50",
#   "Average Oil Consumption": "0.15",
#   "Average Cost of Oil": "7.5",
#   "Cost of Overhaul": "20000",
#   "Time Different Overhaul": "1200",
#   "Annual Insurance Premium": "1200",
#   "Cost of Hanger": "50",
#   "Annual Inspection Maintenance": "1500",
#   "Avionic Database": "500",
#   "Annual Taxes Reg Fee": "255.0",
#   "Value of Aircraft": 50000,
#   "Money Down": 7500,
#   "Loan Balance": 42500,
#   "Loan Interest Rate": 4,
#   "Years of Loan": 20,
#   "Monthly Loan Payment": 257.541639952249,
#   "Rental Cost/HR": 135,
#   "Hours Intend to Fly This Year": 77
# }
# bs = Dashboard(data)

# bs.get_lookup(135)