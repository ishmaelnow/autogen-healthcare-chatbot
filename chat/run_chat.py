from agents.patient import patient_agent
from chat.groupchat import manager

def run_consultation():
    print("\n@ Welcome to the AI Healthcare Consultation System!")
    symptoms = input("Please describe your symptoms: ")

    print("\nDiagnosing symptoms ...")

    try:
        response = patient_agent.initiate_chat(
            manager,
            message=f"I am feeling {symptoms}. Can you help?"
        )
        print("\n--- Consultation Result ---")
        print(response)
    except Exception as e:
        print("\n❌ Error during consultation:")
        print(type(e).__name__, "-", str(e))