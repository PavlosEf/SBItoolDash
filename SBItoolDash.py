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
    .css-17eq0hr {
        background-color: #333333;
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
    st.write("This is a placeholder for future tools.")
    # Placeholder for General Tab 1 content

elif page == "General Tab 2":
    st.title("General Tab 2")
    st.write("This is a placeholder for future tools.")
    # Placeholder for General Tab 2 content
st.markdown("</div>", unsafe_allow_html=True)
