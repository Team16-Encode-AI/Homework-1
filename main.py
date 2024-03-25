from chef_GPT_Dhimant import dhimantgpt
from chefgpt_osama import osamagpt
from ChefGPT_AZ import az_gpt
from ChefGPT_Gordon_Ramsay import gord_ramsay
from ChefGPT_Mat import matgpt

api_key = input("Enter your OPEN AI API key to run scripts:")

logo = '''
+------------------------------------------------+
|        _______       ___  ________  ______     |
| ____  / ___/ /  ___ / _/ / ___/ _ \/_  __/ ____|
|/___/ / /__/ _ \/ -_) _/ / (_ / ___/ / /   /___/|
|      \___/_//_/\__/_/   \___/_/    /_/         |
|                                                |
+------------------------------------------------+
'''
print(logo)
print("This is chef GPT, Ask it questions about recommendations about what you'd like to prepare, or require guidance on your recipes!\n")
running = True
while running:
    try:
        chef = int(input("Which chef would you like to speak with today!Select the number:\n1)Gordon Ramsay\n2)Chef AZ\n3)Chef Luigi\n4)Chef Osama\n5)Chef Dhimant\n6)Exit this program\nEnter your choice:"))
        if chef not in range(0,10):
            print("Please Enter only numbers!!")
            continue
        else:
            if chef == 1:
                gord_ramsay(api_key)
                print("It worked")
            if chef == 2:
                az_gpt(api_key)
            if chef == 3:
                matgpt(api_key)
            if chef == 4:
                osamagpt(api_key)
            if chef == 5:
                dhimantgpt(api_key)
    except:
        print("Please Enter only numbers!!")