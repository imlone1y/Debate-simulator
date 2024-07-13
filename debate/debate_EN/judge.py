from openai import OpenAI
from api_keys import openai_key

client = OpenAI(
      api_key = openai_key(),
  )

def judge_assistant_create():
    global judge_assistant
    judge_assistant = client.beta.assistants.create(
    name="Debate Judge",
    instructions="""You are now an impartial judge.
                    You will receive a debate topic and arguments from both the affirmative and negative sides.
                        - Based on the content and the strength of rebuttals from each side, you will give a score from 1 to 10.
                        - Then, provide a reason for the score, keeping it as concise as possible.
                        - Use the following format for your response:
                        Affirmative - ? points, reason.
                        Negative - ? points, reason.""",
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
