import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable' : {'thread_id': 'thread-1'}}

## st.session_State -> Dictionary
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

#loading Conersation history every time the program reruns
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])
        
user_input = st.chat_input('Type Here')

if user_input:

    ## store the human message first
    st.session_state['message_history'].append({'role':'user', 'content':user_input})
    with st.chat_message('human'):
        st.text(user_input)
    
    response = chatbot.invoke({'message':[HumanMessage(content = user_input)]}, config=CONFIG)
    ai_message = response['message'][-1].content
    
    st.session_state['message_history'].append({'role':'assistant', 'content':ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)