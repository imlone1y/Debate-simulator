from openai import OpenAI
from api_keys import openai_key

client = OpenAI(
      api_key = openai_key(),
  )

def judge_assistant_create():
    global judge_assistant
    judge_assistant = client.beta.assistants.create(
    name="辯論評分員",
    instructions="""你現在是一個公正的裁判。
                    接著你會得到一個辯論題目，以及來自正反方的辯論內容。
                    - 你要依據每次正/反方的內容、以及推翻對方論點的強度給出1~10的分數
                    - 接著再給出評分理由，字數盡量精簡。
                    - 回覆統一格式為: 正方 - ?分，理由。
                                     反方 - ?分，理由。""",
    model="gpt-3.5-turbo-16k",
    tools=[{"type": "code_interpreter"}]
    )
    global my_thread
    my_thread = client.beta.threads.create()

def judger_reply(text):
   
    my_thread_message = client.beta.threads.messages.create(
      thread_id=my_thread.id,
      role="user",
      content=str(text),
    )
    print(f"This is the message object: {my_thread_message} \n")


    my_run = client.beta.threads.runs.create(
      thread_id=my_thread.id,
      assistant_id=judge_assistant.id,
    )

    while my_run.status in ["queued", "in_progress"]:
        keep_retrieving_run = client.beta.threads.runs.retrieve(
            thread_id=my_thread.id,
            run_id=my_run.id
        )
        print(f"Run status: {keep_retrieving_run.status}")

        if keep_retrieving_run.status == "completed":
            print("\n")

            all_messages = client.beta.threads.messages.list(
                thread_id=my_thread.id
            )

            print("------------------------------------------------------------ \n")

            print(f"User: {my_thread_message.content[0].text.value}")
            print(f"Assistant: {all_messages.data[0].content[0].text.value}")

            break
        elif keep_retrieving_run.status == "queued" or keep_retrieving_run.status == "in_progress":
            pass
        else:
            print(f"Run status: {keep_retrieving_run.status}")
            break
      
    return str(all_messages.data[0].content[0].text.value)
