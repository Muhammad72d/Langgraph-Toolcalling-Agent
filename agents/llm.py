import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from agents.tools import search, calculator, get_weather

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    google_api_key=api_key,
    temperature=0.2,
    max_output_tokens=512
)

tools = [search, calculator, get_weather]

llm_with_tools = llm.bind_tools(tools)