import streamlit as st

# Title of the app
st.title("AI-Powered UI Test")

# Text section with a brief description
st.write("""
    This is a simple Streamlit app to test the AI-powered UI generated.
    Feel free to interact with the elements below!
""")

# Adding a header
st.header("Interactive UI")

# Creating a button that changes text when clicked
if st.button('Click Me'):
    st.write("Button clicked! 🎉")

# Creating a text input box
name = st.text_input("Enter your name:")

# Display text based on input
if name:
    st.write(f"Hello, {name}! 👋")

# Create a slider for user interaction
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You are {age} years old.")

# Add an image (optional: you can upload an image or add your UI components here)
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.svg", width=200)

# Display a simple chart (optional)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate some sample data
data = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})

# Plotting the chart
st.line_chart(data)

# Footer
st.write("Thanks for testing the app! 🎉")
