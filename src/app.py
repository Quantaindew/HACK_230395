from uagents import Bureau, Agent, Protocol, Context,Model
from uagents.setup import fund_agent_if_low
from messages import Cab, CabSelection,CabDetails
from agents.Calender.calender import BookEventRequest,BookEventResponse
from messages.general import InputPrompt, Response
from openaiclient import open_ai_client
import json
import agents.Calender.calenderFunctions.calender as c

agent = Agent('core', seed="core's seceret seed")


fund_agent_if_low(agent.wallet.address())

locations = {}


async def handle_query_request(ctx: Context, sender: str, msg: BookEventRequest):
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")
    title = msg.title
    location = msg.location
    start_date_time = msg.start_date_time
    end_date_time = msg.end_date_time
    response = c.create_event(start_date_time, end_date_time, title, location)
    await ctx.send("agent1qwjceuqy2vufna56gh63sk45mu3uds37wy5mquxr7gvlxkusr4trgvn6qku",BookEventResponse(success=response))


@agent.on_message(model=CabDetails)
async def receive_cab_details(ctx: Context, sender: str, msg: CabDetails):
    ctx.logger.info(f"Received message from {sender} in core, session: {ctx.session}")
    ctx.logger.info(f"{msg}")
    # await ctx.send("agent1qttrpd7ngt8q4pf2htrf52ms5jqtslmch3cv4h5u9g8z8kyh4ddh6ned3q9", BookEventRequest(title="Cab booked", location="XYZ", start_date_time="2023-12-28T09:13:00+05:30",end_date_time="2023-12-28T10:14:00+05:30"))
    title = "XYZ"
    location = "XYZ"
    start_date_time = "2023-12-28T09:13:00+05:30"
    end_date_time = "2023-12-28T10:14:00+05:30"
    response = c.create_event(start_date_time, end_date_time, title, location)
    ctx.logger.info("sent message to calender")

open_ai_req = InputPrompt(travelQuery="I am new to Mumbai, suggest me a travel plan this weekend")

@open_ai_client.on_event("startup")
async def say_hello(ctx:Context):
    ctx.logger.info(f"Hello from OpenAI Client! {ctx.name}")
    await ctx.send("agent1qw28qf58k3w0uaap5cwg0el75rr65j55qcfkace4hx4ltdpsctkkz8qtvv2", open_ai_req)

@open_ai_client.on_message(model=Response)
async def respond_to_prompt(ctx:Context, sender: str, msg: Response):
    ctx.logger.info(f"Received response from {sender}: {msg}")
    
    ctx.logger.info(f"Generated output: {msg.output}")
    locations = json.loads(msg.output)
    ctx.storage.set("locations",locations)
    ctx.logger.info(f"Locations: {locations}")

if __name__ == "__main__":
    bureau = Bureau(endpoint=["http://127.0.0.1:8005/submit"], port=8005)
    print(f"Adding core agent to Bureau: {agent.address}")
    bureau.add(agent)
    print(f"Adding openai client agent to Bureau: {open_ai_client.address}")
    bureau.add(open_ai_client)
    bureau.run()