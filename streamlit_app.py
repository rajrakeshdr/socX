import streamlit as st
import random

# Dummy AI function (replace with an actual AI-powered API call like OpenAI GPT)
def get_ai_response(query):
    # Example responses to simulate AI-generated results
    responses = [
        "AI is a branch of computer science that deals with the simulation of intelligent behavior in machines.",
        "Machine learning is a subset of AI that uses statistical methods to allow machines to improve with experience.",
        "AI is transforming industries from healthcare to finance, with applications such as predictive analytics, automation, and smart assistants."
    ]
    return random.choice(responses)

# Streamlit layout and styling
st.set_page_config(page_title="AI-Powered Search", page_icon=":mag_right:", layout="centered")

# Inject custom CSS for styling
st.markdown("""
    <style>
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #f9f9f9;
        color: #333;
        margin: 0;
        padding: 0;
    }

    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 40px;
        text-align: center;
    }

    header {
        margin-bottom: 40px;
    }

    header h1 {
        font-size: 3rem;
        color: #1A202C;
        font-weight: 700;
        margin: 0;
    }

    header p {
        color: #4A5568;
        font-size: 1.2rem;
        margin-top: 10px;
    }

    .stTextInput>div>div>input {
        width: 50%;
        padding: 15px;
        font-size: 18px;
        border: 2px solid #E2E8F0;
        border-radius: 25px;
        outline: none;
        transition: all 0.3s ease;
    }

    .stTextInput>div>div>input:focus {
        border-color: #48BB78;
    }

    .stButton>button {
        padding: 15px 25px;
        font-size: 18px;
        background-color: #48BB78;
        color: white;
        border: none;
        border-radius: 25px;
        cursor: pointer;
    }

    .stButton>button:hover {
        background-color: #38A169;
    }

    .results {
        margin-top: 40px;
        display: none;
        padding: 20px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    footer {
        margin-top: 50px;
        font-size: 14px;
        color: #888;
    }

    footer a {
        color: #48BB78;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Page header
st.title("AI-Powered Search")
st.markdown("#### Get relevant answers from the web using AI.")

# Input search query with a unique key
query = st.text_input("Ask a question...", "", key="search_input")

# Display search button and handle input with a unique key
search_button = st.button("Search", key="search_button")

if search_button and query:
    # Simulate AI response (replace with a real AI API)
    response = get_ai_response(query)

    # Display the response
    st.markdown("### AI Response")
    st.write(response)
elif search_button and not query:
    st.warning("Please enter a query to search!")

# Footer (optional)
st.markdown("---")
st.markdown(
    "Made with ❤️ | [Privacy Policy](#)"
)
