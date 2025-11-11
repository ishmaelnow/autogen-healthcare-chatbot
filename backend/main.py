from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import patient agent and groupchat manager
from agents.patient import patient_agent
from chat.groupchat import manager

# Optional: import chat history if you want to expose it later

app = FastAPI()

# Enable CORS for frontend access from localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ✅ React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request schema for symptom input
class SymptomRequest(BaseModel):
    symptom: str

# POST /consult — main endpoint for chatbot interaction
@app.post("/consult")
def consult(symptom_req: SymptomRequest):
    # Format message for patient agent
    message = f"I'm feeling {symptom_req.symptom}. Can you help?"

    # Initiate multi-agent chat via manager
    response = patient_agent.initiate_chat(manager, message=message)

    # Return full response to frontend
    return {"response": response}

# POST /summary — optional endpoint to extract assistant reply
@app.post("/summary")
def summary(symptom_req: SymptomRequest):
    message = f"I'm feeling {symptom_req.symptom}. Can you help?"

    # Run chat if needed (or reuse existing chat_history)
    result = patient_agent.initiate_chat(manager, message=message)

    # Extract assistant reply from patient agent
    for msg in chat_history:
        if msg.get("role") == "assistant" and msg.get("name") == "patient":
            reply = msg["content"]
            break
    else:
        reply = "No assistant reply generated"

    return {
        "summary": result,
        "reply": reply
    }

# GET / — health check endpoint
@app.get("/")
def read_root():
    return {"message": "Healthcare chatbot backend is running"}