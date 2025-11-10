from autogen import ConversableAgent
from utils.config import llm_config

# Create a simple agent
test_agent = ConversableAgent(
    name="tester",
    system_message="You are a helpful assistant.",
    llm_config=llm_config
)

# Correct format: message must be a dict
message = {"role": "user", "content": "What are the symptoms of dehydration?"}

# Generate reply
response = test_agent.generate_reply(messages=[message])

print("\n--- LLM Response ---")
print(response)