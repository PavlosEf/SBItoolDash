import streamlit as st

# Function to calculate stakes and arbitrage
def calculate_surebet(w1_odds, w2_odds, w1_stake=None, w2_stake=None, total_stake=None):
    # Ensure manual stakes are used directly
    if w1_stake is not None and w2_stake is not None:
        total_stake = w1_stake + w2_stake
    elif total_stake is not None:
        # Calculate stakes from total stake
        w1_stake = total_stake / (1 + w1_odds / w2_odds)
        w2_stake = total_stake - w1_stake

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
st.markdown("Calculate stakes and profits for arbitrage betting scenarios.")

# Input Fields
st.markdown("### Input Parameters")
with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        w1_odds = st.number_input("W1 Odds (Kaizen Bet)", min_value=1.01, value=2.5, step=0.01)
    with col2:
        w2_odds = st.number_input("W2 Odds (Competition Bet)", min_value=1.01, value=2.0, step=0.01)

# Dynamic Input for W1, W2, and Total stakes
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    w1_stake = st.number_input("W1 Stake (€)", min_value=0.0, step=0.01, value=0.0)
with col2:
    w2_stake = st.number_input("W2 Stake (€)", min_value=0.0, step=0.01, value=0.0)
with col3:
    total_stake = st.number_input("Total Stake (€)", min_value=0.0, step=0.01, value=0.0)

# Calculation Button
if st.button("Calculate"):
    if w1_stake > 0 and w2_stake > 0:
        # Use manual stakes if provided
        results = calculate_surebet(w1_odds, w2_odds, w1_stake=w1_stake, w2_stake=w2_stake)
    elif total_stake > 0:
        # Calculate stakes from total stake
        results = calculate_surebet(w1_odds, w2_odds, total_stake=total_stake)
    else:
        results = None

    # Display Results
    if results:
        st.markdown("### Results")
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
            </style>
            <div class="result-box">
                <h4>Calculation Results:</h4>
                <ul>
                    <li>W1 Stake: €{results['W1 Stake']}</li>
                    <li>W2 Stake: €{results['W2 Stake']}</li>
                    <li>Total Stake: €{results['Total Stake']}</li>
                    <li>Profit W1: €{results['Profit W1']}</li>
                    <li>Profit W2: €{results['Profit W2']}</li>
                    <li>Arbitrage %: {results['Arbitrage %']}%</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
