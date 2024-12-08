import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Betting Tools Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling the dark theme
st.markdown("""
    <style>
        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #2B3A42; /* Dark grey sidebar background */
            color: #FFFFFF; /* White text in the sidebar */
        }
        section[data-testid="stSidebar"] h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF; /* Ensure all headers in the sidebar are white */
        }
        section[data-testid="stSidebar"] label {
            color: #FFFFFF; /* Sidebar labels */
        }

        /* Main content styling */
        .stApp {
            background-color: #3E4E56; /* Main content background */
            color: #FFFFFF; /* White text for the main area */
        }

        /* Customize radio buttons (optional) */
        div[data-testid="stSidebar"] .st-radio > label {
            color: #FFFFFF; /* White radio button text */
        }

        /* Add some padding to the sidebar */
        section[data-testid="stSidebar"] {
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("Tools Menu")
    selected_tool = st.radio(
        "Select a Tool:",
        [
            "Off Prices Calculator",
            "Surebet Calculator",
            "Top Price / Betfair Calculator",
            "Margins Removal",
            "Alternative Lines Converter",
            "General Tab 1",
            "General Tab 2"
        ]
    )

# Main content area
if selected_tool == "Off Prices Calculator":
    st.title("Off Prices Calculator")
    st.write("Placeholder for the Off Prices Calculator.")
    # Add your Off Prices Calculator logic here

elif selected_tool == "Surebet Calculator":
    st.title("Surebet Calculator")
    st.write("Placeholder for the Surebet Calculator.")
    # Add your Surebet Calculator logic here

elif selected_tool == "Top Price / Betfair Calculator":
    st.title("Top Price / Betfair Calculator")
    st.write("Placeholder for the Top Price / Betfair Calculator.")
    # Add your Top Price / Betfair Calculator logic here

elif selected_tool == "Margins Removal":
    st.title("Margins Removal")
    st.write("Placeholder for Margins Removal.")
    # Add your Margins Removal logic here

elif selected_tool == "Alternative Lines Converter":
    st.title("Alternative Lines Converter")
    st.write("Placeholder for the Alternative Lines Converter.")
    # Add your Alternative Lines Converter logic here

elif selected_tool == "General Tab 1":
    st.title("General Tab 1")
    st.write("Placeholder for General Tab 1.")
    # Add any future tools or functionality here

elif selected_tool == "General Tab 2":
    st.title("General Tab 2")
    st.write("Placeholder for General Tab 2.")
    # Add any future tools or functionality here
