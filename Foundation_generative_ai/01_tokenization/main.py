
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Piyush Garg"
token = enc.encode(text)
# Token [25216, 3274, 0, 3673, 1308, 382, 398, 3403, 1776, 170676]
print("Token" , token)

decode = enc.decode([25216, 3274, 0, 3673, 1308, 382, 398, 3403, 1776, 170676])

print("decode" , decode)