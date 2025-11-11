from autogen import ConversableAgent
from utils.config import llm_config

doctor_agent = ConversableAgent(
    name="doctor",
    llm_config=llm_config,
    system_message="You are a licensed medical doctor. Provide final clinical guidance based on the patient's symptoms and prior agent input. Escalate when necessary."
)