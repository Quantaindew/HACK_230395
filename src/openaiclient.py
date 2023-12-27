from messages.general import InputPrompt, Response
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import os
 
OPEN_AI_SEED_CLIENT = os.getenv("OPEN_AI_SEED", "Totally Clueless ;_;")

open_ai_client = Agent(
    name="OpenAI Client",
    seed=OPEN_AI_SEED_CLIENT,
    port = 8008,
    endpoint = ["http://127.0.0.1:8008/submit"]
)

fund_agent_if_low(open_ai_client.wallet.address())


if __name__ == "__main__":
    open_ai_client.run()
