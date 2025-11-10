# utils/config.py

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key securely
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with the key
client = OpenAI(api_key=api_key)

# LLM config used by all agents
llm_config = {
    "config_list": [
        {"model": "gpt-4", "api_key": api_key}
    ]
}

# ✅ Optional: Confirm config loaded without exposing sensitive data
# This is safe for debugging — it masks the API key
safe_config = {
    "config_list": [
        {
            "model": model_name,
            "api_key": "****MASKED****"
        }
    ]
}
print("llm_config loaded:", safe_config)

# ✅ Now llm_config is ready to be imported and used by agents
