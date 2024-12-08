import streamlit as st

# Set the page config
st.set_page_config(
    page_title="Betting Tools Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for full dark grey background and styling
st.markdown("""
    <style>
        /* Change background color of the main content */
        .stApp {
            background-color: #1E1E1E;  /* Dark grey background */
        }
        /* Make all text white */
        * {
            color: #FFFFFF;  /* White text */
        }
        .stTextInput > label {
            color: #FFFFFF; /* Ensure input labels are white */
        }
        /* Style for input boxes */
        input {
            width: 33%; /* Reduce input box width to 1/3 size */
            background-color: #EAEAEA; /* Light grey input fields */
            color: #000000; /* Black text inside input fields */
        }
        /* Result box styling */
        .result-box {
            border: 2px solid #FFFFFF;  /* White border */
            padding: 5px;
            margin-top: 29px; /* Align height with inputs */
            text-align: center;
            border-radius: 5px;
            width: 45%;  /* Full width of its column */
            display: inline-block;
        }
        /* Specific text styling */
        .ok {
            color: #00FF00; /* Green for OK */
        }
        .off2 {
            color: #800080; /* Purple for OFF 2 */
        }
        .off1 {
            color: #FF0000; /* Red for OFF 1 */
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.header("Tools Menu")
    page = st.radio(
        "Select a Tool:",
        (
            "Off Prices Calculator",
            "Surebet Calculator",
            "Margins Removal",
            "Alternative Lines Converter",
            "General Tab 1",
            "General Tab 2"
        )
    )

# Main content area
if page == "Off Prices Calculator":
    st.title("Off Prices Calculator")
    st.markdown("<div class='horizontal-bar'></div>", unsafe_allow_html=True)
    st.write("This is the page for the Off Prices Calculator.")
    # Placeholder for Off Prices Calculator content

elif page == "Surebet Calculator":
    st.title("Surebet Calculator")
    st.markdown("<div class='horizontal-bar'></div>", unsafe_allow_html=True)
    st.write("This is the page for the Surebet Calculator.")
    # Placeholder for Surebet Calculator content

elif page == "Margins Removal":
    st.title("Margins Removal")
    st.markdown("<div class='horizontal-bar'></div>", unsafe_allow_html=True)
    st.write("This is the page for Margins Removal.")
    # Placeholder for Margins Removal content

elif page == "Alternative Lines Converter":
    st.title("Alternative Lines Converter")
    st.markdown("<div class='horizontal-bar'></div>", unsafe_allow_html=True)
    st.write("This is the page for the Alternative Lines Converter.")
    # Placeholder for Alternative Lines Converter content

elif page == "General Tab 1":
    st.title("General Tab 1")
    st.markdown("<div class='horizontal-bar'></div>", unsafe_allow_html=True)
    st.write("This i
