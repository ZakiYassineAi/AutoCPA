import sys
import os

# Add the project root to the Python path to allow for absolute imports
# This makes the script runnable from the repository root.
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from agents.master_controller import MasterController

def main():
    """
    Main entry point for the AutoCPA-Agent system.
    Initializes and runs the Master Controller.
    """
    print("--- AutoCPA-Agent System Initializing ---")

    # Create an instance of the Master Controller
    master_controller = MasterController()

    # Start the daily workflow simulation
    # The simulation runs a 24-hour cycle in 24 seconds by default.
    master_controller.run_simulation()

    print("\n--- AutoCPA-Agent System Shutdown ---")

if __name__ == "__main__":
    main()
