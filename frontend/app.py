import streamlit as st
import requests
import os

# NEW: Use an environment variable for the backend URL.
# Fallback to localhost if not set.
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/chat/")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Chatbot")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.spinner("Generating response..."):
        try:
            response = requests.post(
                BACKEND_URL,
                json={"message": prompt}
            ).json()
            bot_response = response.get("response", "Sorry, I couldn't process that.")
        except Exception as e:
            bot_response = f"Error: {str(e)}"
    
    # Display and store bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
