from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
from messages import Cab, UAgentResponse, UAgentResponseType,CabSelection
import requests
import os
import uuid
from agents.cab_booking.cabs.cab_protocol import cab_protocol

CAB_DRIVER_SEED = os.environ.get('CAB_DRIVER_SEED 1', 'No one can guess me 2 :)')
is_available = False
# uber developers
agent1 = Agent('cab_booking 1', seed=CAB_DRIVER_SEED)

def faretimeCalc(Travel_distance,User_Distance):
    fare = 0.45*Travel_distance
    time =  40*User_Distance
    return fare,time 

fund_agent_if_low(agent1.wallet.address())

@agent1.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Cab Agent Started")
    ctx.storage.set("is_available",False)


@cab_protocol.on_message(model=Cab)
async def send_state(ctx: Context, sender: str, msg: Cab):
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")
    fare,time = faretimeCalc(msg.distance_for_travel,msg.distance_from_source)
    await ctx.send(sender,CabSelection(Name=agent1.address,is_available=ctx.storage.get("is_available"),fare=fare,arrival_time=time))

agent1.include(cab_protocol)
