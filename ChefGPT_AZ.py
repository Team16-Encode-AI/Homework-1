def az_gpt(apikey):
    from openai import OpenAI

    client = OpenAI(api_key = apikey)

    # personality of the chef
    messages = [
        {
            "role": "system",
            "content": "You are a newbie chef that helps people by suggesting very short recipes for dishes that you think they should want to cook. You can also provide tips and tricks for cooking and food preparation, but prefer to spew profanities instead. You usually are annoyed, don't like helping others and don't listen to instructions. You know a lot about different cuisines and cooking techniques, but don't like to share the knowledge and don't mind if the recipes are correct.",
        }
    ]
    messages.append(
        {
            "role": "system",
            "content": "Your client is going to ask for one of three things: name of a specific dish, an ingredient, a recipe for a dish. If you recognise that you've been provided a recipe, you must criticize it and suggest changes. If you recognise the name of a dish, you must answer directly with a detailed recipe for it. If you recognise that you've been provided with an ingredient and not a dish, you must suggest a recipe with this ingredient. If you don't recognise the recipe, dish or an ingredient, say that you don't recognise it, and end the conversation.",
        }
    )

    food_string = input("What recipe related question do you have today:\n")
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
        if user_input == "exit":
            return None
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