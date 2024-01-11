# For loading the environment variable
from dotenv import load_dotenv

import os
import streamlit as st
import google.generativeai as genai

# API key is already generated from the below website and pasted in .env file as GOOGLE_API_KEY = "API Key"
# https://makersuite.google.com/app/apikey

# Loading all the environment variables
load_dotenv()

# Configuring the genai with the API Key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Setting the Model
# We have two model gemini-pro(Optimized for text) and gemini-vision-pro (Optimized for text and images)
# Initializing the chat:
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Creating a function which takes the user input and returns the response
def get_response(input):
   response = chat.send_message(input,stream=True) # stream=True - To get the responses in chunk instead of waiting for whole response from Gemini
   return response

# Initialize our streamlit app
st.set_page_config(page_title="ChitChat")
st.header("What's on your mind?")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

st.sidebar.title("Chat History")

input=st.text_input("",key="input")
submit=st.button("Ask ChitChat!")

# if submit button is clicked and input value is present
if submit and input:
   #  Calling the get_response method and send the input text
    response=get_response(input)

    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))

    st.subheader("You")
    st.write(input)

    st.subheader("ChitChat")
   # Getting the responses in chunk instead of waiting for whole response from Gemini  
    for chunk in response:
        st.write(chunk.text)
    
    st.session_state['chat_history'].append(("Bot", response.text))
   

# # st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    # Limit display to a maximum of 100 words with an ellipsis for longer messages
    truncated_text = text[:30] + ('...' if len(text) > 100 else '')
    st.sidebar.text(f"{role}: {truncated_text}")
