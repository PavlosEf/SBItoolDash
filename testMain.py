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

import streamlit as st

# Function to calculate stakes and arbitrage
def calculate_surebet(w1_odds, w2_odds, w1_stake=None, w2_stake=None, total_stake=None):
    if total_stake:
        # Split total stake for equal profit
        w1_stake = total_stake / (1 + w1_odds / w2_odds)
        w2_stake = total_stake - w1_stake
    elif w1_stake:
        # Calculate w2 stake for equal profit
        w2_stake = (w1_stake * w1_odds) / w2_odds
        total_stake = w1_stake + w2_stake
    elif w2_stake:
        # Calculate w1 stake for equal profit
        w1_stake = (w2_stake * w2_odds) / w1_odds
        total_stake = w1_stake + w2_stake

    # Calculate profits
    profit_w1 = (w1_odds * w1_stake) - total_stake
    profit_w2 = (w2_odds * w2_stake) - total_stake

    # Calculate arbitrage percentage
    arbitrage_percentage = max(profit_w1, profit_w2) / total_stake * 100

    return {
        "W1 Stake": round(w1_stake, 2),
        "W2 Stake": round(w2_stake, 2),
        "Total Stake": round(total_stake, 2),
        "Profit W1": round(profit_w1, 2),
        "Profit W2": round(profit_w2, 2),
        "Arbitrage %": round(arbitrage_percentage, 2)
    }

# Layout
st.title("Surebet Calculator")
st.markdown("Calculate stakes and profits for arbitrage betting scenarios dynamically.")

# Input Fields
st.markdown("### Input Parameters")
with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        w1_odds = st.number_input("Kaizen Odds", min_value=1.01, value=2.5, step=0.01)
    with col2:
        w2_odds = st.number_input("Competition Odds", min_value=1.01, value=2.0, step=0.01)

# Dynamic Input for W1, W2, and Total stakes
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    w1_stake = st.number_input("Kaizen Stakes (€)", min_value=0.0, step=0.01, value=0.0)
with col2:
    w2_stake = st.number_input("Competition Stakes (€)", min_value=0.0, step=0.01, value=0.0)
with col3:
    total_stake = st.number_input("Total Stake (€)", min_value=0.0, step=0.01, value=0.0)

# Dynamic Calculation
if total_stake > 0:
    # Scenario 3: Total Stake provided
    results = calculate_surebet(w1_odds, w2_odds, total_stake=total_stake)
elif w1_stake > 0 and w2_stake == 0:
    # Scenario 1: W1 Stake provided
    results = calculate_surebet(w1_odds, w2_odds, w1_stake=w1_stake)
elif w2_stake > 0 and w1_stake == 0:
    # Scenario 2: W2 Stake provided
    results = calculate_surebet(w1_odds, w2_odds, w2_stake=w2_stake)
elif w1_stake > 0 and w2_stake > 0:
    # Scenario 4: Both W1 and W2 stakes provided
    results = calculate_surebet(w1_odds, w2_odds, w1_stake=w1_stake, w2_stake=w2_stake)
else:
    results = None

