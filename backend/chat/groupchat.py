# chat/groupchat.py

from autogen import GroupChat, GroupChatManager
from agents.patient import patient_agent
from agents.diagnosis import diagnosis_agent
from agents.pharmacy import pharmacy_agent
from agents.consultation import consultation_agent
from agents.doctor import doctor_agent  # ✅ new import

# GroupChat: coordinates structured conversation among agents
groupchat = GroupChat(
    agents=[
        patient_agent,
        consultation_agent,
        diagnosis_agent,
        pharmacy_agent,
        doctor_agent  # ✅ should be last
    ],
    messages=[],
    max_round=5,
    speaker_selection_method="round_robin"
)



# GroupChatManager: orchestrates message flow between agents
manager = GroupChatManager(
    name="manager",
    groupchat=groupchat
)



