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

/* Main app container background and fix white gap */
html, body, .stApp {
    background-color: #1E1E1E; /* Dark grey background */
    margin: 0;
    padding: 0;
    height: 100%; /* Ensure the entire height is covered */
    overflow-x: hidden; /* Prevent horizontal scrolling */
}

/* Remove padding/margin from Streamlit's main content wrapper */
.main {
    margin: 0;
    padding: 0;
    background-color: #1E1E1E; /* Match background color */
}



    
        /* Sidebar background */
        section[data-testid="stSidebar"] {
            background-color: #1E1E1E; /* Dark grey background for sidebar */
        }

        /* Tools Menu Header */
        section[data-testid="stSidebar"] h1 {
            color: #FFFFFF; /* White text for the Tools Menu header */
            font-size: 20px; /* Adjust font size if needed */
            font-weight: bold; /* Make it bold */
            text-align: center; /* Center align the header */
        }

        /* Radio buttons in the sidebar */
        section[data-testid="stSidebar"] label {
            color: #FFFFFF; /* White text for labels */
        }

        /* Adjust margin and padding if necessary */
        section[data-testid="stSidebar"] {
            padding: 20px; /* Add some padding for spacing */
        }

        /* Main background color */
        .stApp {
            background-color: #1E1E1E; /* Dark grey background for the main content */
        }

        /* Ensure all text inside the main content is white */
        .stApp * {
            color: #FFFFFF; /* White text */
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
    st.write("This is a placeholder for future tools.")
    # Placeholder for General Tab 1 content

elif page == "General Tab 2":
    st.title("General Tab 2")
    st.markdown("<div class='horizontal-bar'></div>", unsafe_allow_html=True)
    st.write("This is a placeholder for future tools.")
    # Placeholder for General Tab 2 content
