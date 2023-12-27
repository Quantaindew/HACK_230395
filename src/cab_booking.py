from uagents import Agent, Context, Protocol, Bureau, Model
from uagents.setup import fund_agent_if_low
from messages import Cab, UAgentResponse, UAgentResponseType, CabSelection, CabDetails
from agents.Calender.calender import BookEventRequest,BookEventResponse
import requests
import os
import uuid
from agents.cab_booking.cabs.cab_protocol import cab_protocol
from app import locations
from utils.distCal import get_distance
import json
import agents.Calender.calenderFunctions.calender as c

CAB_BOOKING_SEED = os.environ.get('CAB_BOOKING_SEED', 'No one can guess me :)')
# uber developers
def bestBook(is_available,fare,arrival_time):
    if(is_available == False):
        prio = 0.2*fare + 0.5*arrival_time
        return prio
    else:
        return 99999
    
drivers = []

agent = Agent('cab_booking', seed=CAB_BOOKING_SEED, endpoint=["http://127.0.0.1:8002/submit"])



fund_agent_if_low(agent.wallet.address())
current_location = "Chandani Chowk"
@agent.on_event("startup")
async def startup(ctx: Context):
    with open("agent1q2ydd8druw_data.json") as f:
        global locations
        locations = json.load(f)
    ctx.logger.info(f"{locations}")
    source_location = locations["locations"]["travel_plan"][0]
    dest_location = locations["locations"]["travel_plan"][1]
    ctx.logger.info(f"Cab Agent Started {source_location['place_name']}")
    ctx.logger.info("Cab booking agent started")
    await ctx.send("agent1q0pnrp5ahn3stfyuf3s0ym5euuurl3w4ztu60af5v8qv6cndktynqrr99kc",Cab(distance_from_source=get_distance(current_location , source_location['place_name']), distance_for_travel=get_distance(source_location['place_name'],dest_location['place_name']),source=current_location,destination=dest_location['place_name']))
    await ctx.send("agent1qgg4jvaj3a3xtde3wc2gkvqwl43mflt9awnr9za6huu44x80sx7fu2mwz2q",Cab(distance_from_source=get_distance(current_location , source_location['place_name']), distance_for_travel=get_distance(source_location['place_name'],dest_location['place_name']),source=current_location,destination=dest_location['place_name']))
    await ctx.send("agent1qdax9c520nn457edq0q9meumn3ng98pra0840fdqsjpjrarm6p4qvf6ne9g",Cab(distance_from_source=get_distance(current_location , source_location['place_name']), distance_for_travel=get_distance(source_location['place_name'],dest_location['place_name']),source=current_location,destination=dest_location['place_name']))
    # await ctx.send("agent1qttrpd7ngt8q4pf2htrf52ms5jqtslmch3cv4h5u9g8z8kyh4ddh6ned3q9", BookEventRequest(title="Cab booked", location="XYZ", start_date_time="2023-12-28T09:13:00+05:30",end_date_time="2023-12-28T10:14:00+05:30"))
    
@agent.on_message(model=CabSelection)
async def cab_selection(ctx: Context, sender: str, msg: CabSelection):
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")
    ctx.logger.info(f"{msg}")
    drivers.append({"name":sender,"is_available":msg.is_available,"fare":msg.fare,"arrival_time":msg.arrival_time})
    drivers.sort(key=lambda x: bestBook(x["is_available"],x["fare"],x["arrival_time"]))
    best_detail = drivers[0]
    ctx.logger.info(f"Best cab: {best_detail}")
    await ctx.send("agent1qwjceuqy2vufna56gh63sk45mu3uds37wy5mquxr7gvlxkusr4trgvn6qku",CabDetails(cab_name=best_detail["name"],cab_fare=best_detail["fare"],cab_arrival_time=best_detail["arrival_time"]))
    ctx.logger.info(f"{locations}")
    title = f"Trip to {locations['locations']['travel_plan'][0]['place_name']} (Cab_service_Agent: {best_detail['name']})"
    description = f"Cab booked with agent address: {best_detail['name']}"
    location = current_location
    start_date_time = "2024-01-02T20:13:00+05:30"
    end_date_time = "2024-01-02T22:14:00+05:30"
    ctx.logger.info(f"{title},{description},{location},{start_date_time},{end_date_time}")
    response = c.create_event(start_date_time, end_date_time, title, location)
    ctx.logger.info("sent message to calender")



if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8002/submit",port=8002)
    print(f"Adding agent {agent.address} to bureau")
    bureau.add(agent)
    bureau.run()