from openai import OpenAI

from api_keys import openai_key

client = OpenAI(
      api_key = openai_key(),
  )
def negative_assistant_create():
    global negative_assistant
    negative_assistant = client.beta.assistants.create(
    name="Negative side debate robot.",
    instructions="""You are a debater. Next, you will first get a debate topic, and then get the affirmative debate answer.
                    As the opponent, your purpose is to first try to overturn the other party's argument with other concepts or arguments. If the other party's argument is too strong, try to put forward new points of view to prove that your point of view is right.
                        - Replies should be no more than one to two sentences in length.
                        - Never compromise with the other party or agree with the other party's point of view. """,
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
