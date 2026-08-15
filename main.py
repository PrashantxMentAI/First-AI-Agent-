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


# i have added a the output of this agent which shows the step by step execution of the agent and the tools used to get the final answer.

# user: What is 42 + 58?
__________________________________________________
# agent: {'messages': [HumanMessage(content='What is 42 + 58?', additional_kwargs={}, response_metadata={}, id='72021176-fb06-4308-8ebb-292598276afb'), AIMessage(content=[], additional_kwargs={'function_call': {'name': 'add_numbers', 'arguments': '{"a": 42, "b": 58}'}, '__gemini_function_call_thought_signatures__': {'call_919148': 'EoUCCoICARFNMg8g2QSx+5FsfOD5tNwQamx4E9wZ96E3Du/3FawIU9JSKle3ck9KBuG+tOwtZYfTZxdmWR+5yYzi04nS8GlcgOOcpNtbstd72Bql51BanUBzrYejZF2C36WkGAH6mOTavOvEW05hFhbMK09GrhTJS1N+NohqRu5KbJKbc/k/CVlbM3w8jUeYKxU51UzYl2EQesi3NRJGw1fC5R1a+CzPXrCXNRnV9e4kvdLMZDZYwbOBKYMBlDfhZegbs11eu0TttkcEz2ux8kTEb1cZNkT4leXDNkxj3G+cob+NHYQVEMuZ8Sc3turAz1wOX8Dn9WH36Y150smE3cabOIrPWtla'}}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-3.6-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--01a004ea-a363-7822-842b-194e7d8255ea-0', tool_calls=[{'name': 'add_numbers', 'args': {'a': 42, 'b': 58}, 'id': 'call_919148', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 364, 'output_tokens': 79, 'total_tokens': 443, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 59}}), ToolMessage(content='100.0', name='add_numbers', id='f850c7e4-d479-4e6a-bdc2-b97543929a57', tool_call_id='call_919148'), AIMessage(content=[{'type': 'text', 'text': '42 + 58 = 100', 'extras': {'signature': 'Ep0BCpoBARFNMg8bNTvtN24VcdXf6h8ski8ulUujVJs3QGAH0TLJO9Dc9a16sWyt3VUaVUcC5qkcbAhJ51DM7FromjLkKp8Wxy2cc3AGcuYbiRi8E+URThcOmgKXmK6/pFpWdw1wP/QOf6oRZL+5Wf+26l/2KutJ5BR6x5T0Yho+V+M0c2AW3Nq2vjf4xklZq3mPwRoIRUUjI3rYMU6Yig=='}}], additional_kwargs={}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-3.6-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--01a004eb-01ad-7570-938c-3875cf9b68c6-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 457, 'output_tokens': 27, 'total_tokens': 484, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 16}})]}

