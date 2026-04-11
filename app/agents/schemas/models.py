from typing import List, Literal
from pydantic import BaseModel

class Fact(BaseModel):
    claim: str
    category: Literal['date','statistic','person','event']
    original_quote: str

class FactExtraction(BaseModel):
    facts: List[Fact]

class FactAnalysis(BaseModel):
    claim: str
    verdict: Literal['True','False','Unverified','Partially True']
    explanation: str