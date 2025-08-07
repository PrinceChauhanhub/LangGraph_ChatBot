from langgraph.graph import StateGraph, START, END
from typing import TypedDict,  Annotated
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage

load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

class ChatState(TypedDict):
    
    messages : Annotated[list[BaseMessage], add_messages()] # using reducer

def chat_node(state : ChatState):
    
    ##take user query from state
    messages = state['messages']
    
    # send to llm 
    response = llm.invoke(messages)
    
    # response store state
    
    return {'messages': [response]}

checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer = checkpointer)
