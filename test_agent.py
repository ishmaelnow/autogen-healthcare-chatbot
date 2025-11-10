from utils.config import llm_config
from autogen import ConversableAgent

agent = ConversableAgent(
    name="agent_name",
    system_message="Test agent for debugging",
    llm_config=llm_config
)

print("Agent initialized successfully.")