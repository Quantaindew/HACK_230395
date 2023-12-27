from uagents import Bureau
from agents.cab_booking.cabs.cab_agent1 import agent1 as cab_agent1
from agents.cab_booking.cabs.cab_agent2 import agent as cab_agent2
from agents.cab_booking.cabs.cab_agent3 import agent as cab_agent3
from agents.Calender.calender import agent as calender_agent
 
from agents.top_destinations.top_destinations import agent as top_destinations_agent

from agents.OpenAI.openai import OpenAIAgent
# from agents.cab_booking.cab_booking import agent as cab_agent
 
if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8001/submit", port=8001)
    print(f"Adding top destinations agent to Bureau: {top_destinations_agent.address}")
    bureau.add(top_destinations_agent)
    print(f"Adding cab agent 1 to Bureau: {cab_agent1.address}")
    bureau.add(cab_agent1)
    print(f"Adding cab agent 2 to Bureau: {cab_agent2.address}")
    bureau.add(cab_agent2)
    print(f"Adding cab agent 3 to Bureau: {cab_agent3.address}")
    bureau.add(cab_agent3)
    print(f"Adding Calender agent to Bureau: {calender_agent.address}")
    bureau.add(calender_agent)
    print(f"Adding OpenAI agent to Bureau: {OpenAIAgent.address}")
    bureau.add(OpenAIAgent)
    bureau.run()