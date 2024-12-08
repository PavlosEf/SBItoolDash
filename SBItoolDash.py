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
        /* Make all text in the main content white */
        .stApp * {
            color: #FFFFFF !important;
        }
        /* Ensure all text in the sidebar is white */
        section[data-testid="stSidebar"] * {
            color: #FFFFFF !important;
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
    st.markdown("Enter prices below to calculate the percentage difference for up to 10 rows.")

    # Add custom CSS for dark background and styling
    st.markdown(
    """
    <style>
        /* Input fields with black text */
        input[type="text"] {
           width: 100% !important; /* Ensure input area takes full width of the column */
           max-width: 200px !important; /* Limit the maximum size of the box */
           background-color: #EAEAEA !important; /* Light grey background */
           color: #000000 !important; /* Black text */
           caret-color: #000000 !important; /* Black caret for typing */
           padding: 5px !important; /* Adjust padding for a compact input */
           border-radius: 5px; /* Optional: keep rounded corners */
        }

        /* Result boxes for percentage */
       .result-box {
            border: 2px solid #FFFFFF; /* White border */
            padding: 5px;
            margin: 5px 10px; /* Adjust the spacing around the box */
            text-align: center;
            border-radius: 5px;
            width: 70px; /* Smaller width */
            display: inline-block;
            position: relative; /* Adjust position relative to normal flow */
            top: 20px; /* Moves the box slightly up */
        }
       
     .result-container {
            display: flex; /* Use flexbox for alignment */
            align-items: center; /* Vertically align items */
            justify-content: flex-start; /* Align items to the left */
            gap: 20px; /* Add spacing between the percentage and label boxes */
            margin-top: 5px; /* Optional: Add some space above the container */
        }


        /* Color-coded labels */
        .ok {
            color: #FFFFFF;
            background-color: #00FF00; /* Green for OK */
            border: 2px solid #00FF00;
        }

        .off2 {
            color: #FFFFFF;
            background-color: #800080; /* Purple for OFF 2 */
            border: 2px solid #800080;
        }

        .off1 {
            color: #FFFFFF;
            background-color: #FF0000; /* Red for OFF 1 */
            border: 2px solid #FF0000;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

    # Define helper functions
    def parse_number(number_str):
        try:
            return float(number_str.replace(",", "."))
        except ValueError:
            return None

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
        col1, col2, col3, col4 = st.columns([0.3, 0.3, 1, 1])  # Adjust column sizes
        
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
