from uagents import Bureau

from agents.cab_booking.cabs.cab_agent1 import agent as cab_agent1
from agents.cab_booking.cabs.cab_agent2 import agent as cab_agent2
from agents.cab_booking.cabs.cab_agent3 import agent as cab_agent3
# from agents.cab_booking.cabs.cab_main import agent  as cab_main_agent
 
if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8003/submit", port=8003)
    print(f"Adding cab agent 1 to Bureau: {cab_agent1.address}")
    bureau.add(cab_agent1)
    print(f"Adding cab agent 2 to Bureau: {cab_agent2.address}")
    bureau.add(cab_agent2)
    print(f"Adding cab agent 3 to Bureau: {cab_agent3.address}")
    bureau.add(cab_agent3)
    # print(f"Adding cab agent main to Bureau: {cab_main_agent.address}")
    # bureau.add(cab_main_agent)
    bureau.run()