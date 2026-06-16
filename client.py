from openai import OpenAI

#pip install openai
#defaults to getting the key using os.environ.get("OPENAI_API_KEY")
#if you saved the key under a differnt environment variable name, you can do something like:
client = OpenAI(
    api_key="<YOUR_OPEN_API_KEY>",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"sysyem","content": "you are a virtual assistant named jarvis sklilled in general tasks like alexa and google cloud"},
        {"role": "user", "content": "what is coding"}

    ]
)
print(completion.choices[0].message.content)