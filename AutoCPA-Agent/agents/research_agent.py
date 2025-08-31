import time

class ResearchAgent:
    def __init__(self):
        print("Initializing Research Agent...")

    def run(self, duration_minutes=60):
        print(f"[{time.strftime('%H:%M:%S')}] Research Agent: Starting task. Duration: {duration_minutes} minutes.")
        # Simulate work
        time.sleep(2) # Using a short sleep for simulation
        print(f"[{time.strftime('%H:%M:%S')}] Research Agent: Task complete. Found 3 new opportunities.")
        return {"status": "complete", "opportunities_found": 3}
