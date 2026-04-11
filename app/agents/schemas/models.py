from typing import List, Literal
from pydantic import BaseModel

class Fact(BaseModel):
    claim: str
    category: Literal['date','statistic','person','event']
    original_quote: str

class FactExtraction(BaseModel):
    facts: List[Fact]