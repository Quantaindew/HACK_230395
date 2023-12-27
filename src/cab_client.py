from messages import Cab, UAgentResponse
from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
import os

get_cab_client = Agent(
    name="get_cab_client",
    port=8009,
    seed=os.environ.get('GET_CAB_CLIENT_SEED', 'No one can guess me :)'),
    endpoint=["http://127.0.0.1:8001/submit"],
)

fund_agent_if_low(get_cab_client.wallet.address())

cabReq = Cab(source="New York", destination="Boston", time="10:00 AM")

@get_cab_client.on_event("startup")
async def send_message(ctx: Context):
    await ctx.send("agent1qd2jvf7r3k25x03pcu8920xf7geeeuw3cheqymqejhjj4zcluq8xj9lfld2", cabReq)

@get_cab_client.on_message(model=UAgentResponse)
async def message_handler(ctx: Context, _: str, msg: UAgentResponse):
    ctx.logger.info(f"Received cab options from: {msg.options}")

if __name__ == "__main__":
    get_cab_client.run()