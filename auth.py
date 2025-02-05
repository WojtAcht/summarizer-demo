import streamlit as st


def authenticate(username, password):
    return username == "admin" and password == "password123"


def login_page():
    st.markdown(
        """
        <style>
        /* General page styling */
        body {
            background-color: #f9fafb;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .main-title {
            color: #2c3e50;
            text-align: center;
            font-size: 42px;
            font-weight: 700;
            margin-top: 30px;
            margin-bottom: 0;
        }
        .subtitle {
            color: #7f8c8d;
            text-align: center;
            font-size: 18px;
            margin-bottom: 40px;
        }
        .block-container {
            max-width: 800px;
            margin: auto;
        }
        .summary-box {
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        label {
            font-weight: 600 !important;
        }

        /* Make Streamlit default buttons look "fancy" */
        div.stButton > button {
            background-color: #2c3e50 !important;
            color: #ffffff !important;
            border: none !important;
            padding: 0.6em 1.2em !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            cursor: pointer !important;
            transition: background-color 0.3s ease !important;
            margin: 0.3em 0 !important;
        }
        div.stButton > button:hover {
            background-color: #77a8d9 !important;
        }

        /* Specifically style the second button in our horizontal layout (Skip Adding) */
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) > div > button {
            background-color: #e74c3c !important;
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) > div > button:hover {
            background-color: #c0392b !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<h1 class='main-title'>Demo</h1>", unsafe_allow_html=True)
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.session_state.current_view = "summary"
            st.rerun()
        else:
            st.error("Invalid credentials")
