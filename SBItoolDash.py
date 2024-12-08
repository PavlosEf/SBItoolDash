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
    st.markdown("Enter prices below to calculate the percentage difference Kaizen odds are 1st! .")

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
            gap: 2px; /* Add spacing between the percentage and label boxes */
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
        elif -3 <= difference <= -2:
            return '<div class="result-box off2">OFF 2</div>'
        elif difference < -3:
            return '<div class="result-box off1">OFF 1</div>'
        else:
            return '<div class="result-box">None</div>'

    # Create input fields and calculate results
    for i in range(5):
        col1, col2, col3, col4 = st.columns([0.3, 0.3, 1, 1])  # Adjust column sizes
        
        with col1:
            price_a = st.text_input(f"Kaizen Odds {i + 1}:", key=f"price_a_{i}")
        with col2:
            price_b = st.text_input(f"Competition Odds {i + 1}:", key=f"price_b_{i}")
        
        if price_a and price_b:
            parsed_a = parse_number(price_a)
            parsed_b = parse_number(price_b)
       
            if parsed_a and parsed_b and parsed_a > 0 and parsed_b > 0:
                 # Calculate percentage difference
                 difference = ((1 / parsed_a) - (1 / parsed_b)) * 100

                    # Display percentage difference and label together in col3
                 with col3:
                     st.markdown(
                         f"""
                         <div class="result-container">
                             <div class="result-box">{difference:.2f}%</div>
                             {get_label(difference)}
                         </div>
                         """,
                         unsafe_allow_html=True,
                     )
elif selected_tool == "Surebet Calculator":
    st.title("Surebet Calculator")
    st.write("Placeholder for the Surebet Calculator.")
    # Add your Surebet Calculator logic here

elif selected_tool == "Top Price / Betfair Calculator":
    st.title("Top Price / Betfair Calculator")
    st.write("Placeholder for the Top Price / Betfair Calculator.")

    # Define the function for calculation
    def calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission):
        """
        Calculate lay stake, liability, and profit for a back and lay bet.
        """
        # Calculate the lay stake
        lay_stake = (back_stake * back_odds) / lay_odds

        # Calculate the liability
        liability = lay_stake * (lay_odds - 1)

        # Calculate potential outcomes
        back_bet_win = (back_stake * (back_odds - 1)) - liability
        lay_bet_win = lay_stake * (1 - commission / 100)

        return {
            "Lay Stake": round(lay_stake, 2),
            "Liability": round(liability, 2),
            "Profit if Back Bet Wins": round(back_bet_win, 2),
            "Profit if Lay Bet Wins": round(lay_bet_win, 2),
        }

    # Input fields
    st.subheader("Input Parameters")

    # Input fields in the main content area
    col1, col2 = st.columns(2)

    with col1:
        back_stake = st.number_input("Back Stake (£):", min_value=0.0, value=10.0, step=1.0)
        back_odds = st.number_input("Back Odds (decimal):", min_value=1.01, value=2.5, step=0.01)

    with col2:
        lay_odds = st.number_input("Lay Odds (decimal):", min_value=1.01, value=2.4, step=0.01)
        commission = st.slider("Exchange Commission (%):", min_value=0.0, max_value=100.0, value=5.0)

    # Add a Calculate button
    if st.button("Calculate"):
        # Calculate results
        results = calculate_back_lay_bet(back_stake, back_odds, lay_odds, commission)

        # Results Display
        st.subheader("Calculation Results")
        st.write(f"### Lay Stake: £{results['Lay Stake']}")
        st.write(f"### Liability: £{results['Liability']}")
        st.write(f"### Profit if Back Bet Wins: £{results['Profit if Back Bet Wins']}")
        st.write(f"### Profit if Lay Bet Wins: £{results['Profit if Lay Bet Wins']}")

        # Summary Table
        st.table(
            {
                "Outcome": ["Back Bet Wins", "Lay Bet Wins"],
                "Profit (£)": [results["Profit if Back Bet Wins"], results["Profit if Lay Bet Wins"]],
            }
        )
    
    else:
        st.write("Please input values and click the **Calculate** button to see results.")

    # Footer
    st.markdown("---")


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
