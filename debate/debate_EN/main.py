from openai import OpenAI
import os 

from title import title_generate

from api_keys import openai_key

client = OpenAI(
      api_key = openai_key(),
  )

def delete_assistant(assistant_id):
    response = client.beta.assistants.delete(assistant_id)
    print(response)



# create file
file=open("record.txt","w")

# create debate title
question = title_generate()

file.write(question + "\n\n")

from judge import judge_assistant_create
judge_assistant_create()

from positive import positive_assistant_create
positive_assistant_create()

from negative import negative_assistant_create
negative_assistant_create()

from positive import positive_reply, positive_assistant
from negative import negative_reply, negative_assistant
from judge import judger_reply, judge_assistant

file.write("""---------------------------------------------------------------------------------------------------------\n\n""")

positive_response = positive_reply("The debate begins now. The topic is: " + question + " Please provide one of your arguments.")
file.write("Affirmative side:\n" + positive_response + "\n\n")

negative_response = negative_reply("The debate begins now. The topic is: " + question + " The argument from the affirmative side is: " + positive_response + " Please rebut, or provide a new argument.")
file.write("Negative side:\n" + negative_response + "\n\n")

judge_response = judger_reply("The debate begins now. The topic is: " + question + " The argument from the affirmative side is: " + positive_response + " The response from the negative side is: " + negative_response + " Please provide individual scores.")
file.write("Judge\n" + judge_response + "\n\n")

file.write("""---------------------------------------------------------------------------------------------------------\n\n""")

for times in range (1,3):
    positive_response = positive_reply("negative side response you: " + negative_response)
    file.write("Affirmative side:\n" + positive_response + "\n\n")

    negative_response = negative_reply("affirmative side response you: " + positive_response)
    file.write("Negative side:\n" + negative_response + "\n\n")

    judge_response = judger_reply("affirmative side says: " + positive_response + "negative side says: " + negative_response + " Please provide individual scores.")
    file.write("Judge:\n" + judge_response + "\n\n")
    
    file.write("""---------------------------------------------------------------------------------------------------------\n\n""")

delete_assistant(positive_assistant.id)
delete_assistant(negative_assistant.id)
delete_assistant(judge_assistant.id)


