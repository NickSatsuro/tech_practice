import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Объект LLM
def get_llm():
    return ChatOpenAI(
        model=os.getenv("LLM", ""),         
        openai_api_key=os.getenv("API_KEY", ""), 
        openai_api_base=os.getenv("API_URL", ""),  
        temperature=0.2,                           
    )
