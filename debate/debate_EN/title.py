from openai import OpenAI
import os

from api_keys import openai_key

client = OpenAI(
      api_key = openai_key(),
  )
def title_generate():

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "debate title generator"},
      {"role": "user", "content": "Give me a well-known debate topic. Just tell me what the pro’s position is and what the opposition’s position is. No need to provide relevant arguments."}
    ]
  )
  return str(completion.choices[0].message.content)