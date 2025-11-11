# utils/config.py

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file in project root
load_dotenv()

# Retrieve values securely
api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME", "gpt-4")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# LLM config used by all agents
llm_config = {
    "config_list": [
        {
            "model": model_name,
            "api_key": api_key
        }
    ]
}

# Optional: Config for safe logging (no sensitive data)
safe_config = {
    "config_list": [
        {
            "model": model_name,
            "api_key": "MASKED***"
        }
    ]
}

print("Main llm_config is ready to be imported and used by agents:", safe_config)