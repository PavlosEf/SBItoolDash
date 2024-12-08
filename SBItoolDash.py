import streamlit as st

# Set the page config
st.set_page_config(
    page_title="Betting Tools Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #2b2b2b;
    }
   
    /* Font and layout adjustments */
    body {
        color: #e0e0e0;
        background-color: #1e1e1e;
    }
    .css-1hynsf2 {
        background-color: #444444 !important;
    }
    h1, h2, h3, h4, h5 {
        color: #e0e0e0 !important;
    }
    .css-10trblm {
        color: #e0e0e0;
    }
    /* Main dashboard area */
    .dashboard-container {
        background-color: #2b2b2b;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
    }
    /* Buttons and inputs styling */
    .stButton>button {
        background-color: #333333;
        color: #e0e0e0;
        border: 1px solid #555555;
        border-radius: 5px;
        padding: 0.5em 1em;
        font-size: 1rem;
    }
    .stButton>button:hover {
        background-color: #555555;
        border: 1px solid #777777;
    }
    input, textarea {
        background-color: #333333;
        color: #e0e0e0;
        border: 1px solid #555555;
        border-radius: 5px;
        padding: 0.5em;
    }
    input:focus, textarea:focus {
        border: 1px solid #777777;
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
st.markdown("<div class='dashboard-container'>", unsafe_allow_html=True)
if page == "Off Prices Calculator":
    st.title("Off Prices Calculator")
    st.write("This is the page for the Off Prices Calculator.")
    # Placeholder for Off Prices Calculator content

elif page == "Surebet Calculator":
    st.title("Surebet Calculator")
    st.write("This is the page for the Surebet Calculator.")
    # Placeholder for Surebet Calculator content

elif page == "Margins Removal":
    st.title("Margins Removal")
    st.write("This is the page for Margins Removal.")
    # Placeholder for Margins Removal content

elif page == "Alternative Lines Converter":
    st.title("Alternative Lines Converter")
    st.write("This is the page for the Alternative Lines Converter.")
    # Placeholder for Alternative Lines Converter content

elif page == "General Tab 1":
    st.title("General Tab 1")
    st.subheader("Off Prices Calculator")
    
   # Set the page title and layout
st.set_page_config(page_title="Price Difference Calculator", layout="centered")

# Add custom CSS for dark background and styling
st.markdown(
    """
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
          .result-box {
            border: 2px solid #FFFFFF;  /* White border */
            padding: 5px;
            margin-top: 29px; /* Align height with inputs */
            text-align: center;
            border-radius: 5px;
            width: 45%;  /* Full width of its column */
            display: inline-block;
}
        }
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
    """,
    unsafe_allow_html=True,
)

# Page title and description
st.title("Off Prices Calculator")
st.markdown("Enter prices below to calculate the percentage difference for up to 10 rows.")

# Helper function to parse numbers (handles commas and periods)
def parse_number(number_str):
    try:
        return float(number_str.replace(",", "."))
    except ValueError:
        return None

# Calculate label outcome based on the difference
def get_label(difference):
    if difference > -2:
        return '<div class="result-box ok">OK</div>'
    elif -2 >= difference >= 2:
        return '<div class="result-box off2">OFF 2</div>'
    elif difference < -2:
        return '<div class="result-box off1">OFF 1</div>'
    else:
        return '<div class="result-box">None</div>'

# Create input fields and calculate results
for i in range(10):
    col1, col2, col3, col4 = st.columns([1, 1, 1.6, 1])  # Adjust column sizes
    
    with col1:
        price_a = st.text_input(f"Kaizen Odds {i + 1}:", key=f"price_a_{i}")
    with col2:
        price_b = st.text_input(f"Competition Odds {i + 1}:", key=f"price_b_{i}")
    
    # Ensure inputs are provided
    if price_a and price_b:
        parsed_a = parse_number(price_a)
        parsed_b = parse_number(price_b)
        if parsed_a and parsed_b and parsed_a > 0 and parsed_b > 0:
            # Calculate percentage difference
            difference = ((1 / parsed_a) - (1 / parsed_b)) * 100
            
            # Display percentage difference in a styled box
            with col3:
                st.markdown(
                    f'<div class="result-box">{difference:.2f}%</div>',
                    unsafe_allow_html=True,
                )
            
            # Display label in a styled box
            with col4:
                st.markdown(get_label(difference), unsafe_allow_html=True)

    
    # Button for calculation (can be expanded later)
    st.button("Calculate")

elif page == "General Tab 2":
    st.title("General Tab 2")
    st.write("This is a placeholder for future tools.")
    # Placeholder for General Tab 2 content
st.markdown("</div>", unsafe_allow_html=True)
