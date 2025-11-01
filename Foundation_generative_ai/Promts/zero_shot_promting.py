

import os
import ssl

# Force TLS 1.2 or higher
os.environ['CURL_CA_BUNDLE'] = ''

from google import genai

client = genai.Client(
    api_key = "AIzaSyCbfmGD1JvtwiOo8C7P80y6I0n3id87I7E"
    
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        {"role": "user", "parts": [{"text": "Hey, Can you help me solve a+ b  whole square "}]}
    ],
    config={
        "system_instruction": "You are an expert in Maths and only and only answer maths related questions"
    }
)


print(response.text)



