import streamlit as st

# Function to calculate stakes and arbitrage
def calculate_surebet(odds, total_stake=None):
    num_outcomes = len(odds)

    if total_stake:
        # Calculate stakes for equal profit
        total_inverse_odds = sum(1 / o for o in odds)
        stakes = [(total_stake / total_inverse_odds) * (1 / o) for o in odds]

    # Calculate profits for each outcome
    profits = [(odds[i] * stakes[i]) - total_stake for i in range(num_outcomes)]

    # Calculate arbitrage percentage
    arbitrage_percentage = max(profits) / total_stake * 100 if total_stake > 0 else 0

    return {
        "Stakes": [round(s, 2) for s in stakes],
        "Total Stake": round(total_stake, 2),
        "Profits": [round(p, 2) for p in profits],
        "Arbitrage %": round(arbitrage_percentage, 2)
    }

# Layout
st.title("Surebet Calculator")
st.markdown("Calculate stakes and profits for arbitrage betting scenarios dynamically.")

# Dropdown for number of outcomes
st.markdown("### Input Parameters")
num_outcomes = st.selectbox(
    "Select number of outcomes:", ["2way", "3way", "4way", "5way", "6way", "7way", "8way", "9way", "10way"], index=0
)
num_outcomes = int(num_outcomes.replace("way", ""))

# Input Fields
with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        kaizen_odds = st.number_input("Kaizen Odds", min_value=1.01, value=2.5, step=0.01)
    with col2:
        competition_odds_1 = st.number_input("Competition 1 Odds", min_value=1.01, value=2.0, step=0.01)

# Dynamic Input for Odds
odds = [kaizen_odds, competition_odds_1]
if num_outcomes > 2:
    for i in range(2, num_outcomes):
        odds.append(
            st.number_input(f"Competition {i} Odds", min_value=1.01, step=0.01, value=1.01, key=f"odds_{i}")
        )

# Input for total stake
total_stake = st.number_input("Total Stake (€)", min_value=0.0, step=0.01, value=0.0)

# Ensure all odds are filled
if any(o < 1.01 for o in odds):
    st.markdown("<p style='color: red;'>Please input all odds</p>", unsafe_allow_html=True)
    results = None
else:
    # Dynamic Calculation
    if total_stake > 0:
        results = calculate_surebet(odds, total_stake=total_stake)
    else:
        results = None

# Display Results
if results:
    st.markdown("### Results")

    # Styling for Arbitrage and Profits
    arbitrage_color = "green" if results["Arbitrage %"] > 0 else "red"
    profit_colors = ["green" if p > 0 else "red" for p in results["Profits"]]

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
        </style>
        <div class="result-box">
            <h4>Calculation Results:</h4>
            <ul>
                <li>Kaizen Stakes: {results['Stakes'][0]}€</li>
                {''.join(f'<li>Competition {i} Stakes: {results["Stakes"][i]}€</li>' for i in range(1, len(results['Stakes'])))}
                <li>Total Stake: {results['Total Stake']}€</li>
                {''.join(f'<li style="color: {profit_colors[i]}">Profit Outcome {i + 1}: {results["Profits"][i]}€</li>' for i in range(len(results['Profits'])))}
                <li>Arbitrage: <span class="arbitrage">{results['Arbitrage %']}%</span></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
