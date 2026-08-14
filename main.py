# step 1 "Initialize the chat model"


from langchain.chat_models import init_chat_model
model = init_chat_model("openai:gpt-4o-mini", )

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
        "message": [("user", question)]
    })
    
    print("agent: {result}")