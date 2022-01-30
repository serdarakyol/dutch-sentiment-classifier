from pydantic import BaseModel
from typing import List

from pydantic.types import Json

class SentimentClassifyRequest(BaseModel):
    content: str

class SentimentClassifyResponse(BaseModel):
    content:str
    sentiment: str