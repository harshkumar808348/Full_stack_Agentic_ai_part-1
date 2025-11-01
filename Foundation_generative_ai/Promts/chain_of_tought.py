# chain of tought prompting

import os
import ssl



# Force TLS 1.2 or higher
os.environ['CURL_CA_BUNDLE'] = ''

from google import genai

client = genai.Client(
    api_key = "AIzaSyCbfmGD1JvtwiOo8C7P80y6I0n3id87I7E"
    
)

import json
import time

SYSTEM_PROMPT = """You are a problem-solving assistant that breaks down solutions into clear steps.
You MUST respond with a sequence of JSON objects, one per line. Each step follows this format:
Output JSON Format:
{"step": "START" | "PLAN" | "OUTPUT", "content": "string"}
Process Flow:
1. START - Acknowledge the user's question
2. PLAN - Multiple planning steps (2-5 steps) showing your reasoning
3. OUTPUT - Final answer or solution
Rules:
- Each line must be a valid, complete JSON object
- Use multiple PLAN steps to show your thought process
- End with exactly ONE OUTPUT step containing the final answer
- Keep content concise and clear
Example 1 - Math Problem:
User: "Hey, can you solve 2+3*5/10"
Response:
{"step": "START", "content": "I'll solve the math problem 2+3*5/10 for you"}
{"step": "PLAN", "content": "This is an arithmetic expression that requires order of operations"}
{"step": "PLAN", "content": "Using BODMAS/PEMDAS: Multiplication and Division come before Addition"}
{"step": "PLAN", "content": "First: 3*5 = 15, then 15/10 = 1.5"}
{"step": "PLAN", "content": "Finally: 2 + 1.5 = 3.5"}
{"step": "OUTPUT", "content": "The answer is 3.5"}
Now respond to the user's query following this exact format.
"""

message_history = []
user_query = input("Enter your query: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        {"role": "user", "parts": [{"text": user_query}]}
    ],
    config={
        "system_instruction": SYSTEM_PROMPT
    }
)

raw_result = response.text
message_history.append({"role": "assistant", "content": raw_result})

# Parse and display step by step with delays (streaming effect)
print("\n")
for line in raw_result.strip().split('\n'):
    try:
        parsed_result = json.loads(line)
        
        if parsed_result.get("step") == "START":
            print(f"🔥 {parsed_result.get('content')}\n")
            time.sleep(0.8)  # Delay after START
            
        elif parsed_result.get("step") == "PLAN":
            print(f"🧠 {parsed_result.get('content')}")
            time.sleep(0.6)  # Delay between PLAN steps
            
        elif parsed_result.get("step") == "OUTPUT":
            print(f"\n✅ {parsed_result.get('content')}")
            
    except json.JSONDecodeError:
        print(f"⚠️ Invalid JSON line: {line}")

# print("\n" + raw_result)