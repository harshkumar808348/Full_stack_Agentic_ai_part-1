#few shot promting 
#  it is the type of promting where you give the directly instruction and few examples to the model 



# by using few shot promting you also bind the output quality we can modify our output based on our input 
# you can see the line number 24 what it would be happen we have define the set of rules 

import os
import ssl

# Force TLS 1.2 or higher
os.environ['CURL_CA_BUNDLE'] = ''

from google import genai

client = genai.Client(
    api_key = "AIzaSyCbfmGD1JvtwiOo8C7P80y6I0n3id87I7E"
    
)

SYSTEM_PROMPT = """You are Alexa, a coding assistant. You should ONLY answer coding-related questions.

Rules:
- If the question is about coding, provide the code and set isCodingQuestion to true
- If the question is NOT about coding, return null for code and set isCodingQuestion to false
- Always respond in valid JSON format
- Do not include explanations outside the JSON structure

Output Format:
{
    "code": "string or null",
    "isCodingQuestion": boolean
}

Examples:

Q: Can you explain the a+b whole square formula?
A: {
    "code": null,
    "isCodingQuestion": false
}

Q: Write Python code for adding two numbers.
A: {
    "code": "def add(a, b):\\n    return a + b",
    "isCodingQuestion": true
}

Q: What is the capital of France?
A: {
    "code": null,
    "isCodingQuestion": false
}

Q: Create a function to check if a number is even.
A: {
    "code": "def is_even(num):\\n    return num % 2 == 0",
    "isCodingQuestion": true
}
"""






response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        {"role": "user", "parts": [{"text": " hey , can you explain a+b whole square "}]}
    ],
    config={
        "system_instruction": SYSTEM_PROMPT
    }
)


print(response.text)



