import streamlit as st


def summary_page():
    # Add some custom CSS to style the page and buttons more elegantly
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

    # --- Page Title ---
    st.markdown("<h1 class='main-title'>Demo</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='subtitle'>A simple article summarizer</p>", unsafe_allow_html=True
    )

    # --- Text Input for Article ---
    article_content = st.text_area(label="Paste your article content here:", height=300)

    # --- Model Selection ---
    selected_model = st.selectbox(
        "Select Large Language Model:", ["GPT-4o", "O1", "Cloud Sonnet 3.5"]
    )

    if "add_clicked" not in st.session_state:
        st.session_state.add_clicked = False
    if "skip_clicked" not in st.session_state:
        st.session_state.skip_clicked = False

    if st.button("Summarize"):
        st.session_state.add_clicked = False
        st.session_state.skip_clicked = False
        st.markdown(
            """
            <div class='summary-box' style='
                background-color: #f8f9fa;
                border-left: 4px solid #2c3e50;
                border-radius: 4px;
                padding: 20px;
                margin: 20px 0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            '>
                <h3 style='
                    color: #2c3e50;
                    margin-top: 0;
                    margin-bottom: 15px;
                    font-size: 1.2em;
                '>Summary</h3>
                <p style='
                    color: #495057;
                    line-height: 1.6;
                    margin: 0;
                    font-size: 1.1em;
                '>
                    This is a mock summary for demonstration purposes.
                    Replace this text with your actual summarization logic.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # --- Add to Knowledge Base Question (via fancy buttons) ---
        col1, col2 = st.columns(2)

        def on_add_click():
            st.session_state.add_clicked = True
            st.session_state.skip_clicked = False

        def on_skip_click():
            st.session_state.skip_clicked = True
            st.session_state.add_clicked = False

        with col1:
            if st.button("Add to Knowledge Base", on_click=on_add_click):
                pass

        with col2:
            if st.button("Skip Adding", on_click=on_skip_click):
                pass

    if st.session_state.add_clicked:
        st.success("Summary added to the knowledge base (mocked).")
    if st.session_state.skip_clicked:
        st.info("Summary was not added to the knowledge base.")
