# agents/pharmacy.py

from autogen import ConversableAgent
from utils.config import llm_config

# Pharmacy agent: recommends medications based on diagnosis. Responds only once.
pharmacy_agent = ConversableAgent(
    name="pharmacy",
    system_message="You recommend medications based on diagnosis. Only respond once.",
    llm_config=llm_config
)