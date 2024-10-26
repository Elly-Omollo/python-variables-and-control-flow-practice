# Using a while loop, write a function that continuously asks the user for input until they type the word "exit".
#  The program should print each word entered by the user before asking for the next input.



def ask_for_input():
    while True:
        user_input = input("Enter a word (type 'exit' to quit this programm): ")
        if user_input.lower() == "exit":
            break
        print(user_input)


ask_for_input()
