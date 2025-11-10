# agents/consultation.py

from autogen import ConversableAgent
from utils.config import llm_config

# Consultation agent: decides if a doctor visit is needed and ends session with 'CONSULTATION_COMPLETE'
consultation_agent = ConversableAgent(
    name="consultation",
    system_message="You determine if a doctor's visit is required. Provide a final summary with clear next steps. IMPORTANT: End your response with 'CONSULTATION_COMPLETE' to signal the end of the consultation.",
    llm_config=llm_config
)