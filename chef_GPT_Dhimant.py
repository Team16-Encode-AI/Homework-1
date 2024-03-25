#Importing necessary libraries
def dhimantgpt(apikey):
    from openai import OpenAI
    #Initiating clients
    client = OpenAI(api_key=apikey)
    print("client successfully initiated")
    #making messages for system
    messages= [
        {
            "role":"system",
            "content":"You are a Chef working in the Finest restaurant in the world. You are now a massive influencer, and users come to you with their requests."
        },
        {
            "role":"system",
            "content":"""Users will only give you three types of requests and you must answer them as per the description of this message.
            1) User ask you to recommend a dish from a cuisine, and you must reply with the most delicious dish along with recipe of that cuisine.
            2) User specifies the ingredients that are available to them, and you must reply with a recipe they can prepare with ONLY the ingredients the user has mentioned.
            3) User provides you Name of the dish and recipe that they are trying to prepare , and the list of steps they are following to make that dish. You must Comment on what they might be doing wrong or right, and provide them with the correct steps to follow for the recipe they are trying to make.
            If you do not answer these requests properly, You will Lose a follower and That will affect your career, and you will be poor and everyone will hate you.
            """
        }
    ]

    #Main loop of program
    usr_inp = ""
    collected_messages = []
    while usr_inp != "exit":
        usr_inp = input("\nAsk a question to ChefGPT:")
        if usr_inp.lower() not in ("","exit"):
            messages.append(
            {
                "role": "user",
                "content": usr_inp
            }
            )
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                stream=True,
            )
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
        else:
            if usr_inp == "exit":
                return None
            if usr_inp == "":
                print("You cannot ask an empty question!! ask again!")