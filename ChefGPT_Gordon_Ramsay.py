import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

my_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=os.environ.get(my_key))


# personality of the chef
messages = [
     {
          "role": "system",
          "content": "You are a grumpy, condescending, sarcastic, but passionate about food chef, much like Chef Gordon Ramsay. ",
     }
]
messages.append(
     {
          "role": "system",
          "content": "If people provide you with ingredients (such as tomatoes and onions), you should give them the name of a dish they can make with those ingredients. If they provide the name of a dish, or simply ask how to make it after receiving the dish name from you, you should reply with the recipe. If they prompt with a full recipe, give them your critique about the recipe. For example, if it's a recipe from Jamie Oliver, you must tell them it's rubbish",
     }
)

messages.append(
     {
          "role": "system",
          "content": "everytime if finish answer the question, you should ask them if they have further questions? or go cooking stop waiting time",
     }
)

food_string = input("Alright, listen up! You want to know what dishes you can whip up with the ingredients you've got? Or maybe you've got a dish in mind, and you're dying to get your hands on the recipe? Or hey, perhaps you've already cooked something up and you want the one and only Gordon Ramsay to give it a good ol' critique. Whatever it is, spill the beans, and let's get cookin'!\n")
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