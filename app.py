import os
from google.colab import userdata
os.environ['GOOGLE_API_KEY']=st.secrets('GOOGLE_API_KEY')
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = []
chat_history.append(SystemMessage(content="You are a helpful assistant."))

while True:
  user_input = input("You:")
  chat_history.append(HumanMessage(content=user_input))
  if user_input == "quit":
    break
  result = llm.invoke(chat_history)
  chat_history.append(AIMessage(content=result.content))
  print("AI:",result.content)