#  user: What is 15 multiplied by 8, then divided by 3?
__________________________________________________
# agent: {'messages': [HumanMessage(content='What is 15 multiplied by 8, then divided by 3?', additional_kwargs={}, response_metadata={}, id='fce06208-cc97-4e09-928d-1f9181e65d77'), AIMessage(content=[], additional_kwargs={'function_call': {'name': 'multiply_numbers', 'arguments': '{"b": 8, "a": 15}'}, '__gemini_function_call_thought_signatures__': {'call_733323': 'EvsBCvgBARFNMg+c9K9WIvgAHeVOyFPNYhACCcio9Gght9lP/VbhSkPVdIGOoxOOcYXcNhdP0RRqsjGGAQpF32hrSKf3NR43sJaWFOg17fZkxnZyplCeySTlm+40bs2NKvM/uu7qbDgWfYFDQWyr1G04nroXv73H/RbDB0g6gYTN1dz5tQraLvPi/KkT5t5EkwFcZWJ+Jvhg+2fE0COkVrKztJ7YVCif/qFHx9ludtcUHK2goNHy2hcwxgDIsniF2Ho/rjSppQ6jlfUlm8dxUkdcq+oUo4LGIYdRiIkl/cr1w+iWXkRHXTt+fOdCF8xyCWbIbBpSmy3aw2bravA='}}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-3.6-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--01a004eb-0f62-7bb3-a2c9-ce29f3fd6706-0', tool_calls=[{'name': 'multiply_numbers', 'args': {'b': 8, 'a': 15}, 'id': 'call_733323', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 370, 'output_tokens': 74, 'total_tokens': 444, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 55}}), ToolMessage(content='120.0', name='multiply_numbers', id='2bcfa590-3058-46d2-931f-84859f443377', tool_call_id='call_733323'), AIMessage(content=[], additional_kwargs={'function_call': {'name': 'divide_numbers', 'arguments': '{"a": 120, "b": 3}'}, '__gemini_function_call_thought_signatures__': {'call_924832': 'Ep8BCpwBARFNMg91cJz/vEE429V+d0PbO685wElZV+xCBH8zBXTgyW95How4m9AZxZWkf4ZA5GLNoEkJ2n/YOf5owajE3CXY4AXQLS7TzZOAiZSyFVIVCq7DDnYmme67p558iQEt54WyVqkPmMNlPimGsO+xm03zkA848giotorwfEIsbVNhUPruNBMGXpnxf3pxqoCTo14wAWjHNEs3kUgO'}}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-3.6-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--01a004eb-1c05-7141-bbc8-08dfc0f78d26-0', tool_calls=[{'name': 'divide_numbers', 'args': {'a': 120, 'b': 3}, 'id': 'call_924832', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 458, 'output_tokens': 46, 'total_tokens': 504, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 26}}), ToolMessage(content='40.0', name='divide_numbers', id='1e40112d-b330-4b0e-89b8-7f6298a21fc4', tool_call_id='call_924832'), AIMessage(content=[{'type': 'text', 'text': '15 multiplied by 8 is **120**, and then divided by 3 is **40**.', 'extras': {'signature': 'ErYBCrMBARFNMg9+dqRMWgVYScS9oDN8D7RBr4+p/Sm7ECTaZIGX24qzYc7cAv1F9c641FQjfoAGLrhG3geQLl1+puWYrW+mQ7EFCXpfDDsMcMInYP0orbzxbyHAQHVE1SjpXwNWWcvwDCBLyUVtXhKgV93n2s1U22ZwbalawyyjisLW9HUreC/bCaXmprjdYaaaA95hequh6ahaTgz0RtzuxtBmV9hFdUmRsLXk+pOGMUAh3bbbCJE='}}], additional_kwargs={}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-3.6-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--01a004eb-264b-71c2-8cfd-4eb16a5fb2b3-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 517, 'output_tokens': 41, 'total_tokens': 558, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 18}})]}

