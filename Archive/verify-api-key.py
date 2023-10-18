import openai

# openai.log = "debug"
openai.api_key = "sk-xxx"
openai.api_base = "https://api.openai.com"

while True:
    text = input("请输入问题：")
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': text},
        ],
        stream=True
    )

    for chunk in response:
        print(chunk.choices[0].delta.get("content", ""), end="", flush=True)
    print("\n")
