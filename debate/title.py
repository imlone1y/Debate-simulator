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
      {"role": "system", "content": "辯論題目產生器"},
      {"role": "user", "content": "給我一個有名的辯論題目，只要給我正方的立場是什麼，以及反方的立場是什麼就可以了，不用提供相關論證"}
    ]
  )
  return str(completion.choices[0].message.content)