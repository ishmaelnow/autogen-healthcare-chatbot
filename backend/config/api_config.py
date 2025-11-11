# backend/config/api_config.py

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI key and model name
api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME", "gpt-4")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Config used by FastAPI agents
llm_config = {
    "config_list": [
        {
            "model": model_name,
            "api_key": api_key
        }
    ]
}

# Masked config for safe logging
safe_config = {
    "config_list": [
        {
            "model": model_name,
            "api_key": "****MASKED****"
        }
    ]
}

print("FastAPI llm_config loaded:", safe_config)