import streamlit as st
from streamlit import components

# Import the individual page files
import home
import pages.income_statement as income_statement
import pages.balance_sheet as balance_sheet
from Balance_sheet_class import BalanceSheet
# Create a SessionState class for managing page state
class SessionState:
    def __init__(self):
        self.page = "Home"  # Default page is Home

# Create a shared session state
session_state = SessionState()

# Define the page names and their corresponding functions
pages = {
    "Home": home.main,
    "Income Statement": income_statement.income_statement,
    "Balance Sheet": balance_sheet.balance_sheet,
}

# Create the horizontal navbar
# st.sidebar.title("Sales Forecast Model")
st.title("Sales Forecast Model")
# selected_page = st.sidebar.radio("Go to", list(pages.keys()))
# session_state.page = selected_page

# Display the selected page
# pages[session_state.page]()
