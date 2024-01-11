# ChitChat: Conversational AI Chat Bot

ChitChat is a conversational AI chat bot built using the Google Generative AI API. It allows users to interact with an AI model to engage in text-based conversations. The chat bot is configured with the `gemini-pro` model, optimized for text interactions.

## Getting Started

To run the ChitChat app locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ChitChat.git
   cd ChitChat

2. **Install Dependencies::**
   ```bash
   pip install -r requirements.txt

3. **Generate API Key:**
   ```bash
   GOOGLE_API_KEY="your_api_key"

4. **Run the App:**
   ```bash
   streamlit run ChitChat.py

## Usage
Enter your message in the text input box.
Click on the "Ask ChitChat!" button to get responses from the chat bot.
The conversation history is displayed on the sidebar.

## Features
Utilizes the Google Generative AI API for conversational interactions.
Supports a streamlined chat history display.
Easy-to-use Streamlit app interface.
Feel free to explore and engage in conversations with ChitChat!

## Note
Make sure to keep your API key confidential. Do not expose it in your code or share it publicly.
The chat history is stored in the session state and persists across interactions within the same session.
