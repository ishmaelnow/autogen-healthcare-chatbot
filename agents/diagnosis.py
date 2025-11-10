# agents/diagnosis.py

from autogen import ConversableAgent
from utils.config import llm_config

# Diagnosis agent: analyzes symptoms and provides a concise diagnosis
diagnosis_agent = ConversableAgent(
    name="diagnosis",
    system_message="You analyze symptoms and provide a possible diagnosis. Summarize key points in one response.",
    llm_config=llm_config
)