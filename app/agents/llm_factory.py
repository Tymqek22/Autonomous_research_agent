import os
from enum import Enum
from dotenv import load_dotenv
from langchain_openai import OpenAI
from pydantic import BaseModel
from typing import Optional, Type, Any

class ModelType(Enum):
    GPT_4O_MINI = "gpt-4o-mini"

class LLMFactory:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_KEY")

        if not self.api_key:
            raise ValueError("LLM api key not specified.")

    def get_llm(
            self,
            model: ModelType = ModelType.GPT_4O_MINI,
            temperature: float = 0,
            structured_output: Optional[Type[BaseModel]] = None
            ) -> Any:
        llm = OpenAI(
            model=model.value,
            temperature=temperature,
        )

        if structured_output:
            llm = llm.with_structured_output(structured_output)

        return llm
    
llm_factory = LLMFactory()