import streamlit as st
import os

# Create a function to run the main Streamlit app
def run_main_app():
    st.title("RENT OR BUY CALCULATOR")
    st.sidebar.title("NAVIGATION")

    # Define the navigation options
    navigation = st.sidebar.radio("Choose an option:", ["Home", "Predict"])

    if navigation == "Home":
        show_home_page()
    elif navigation == "Predict":
        st.markdown('<a href="/predict">Go to Prediction Page</a>', unsafe_allow_html=True)

# Define the home page content
def show_home_page():
    st.write("Welcome to the Rent or Buy Calculator!")
    st.write("Please use the sidebar to navigate to the 'Predict' page for predictions.")

if __name__ == "__main__":
    run_main_app()
