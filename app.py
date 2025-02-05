from auth import login_page
import streamlit as st
from summary import summary_page


def initialize_session_state():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "current_view" not in st.session_state and not st.session_state.authenticated:
        st.session_state.current_view = "login"


initialize_session_state()

if __name__ == "__main__":
    if st.session_state.current_view == "login":
        login_page()
    elif st.session_state.current_view == "summary":
        summary_page()
