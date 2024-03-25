
print('Hi, What are the different scripts that you would like to run?')

string_input = input("Gimme file name, one at a time, or shout 'STOP!' if you want to stop.\n")

while string_input:

    if 'stop' in string_input.lower():
        print("Ok, I won't ask you for any more scripts.")
        break
    else:
        try:
            print('Now trying to work with the script you have requestes')
            exec(open(string_input).read())
        except:
            print("THis doesn't seem to be a legitimate script name. Give me a new one, or shout 'STOP' if you're not interested to continue.")
            
    string_input = input("Gimme file name, one at a time, or shout 'STOP!' if you want to stop.\n")