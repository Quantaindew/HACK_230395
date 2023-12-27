from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
from messages.general import InputPrompt, Response
from dotenv import load_dotenv
import os

load_dotenv()

OPEN_AI_SEED = os.getenv("OPEN_AI_SEED", "I really don't know what the heck I'm doing :0")

OpenAIAgent = Agent(
    name="OpenAI",
    seed=OPEN_AI_SEED
)

fund_agent_if_low(OpenAIAgent.wallet.address())

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="""
    Travel Plan Prompt:
    {{
    "request": "You are a expert of travel plans and can provide best travel plans to user wishes.\n
    A user has put his query as {travelQuery}.Include details such as the place name, location, start date time, and end datetime for each destination only",
    "output_format": "JSON",
    "json_format": true
    }}
    Sample travelQuery = "I am new to mumbai, suggest me a travel plan this weekend"
    Sample output:
    {{
     "travel_plan": [
    {{
      "place_name": "Gateway of India",
      "location": "Apollo Bandar, Colaba, Mumbai, Maharashtra 400001, India",
      "start_time": "2023-12-30T09:00:00+05:30",
      "end_time": "2023-12-30T11:00:00+05:30"
    }},
    {{
      "place_name": "Juhu Beach",
      "location": "Juhu, Mumbai, Maharashtra, India",
      "start_time": "2023-12-30T13:00:00+05:30",
      "end_time": "2023-12-30T15:00:00+05:30"
    }}
    ]
    }}
    """,
    input_variables=["travelQuery"],
)
modelName = "gpt-3.5-turbo"
llm = ChatOpenAI(temperature=0.1, openai_api_key=os.getenv("OPENAI_API_KEY"), model_name=modelName)
op = StrOutputParser()
chain = prompt|llm|op

@OpenAIAgent.on_event("startup")
async def say_hello(ctx:Context):
    ctx.logger.info(f"Hello from OpenAI! {ctx.name}")

open_ai_protocol = Protocol("OpenAI")


@open_ai_protocol.on_message(model=InputPrompt, replies=Response)
async def respond_to_prompt(ctx:Context, sender: str, msg: InputPrompt):
    ctx.logger.info(f"Received prompt from {sender}: {msg}")
    # additional_specifications = f"Try to include these words in your poem: {msg.additional_specifications}.\n" if msg.additional_specifications else ""
    # _input = prompt.format(travelQuery=msg.travelQuery, theme=msg.theme, format_instructions=additional_specifications)
    try:
        ctx.logger.info(f"Generated output: {msg}")
        output = chain.invoke({"travelQuery":msg.travelQuery})
        # output = "Hello"
        ctx.logger.info(f"Generated output: {output}")
        await ctx.send(
            sender,
            Response(output=output)
        )

    except Exception as e:
        ctx.logger.error(f"Error generating text: {e}")
        await ctx.send(sender, Response(output="I'm sorry, I couldn't generate a poem for you. Please try again."))
        raise e
    
OpenAIAgent.include(open_ai_protocol)


 
