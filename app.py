import streamlit as st

st.title("AI Chatbot")

user_input = st.text_input("Ask something")

if user_input:
    if "hello" in user_input.lower():
        st.write("Hi!")
    elif "how are you" in user_input.lower():
        st.write("I am fine!")
    elif "bye" in user_input.lower():
        st.write("Goodbye!")
    else:
        st.write("Sorry, I don't understand.")
