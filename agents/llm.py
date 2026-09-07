from langchain_ollama import ChatOllama
from agents.tools import search, calculator, get_weather


llm = ChatOllama(model='llama3.1')

tools = [search, calculator, get_weather]

llm_with_tools = llm.bind_tools(tools)