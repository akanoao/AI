from secret_key import APIKEY
from openai import OpenAI


client = OpenAI(api_key=APIKEY)
# chage
chat_log = [{"role": "system",
             "content": "you are a high school teacher who uses examples to explain things"}]
while True:
    user_input = input()
    if user_input == "quit":
        break
    else:
        chat_log.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=chat_log,
        )
        assistant_response = response.choices[0].message.content
        chat_log.append(
            {"role": "assistant", "content": assistant_response.strip().strip("/n")})
        print("assistant: ", assistant_response.strip().strip("/n"))

# print(response.model_dump_json(indent=2))
