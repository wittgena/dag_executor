import os
import openai
from dotenv import load_dotenv

load_dotenv()

def set_api_key(api_key=None):
    openai.api_key = api_key or os.getenv("OPENAI_API_KEY")