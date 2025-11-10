# chat/groupchat.py

from autogen import GroupChat, GroupChatManager
from agents.diagnosis import diagnosis_agent
from agents.pharmacy import pharmacy_agent
from agents.consultation import consultation_agent

# GroupChat: coordinates structured conversation among agents
groupchat = GroupChat(
    agents=[diagnosis_agent, pharmacy_agent, consultation_agent],
    messages=[],
    max_round=5,
    speaker_selection_method="round_robin"
)

# GroupChatManager: orchestrates message flow between agents
manager = GroupChatManager(
    name="manager",
    groupchat=groupchat
)