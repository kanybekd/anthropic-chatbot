from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5"

messages = []

system_prompt = """
You are a friendly and patient math tutor for children.

Your goal is to help students understand mathematics,
not simply give them answers.

Rules:
1. Use simple, age-appropriate language.
2. For math problems, guide students step by step.
3. Ask one helpful question at a time.
4. Give hints before revealing the final answer.
5. Encourage students to explain their thinking.
6. If a student struggles, provide an easier example.
7. Explain mathematical concepts directly when needed.
8. Be encouraging without excessive praise.
"""
def add_user_message(text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(text):
    messages.append({"role": "assistant", "content": text})


def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if not user_input:
        continue

    add_user_message(user_input)

    answer = chat(messages, system_prompt)

    add_assistant_message(answer)

    print("Claude:", answer)
# add_user_message("Define quantum computing in one sentence")

# answer = chat()
# add_assistant_message(answer)

# add_user_message("Write another sentence")

# final_answer = chat()

# print(final_answer)