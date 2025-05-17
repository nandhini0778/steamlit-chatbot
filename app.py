import streamlit as st
import os
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Set the title of the Streamlit app
st.title("Simple Chatbot with Gemini")

# Initialize chat history in Streamlit's session state if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = SystemMessage(content="You are a helpful assistant.")

# Initialize the ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Display existing chat messages
for message in st.session_state["chat_history"]:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Get user input
user_input = st.chat_input("You:")

if user_input:
    # Add user message to chat history
    st.session_state["chat_history"].append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    result = llm.invoke(st.session_state["chat_history"])

    # Add AI response to chat history
    st.session_state["chat_history"].append(AIMessage(content=result.content))
    with st.chat_message("assistant"):
        st.markdown(result.content)

    # Optional: Clear the input field after sending the message
    st.session_state["chat_input"] = ""
