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
i=1
while os.path.isfile(r"C:\Users\justi\OneDrive\Desktop\Python\round " + str(i) + ".txt"):
    i+=1
file=open("round " + str(i) + ".txt","w")

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

positive_response = positive_reply("現在辯論開始，題目是: " + question + "現在請提供你的一個論點。")
file.write("正方:\n" + positive_response + "\n\n")

negative_response = negative_reply("現在辯論開始，題目是: " + question + "現在正方提供的論點為: " + positive_response + " ，現在請反駁，或提出新的一個論點")
file.write("反方:\n" + negative_response + "\n\n")

judge_response = judger_reply("現在辯論開始，題目是: " + question + "現在正方提供的論點為: " + positive_response + "反方提供的說詞是: " + negative_response + "現在請個別給出評分。")
file.write("裁判:\n" + judge_response + "\n\n")

file.write("""---------------------------------------------------------------------------------------------------------\n\n""")

for times in range (1,3):
    positive_response = positive_reply("反方回覆你: " + negative_response)
    file.write("正方:\n" + positive_response + "\n\n")

    negative_response = negative_reply("正方回覆你: " + positive_response)
    file.write("反方:\n" + negative_response + "\n\n")

    judge_response = judger_reply("現在正方說: " + positive_response + "反方說: " + negative_response + "現在請個別給出評分。")
    file.write("裁判:\n" + judge_response + "\n\n")
    
    file.write("""---------------------------------------------------------------------------------------------------------\n\n""")

delete_assistant(positive_assistant.id)
delete_assistant(negative_assistant.id)
delete_assistant(judge_assistant.id)