#  user: I have a rectangle with width 12 and height 7. What is its area, and what is the square root of that area?
__________________________________________________
# agent: {'messages': [HumanMessage(content='I have a rectangle with width 12 and height 7. What is its area, and what is the square root of that area?', additional_kwargs={}, response_metadata={}, id='7a5a6d82-d526-47a9-8fda-eb2fe6a11805'), AIMessage(content=[], additional_kwargs={'function_call': {'name': 'multiply_numbers', 'arguments': '{"a": 12, "b": 7}'}, '__gemini_function_call_thought_signatures__': {'call_908554': 'EvwCCvkCARFNMg+lwk2OyH2fKG+HZwmYk7N9QEcWBlChRldWJ6yvAsiCHjJuLqHFFYH5W8gFT0hmJQoKp/FUflXxgZizHrDEMBzKNmILzKmJZ0Ie5BFboI+kd2PYN/P7f/oTLYZMWhTq/FSBjp8k6PSsK2DXRI8TeHHlMyf1pgDZdaRGAOtwQ7MAIxqD4Zp/hPOPFWhdHfnWt5c9o10F7WFuJGO3SHD6FMCY6dbpqX1mow92zZTtB1MZKanNWeynqaqnzNHJC1zGZMMuZfwafVRWIyqo5iNVlnWbgr4gibIkLfYzF9OWMc6yPnjFWItZpQG5h2uKdeGpzfpWgfa0NuoOcZtUnWXHVfK9fgZ/zee+DoCcIgdvSdjj1qt7kBZJsGPptk7cRmYQeipNsKGehOrKBhm7dBh9jilAdHUIl9vf8u3BH7oU0vTfLswPq8clZEywHxtVm+lshjl+svJVLxG8rfBKk/C2j1n2Hnmj9Hfn+DSIBJJpbPBCP1/KBoo='}}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-3.6-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--01a004eb-571b-79d0-bead-ae54d85ccfdd-0', tool_calls=[{'name': 'multiply_numbers', 'args': {'a': 12, 'b': 7}, 'id': 'call_908554', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 383, 'output_tokens': 111, 'total_tokens': 494, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 92}}), ToolMessage(content='84.0', name='multiply_numbers', id='51160d48-b3e6-43f2-96fe-8f02f0d49f4d', tool_call_id='call_908554'), AIMessage(content=[], additional_kwargs={'function_call': {'name': 'square_root', 'arguments': '{"a": 84}'}, '__gemini_function_call_thought_signatures__': {'call_999873': 'EtMBCtABARFNMg+edCLoUSyVbs3L67FjDkFAIuZbgqn3jbu4IWx3ZRvxxgq0BquVzG4RdKvxzL1FlYK9/BqVqy7AQktBdnc6jhK5FNAl0uJVB61ZaeZ6KNhCy6d8714UA7KsdfLfm3bnLrqZIDKlhC46KZQtsMftr//vcTorVcb0Db9u8SkUGc4SWdJIcI2nWgsyuWOIrpW3AnITINXhmqX3TCBfuMeZQQ5mzxl+AHvdE14PcokJOIRLYPRIztmCKlshWxL+O5K/1xpo41a7M2tLipH+lg=='}}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-3.6-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--01a004eb-bded-7c43-8b71-85c6b5531eae-0', tool_calls=[{'name': 'square_root', 'args': {'a': 84}, 'id': 'call_999873', 'type': 'tool_call'}], invalid_tool_calls=[], usage_metadata={'input_tokens': 507, 'output_tokens': 54, 'total_tokens': 561, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 39}}), ToolMessage(content='9.16515138991168', name='square_root', id='0ec7c4fe-adc8-4246-8b2d-cca11ec0ee8c', tool_call_id='call_999873'), AIMessage(content=[{'type': 'text', 'text': 'The area of the rectangle is **84** ($12 \\times 7 = 84$).\n\nThe square root of that area is approximately **9.165** ($\\sqrt{84} \\approx 9.16515$).', 'extras': {'signature': 'Eo4CCosCARFNMg/+UTL3j7cHss49hp6Z5tYNiR3v2bsR7YiC84GkAzMWPov7BH6noxYlkjDCdNOkUP7oMLCGRKiMVlN6CkyndTTFSTRQkVcyyvBdqKuYWiorLk8U4Dih5RhtvPVGR0bAbAOtLAU9tkCncc64l2lKd2qQrdn24tUfXIw/y7FSAGwJDLmZW5wKowtd19joxxmPTEc1AWS0Rthjch6lQB5GGflL6knUhhi6Oeu+NfvLA72PyxUKnCuU3VFE1uOaQ5C/jR+ntfttRUsnpE8Uj1bkZOxmI01G3eGaxvCOfliF5tmitzxNz7Q6JWUvnqWy5RFl6KUSkKUhOPnGYdLSf3J08ppigvrUp5YF'}}], additional_kwargs={}, response_metadata={'finish_reason': 'STOP', 'model_name': 'gemini-3.6-flash', 'safety_ratings': [], 'model_provider': 'google_genai'}, id='lc_run--01a004eb-c62b-7d32-a1a8-5c77d77fdf6c-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 588, 'output_tokens': 115, 'total_tokens': 703, 'input_token_details': {'cache_read': 0}, 'output_token_details': {'reasoning': 60}})]}