# agents/patient.py

from autogen import ConversableAgent
from utils.config import llm_config

# Patient agent: captures user symptoms and initiates the conversation
patient_agent = ConversableAgent(
    name="patient",
    system_message="You describe symptoms and ask for medical help.",
    llm_config=llm_config
)