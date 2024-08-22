# main.py

import streamlit as st
from langchain_helper import generate_swim_workout

st.title("Swim Workout Generator")

input_text = st.text_input("Enter your workout request:", "")

if st.button("Generate Workout"):
    if input_text:
        with st.spinner("Generating workout..."):
            response = generate_swim_workout(input_text)
            st.success("Workout generated successfully!")
            st.write(response)
    else:
        st.error("Please enter a workout request.")
