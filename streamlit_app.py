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

# Page header
st.title("AI-Powered Search")
st.markdown("#### Get relevant answers from the web using AI.")

# Input search query
query = st.text_input("Ask a question...", "")

# Display search button and handle input
if st.button("Search") and query:
    # Simulate AI response (replace with a real AI API)
    response = get_ai_response(query)

    # Display the response
    st.markdown("### AI Response")
    st.write(response)
elif st.button("Search") and not query:
    st.warning("Please enter a query to search!")

# Footer (optional)
st.markdown("---")
st.markdown(
    "Made with ❤️ | [Privacy Policy](#)"
)
