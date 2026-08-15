# step 1 "Initialize the chat model"

from dotenv import load_dotenv

load_dotenv()


from langchain.chat_models import init_chat_model
model = init_chat_model(
    "google_genai:gemini-3.6-flash",)

# step2: define your tools 
from langchain_core.tools import tool
import math 

@tool
def add_numbers(a: float, b: float) -> float:
    """ADD two numbers together.use addition operator to add two numbers."""
    return a + b

@tool
def multiply_numbers(a: float, b: float) -> float:
    """MULTIPLY two numbers together.use multiplication operator to multiply two numbers."""
    return a * b

@tool
def divide_numbers(a: float, b: float) -> float:
    """DIVIDE two numbers together.use division operator to divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@tool
def subtract_numbers(a: float, b: float) -> float:
    """SUBTRACT two numbers together.use subtraction operator to subtract two numbers."""
    return a - b

@tool
def square_root(a: float) -> float:
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)

@tool
def power(a: float, b: float) -> float:
    """Calculate a raised to the power of b."""
    return math.pow(a, b)

tools = [
    add_numbers,
    multiply_numbers,
    divide_numbers,
    subtract_numbers,
    square_root,
    power,
]



#  step 3 : create the agent 

from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools = tools,
)

# step4 run the agent 

def run_agent(question: str):
    """run the agent and print the execution trace"""
    print(f" user: {question}")
    print("_" * 50)
    result = agent.invoke({
        "messages": [("user", question)]
    })
    
    print(f"agent: {result}")
    
    
    # Simple: single tool call
run_agent("What is 42 + 58?")

# Medium: multiple tool calls in sequence
run_agent("What is 15 multiplied by 8, then divided by 3?")

# Complex: the agent must plan a multi-step approach
run_agent(
    "I have a rectangle with width 12 and height 7. "
    "What is its area, and what is the square root of that area?"
)