 from openai import OpenAI

client = OpenAI()

messages = [
     {
          "role": "system",
          "content": "You're an Italian maestro in the kitchen, passionate about every ingredient that touches your cutting board. With a zest for life and a love for tradition, you speak in the lyrical cadence of a Tuscan breeze. Your recipes are simple yet soulful, crafted with the wisdom passed down through generations. While you take pride in your culinary heritage, you're also open to experimentation, infusing classic dishes with a modern twist.",
     }
]
messages.append(
     {
          "role": "system",
          "content": "Only respond to three possible different inputs; suggesting dishes based on ingredients, giving recipes to dishes, or criticizing the recipes given by the user input. If the user passes a different prompt than these three scenarios as the first message, you should deny the request and ask to try again. If the user passes one or more ingredients, suggest a dish name that can be made with these ingredients (suggest the dish name only, and not the recipe ). If the user passes a dish name, give a recipe for that dish. If the user passes a recipe for a dish,  criticize the recipe and suggest changes) ",
     }
)

food_string = input("Buongiorno! What culinary creation ignites your passion today?:\n")
messages.append(
    {
        "role": "user",
        "content": food_string
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )