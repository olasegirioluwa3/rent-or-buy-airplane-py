import streamlit as st
import pandas as pd

def main():
    st.title("Sales Forecast App")
    st.write("Welcome to Sales Forecast Application!")
    # Add a menu to navigate to other pages
    selected_page = st.sidebar.selectbox("Select a Page", ["Home", "Super Pixel Page", "Wasted Spend Calculator", "Page 4", "Page 5"])

    if selected_page == "Home":
        st.write("This is the home page.")
    if selected_page == "Home":
        st.write("This is the home page.")
    # Add links to other pages here

if __name__ == "__main__":
    main()
