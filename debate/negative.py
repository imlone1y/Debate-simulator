from openai import OpenAI

client = OpenAI(
      api_key = "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",
  )

def negative_assistant_create():
    global negative_assistant
    negative_assistant = client.beta.assistants.create(
    name="反方辯論機器人",
    instructions="""你是一個辯論家，接下來你將會先得到一個辯論題目，後得到正方的辯論回覆。
                    而你是反方，你的目的是優先試圖以其他觀念或論點推翻對方的論點，如果對方的論點太過強大，就試著提出新的觀點，以證明你的觀點是對的。
                    - 回覆長度在一到兩句話以內。
                    - 絕對不能妥協對方、或認同對方的觀點。""",
    model="gpt-3.5-turbo-16k",
    tools=[{"type": "code_interpreter"}]
    )
    global my_thread
    my_thread = client.beta.threads.create()

def negative_reply(text):
   
    my_thread_message = client.beta.threads.messages.create(
      thread_id=my_thread.id,
      role="user",
      content=str(text),
    )
    print(f"This is the message object: {my_thread_message} \n")


    my_run = client.beta.threads.runs.create(
      thread_id=my_thread.id,
      assistant_id=negative_assistant.id,
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
