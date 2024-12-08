import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Betting Tools", layout="wide")

# Define the sidebar with navigation
st.sidebar.title("Navigation")
options = ["Off Prices Calculator", "Surebet Calculator", "Margins Removal", "Alternative Lines Converter", "General Tab 1", "General Tab 2"]
selected_option = st.sidebar.selectbox("Select a tool", options)

# Set the background color
st.markdown(
    """
    <style>
    .reportview-container {
        background: #2E2E2E;  /* This is the sidebar background */
    }
    .sidebar .sidebar-content {
        background: #2E2E2E;  /* This is the sidebar content background */
    }
    .main {
        background-color: #1E1E1E;  /* This is the main content area background */
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function for Off Prices Calculator
def off_prices_calculator():
    st.title("Off Prices Calculator")
    # Add your calculator logic here
    st.write("This is where the Off Prices Calculator will be implemented.")

# Function for Surebet Calculator
def surebet_calculator():
    st.title("Surebet Calculator")
    # Add your calculator logic here
    st.write("This is where the Surebet Calculator will be implemented.")

# Function for Margins Removal
def margins_removal():
    st.title("Margins Removal")
    # Add your calculator logic here
    st.write("This is where the Margins Removal tool will be implemented.")

# Function for Alternative Lines Converter
def alternative_lines_converter():
    st.title("Alternative Lines Converter")
    # Add your calculator logic here
    st.write("This is where the Alternative Lines Converter will be implemented.")

# Function for General Tab 1
def general_tab_1():
    st.title("General Tab 1")
    # Add your content here
    st.write("This is where General Tab 1 content will be implemented.")

# Function for General Tab 2
def general_tab_2():
    st.title("General Tab 2")
    # Add your content here
    st.write("This is where General Tab 2 content will be implemented.")

# Display the selected tool
if selected_option == "Off Prices Calculator":
    off_prices_calculator()
elif selected_option == "Surebet Calculator":
    surebet_calculator()
elif selected_option == "Margins Removal":
    margins_removal()
elif selected_option == "Alternative Lines Converter":
    alternative_lines_converter()
elif selected_option == "General Tab 1":
    general_tab_1()
elif selected_option == "General Tab 2":
    general_tab_2()
