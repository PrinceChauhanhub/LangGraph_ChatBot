from langgraph.graph import StateGraph, START, END
from typing import TypedDict,  Annotated
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

class ChatState(TypedDict):
    
    messages : Annotated[list[BaseMessage], add_messages()] # using reducer
    topic : list

def chat_node(state : ChatState):
    
    ##take user query from state
    messages = state['messages']
    
    # send to llm 
    response = llm.invoke(messages)
    
    # response store state
    
    return {'messages': [response]}

conn = sqlite3.connect(database="chatbot.db",check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer = checkpointer)

def retrieve_all_threads():
    all_thread = set()
    ## to extract the no. of threads
    for checkpoint in checkpointer.list(None):
        all_thread.add(checkpoint.config['configurable']['thread_id'])
    return list(all_thread)