# Display Results
if results:
    st.markdown("### Results")

    # Styling for Arbitrage and Profits
    arbitrage_color = "green" if results["Arbitrage %"] > 0 else "red"
    profit_w1_color = "green" if results["Profit W1"] > 0 else "red"
    profit_w2_color = "green" if results["Profit W2"] > 0 else "red"

    st.markdown(
        f"""
        <style>
        .result-box {{
            background-color: #3E4E56;
            border: 1px solid #DEE2E6;
            border-radius: 8px;
            padding: 15px;
            margin: 10px;
            color: #FFFFFF;
        }}
        .result-box h4 {{
            margin-bottom: 10px;
            text-decoration: underline;
        }}
        .result-box ul {{
            list-style-type: none;
            padding: 0;
        }}
        .result-box ul li {{
            margin-bottom: 5px;
        }}
        .arbitrage {{
            color: {arbitrage_color};
            font-weight: bold;
        }}
        .profit-w1 {{
            color: {profit_w1_color};
            font-weight: bold;
        }}
        .profit-w2 {{
            color: {profit_w2_color};
            font-weight: bold;
        }}
        </style>
        <div class="result-box">
            <h4>Calculation Results:</h4>
            <ul>
                <li>Kaizen Stakes: {results['W1 Stake']}€</li>
                <li>Competition Stakes: {results['W2 Stake']}€</li>
                <li>Total Stake: {results['Total Stake']}€</li>
                <li>Profit Kaizen: <span class="profit-w1">{results['Profit W1']}€</span></li>
                <li>Profit Competition: <span class="profit-w2">{results['Profit W2']}€</span></li>
                <li>Arbitrage: <span class="arbitrage">{results['Arbitrage %']}%</span></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif selected_tool == "Top Price / Betfair Calculator":
    st.title("Top Price / Betfair Calculator")

    # Function for calculation
    def calculate_back_lay_bet(back_stake, back_odds, lay_odds):
        lay_stake = (back_stake * back_odds) / lay_odds
        liability = lay_stake * (lay_odds - 1)

        # Back Bet Outcomes
        back_bet_profit_win = back_stake * (back_odds - 1)  # Profit when back bet wins
        back_bet_profit_lose = -back_stake  # Loss when back bet loses

        # Lay Bet Outcomes
        lay_bet_profit_win = -liability  # Loss when lay bet loses
        lay_bet_profit_lose = lay_stake  # Profit when lay bet wins

        # Market Profit (combined outcomes)
        market_profit_win = back_bet_profit_win + lay_bet_profit_win
        market_profit_lose = back_bet_profit_lose + lay_bet_profit_lose

        return {
            "Lay Stake": round(lay_stake, 2),
            "Liability": round(liability, 2),
            "Back Bet Profit Win": round(back_bet_profit_win, 2),
            "Back Bet Profit Lose": round(back_bet_profit_lose, 2),
            "Lay Bet Profit Win": round(lay_bet_profit_win, 2),
            "Lay Bet Profit Lose": round(lay_bet_profit_lose, 2),
            "Market Profit Win": round(market_profit_win, 2),
            "Market Profit Lose": round(market_profit_lose, 2),
        }

    # Input Fields
    st.markdown("### Input Parameters")
    with st.container():
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            back_odds = st.number_input("Back Odds", min_value=1.01, value=2.5, step=0.01)
        with col2:
            lay_odds = st.number_input("Lay Odds", min_value=1.01, value=2.4, step=0.01)
        with col3:
            back_stake = st.number_input("Back Stake (€)", min_value=0.0, value=100.0, step=1.0)

    # Calculate Lay Stake on Input
    calculated_lay_stake = (back_stake * back_odds) / lay_odds
    calculated_total_stake = back_stake + calculated_lay_stake

    # Dynamic Input Boxes for Lay Stake and Total Stake
    col1, col2 = st.columns([1, 1])
    with col1:
        lay_stake = st.number_input(
            "Lay Stake (€)", min_value=0.0, value=round(calculated_lay_stake, 2), step=0.01
        )
    with col2:
        total_stake = st.number_input(
            "Total Stake (€)", min_value=0.0, value=round(calculated_total_stake, 2), step=0.01
        )

    # Adjust Lay Stake and Total Stake Dynamically
    if lay_stake != round(calculated_lay_stake, 2):
        total_stake = back_stake + lay_stake
    elif total_stake != round(calculated_total_stake, 2):
        lay_stake = total_stake - back_stake

    # Calculation Button
    if st.button("Calculate"):
        results = calculate_back_lay_bet(back_stake, back_odds, lay_odds)

        # Display Results
        st.markdown("### Results Breakdown")

        # Simplified Display
        st.markdown(
            f"""
            <style>
            .result-box {{
                background-color: #3E4E56;
                border: 1px solid #DEE2E6;
                border-radius: 8px;
                padding: 15px;
                margin: 10px;
                color: #FFFFFF;
            }}
            .result-box h4 {{
                margin-bottom: 10px;
                text-decoration: underline;
            }}
            .result-box ul {{
                list-style-type: none;
                padding: 0;
            }}
            .result-box ul li {{
                margin-bottom: 5px;
            }}
            .warning {{
                color: red;
                font-weight: bold;
            }}
            </style>
            <div class="result-box">
                <h4>If Win:</h4>
                <ul>
                    <li>Back Bet Profit: €{results['Back Bet Profit Win']}</li>
                    <li>Lay Bet Profit: €{results['Lay Bet Profit Win']}</li>
                    <li>Market Profit: €{results['Market Profit Win']}</li>
                </ul>
                <h4>If Lose:</h4>
                <ul>
                    <li>Back Bet Profit: €{results['Back Bet Profit Lose']}</li>
                    <li>Lay Bet Profit: €{results['Lay Bet Profit Lose']}</li>
                    <li>Market Profit: €{results['Market Profit Lose']}</li>
                </ul>
            </div>
            <p class="warning">In case the outcome confirms in Exchange it will be applied a Commission (%) on the NET winnings. Most exchanges are on 2%.</p>
            """,
            unsafe_allow_html=True,
        )


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
