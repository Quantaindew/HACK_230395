from uagents import Model
from enum import Enum
from typing import Optional, List
from pydantic import Field
 
class UAgentResponseType(Enum):
  ERROR = "error"
  SELECT_FROM_OPTIONS = "select_from_options"
  FINAL_OPTIONS = "final_options"
 
class KeyValue(Model):
  key: str
  value: str
 
class UAgentResponse(Model):
  type: UAgentResponseType
  agent_address: Optional[str]
  message: Optional[str]
  options: Optional[List[KeyValue]]
  request_id: Optional[str]
 
class BookingRequest(Model):
  request_id: str
  user_response: str
  user_email: str
  user_full_name: str

class CabDetails(Model):
  cab_name: str
  cab_fare: int
  cab_arrival_time: int

class InputPrompt(Model):
    travelQuery: str = Field(..., description="The travel query")
    # theme: str = Field(..., description="The theme of the poem.")
    # additional_specifications: Optional[str] = Field(None, description="Additional specifications for the poem.")

class Response(Model):
    output: str = Field(..., description="The travel plan")

    