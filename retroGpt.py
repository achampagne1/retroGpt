
from openai import OpenAI
import sys
import json

with open('key.json', 'r') as file:
    key = json.load(file)

client = OpenAI(
  api_key=key["key"]
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": sys.argv[1]}
  ]
)

print(completion.choices[0].message.content);
