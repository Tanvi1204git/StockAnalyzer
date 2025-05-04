import streamlit as st
import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with your key directly, not recommended

# Set Streamlit page config
st.set_page_config(page_title="Chatbot", layout="centered")

# Title
st.title("🤖 Chatbot with OpenAI")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Say something...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=st.session_state.messages
        )

        reply = response.choices[0].message["content"]

        # Add bot response to history
        st.session_state.messages.append({"role": "assistant", "content": reply})

        # Display bot response
        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"Error: {str(e)}")
