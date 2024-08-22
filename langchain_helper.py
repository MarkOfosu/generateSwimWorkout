# langchain_helper.py

from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional
from langchain_core.prompts import ChatPromptTemplate
from system_training_data import system_training_data
import json

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the ChatOpenAI LLM
llm = ChatOpenAI(model="gpt-4", api_key=api_key)

# Define the SwimWorkout Pydantic model
class SwimWorkout(BaseModel):
    """A swim workout."""
    focus: Optional[str] = Field(description="Focus of the workout")
    warmup: List[str] = Field(description="Warm-up set")
    preset: List[str] = Field(description="Preset set")
    main_set: List[str] = Field(description="Main set")
    cooldown: List[str] = Field(description="Cool-down set")
    distance: Optional[str] = Field(description="What is the total distance of the workout")
    duration: Optional[str] = Field(description="What is the total estimated duration of the workout")
    intensity: Optional[str] = Field(description="Intensity level of the workout")
    description: Optional[str] = Field(description="Describe the workout")

# Use the .with_structured_output() method to configure the LLM
structured_llm = llm.with_structured_output(SwimWorkout)

# Create a ChatPromptTemplate using a list of tuples to define the messages
prompt = ChatPromptTemplate.from_messages([
    ("system", system_training_data),
    ("human", "{input}")
])

# Chain the prompt with the structured LLM
few_shot_structured_llm = prompt | structured_llm

def generate_swim_workout(input_text: str):
    input_prompt = {"input": input_text}
    response = few_shot_structured_llm.invoke(input_prompt)
    try:
        response_json = json.loads(response.json())
    except json.JSONDecodeError:
        response_json = {"error": "Invalid response format", "response": response}
    return response_json
