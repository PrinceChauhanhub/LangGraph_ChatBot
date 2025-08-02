# LangGraph ChatBot 🤖

This project is a simple **Chatbot UI using Streamlit** that keeps track of chat history across user interactions using **Streamlit's session state**. It mimics a chat-like interface where both user and assistant messages are displayed sequentially, providing a base framework to integrate with any LLM (Large Language Model) API like OpenAI, Gemini, Ollama, etc.

## 🚀 Features
- Clean Chat Interface using Streamlit's `st.chat_message()`
- Persistent chat history using `st.session_state`
- Dynamic message rendering on each user input
- Simple and lightweight code structure
- Ready to be connected with an AI model backend (API call integration)

## 🛠️ Technologies Used
- Python 3.11
- Streamlit

## 🔧 How to Run
1. Clone the repository:
```
    git clone https://github.com/PrinceChauhanhub/LangGraph_ChatBot.git
    cd LangGraph_ChatBot 
```
2. Install the required packages:
```    pip install requirements.txt
```
3. Setup the Google gemini key:
```    
    Create a file .env 
    Put your Google Gemini API Key as : GOOGLE_API_KEY = <Your key>
```
4. Run the Streamlit App:
```    
    streamlit run streamlit_frontent.py
```
5. Open your browser and start chatting!

## 📝 How it Works
- Maintains a `message_history` list inside Streamlit's `session_state` to persist chat history across interactions.
- On every user input, the message is appended to the history.
- The entire chat history is re-rendered after each interaction.
- The user's message is sent to **Google Gemini API** to generate AI-powered responses.
- The assistant's reply is dynamically displayed in the chat interface.
---

Happy Building! 🚀
