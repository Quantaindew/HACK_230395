from uagents import Agent, Protocol, Context
from uagents.setup import fund_agent_if_low
from messages import Cab, UAgentResponse, UAgentResponseType,CabSelection
from agents.cab_booking.cabs.cab_protocol import cab_protocol
import os

CAB_MAIN_SEED = os.environ.get('CAB_MAIN_SEED', 'No one can guess me main :)')

agent = Agent('cab_booking', seed=CAB_MAIN_SEED)

fund_agent_if_low(agent.wallet.address())


@cab_protocol.on_message(model=Cab)
async def send_state(ctx: Context, sender: str, msg: Cab):
    ctx.logger.info(f"Received message from {sender} in cab_main, session: {ctx.session}")
    await ctx.experimental_broadcast(cab_protocol.digest, msg)

agent.include(cab_protocol)


