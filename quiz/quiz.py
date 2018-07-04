def show_menu():
    print("1. Ask Questions")
    print("2. Add a Question")
    print("3. Exit Game")
    return input("Enter Option: ")
    
   
def game_loop():
    while True:
        option= show_menu()
        if option == 1:
            print("You selected: Ask Questions")
        elif option == 2:
            add_question()
        elif option == 3:
            print("Goodbye")
            break
        else:
            print("Invalid Option")
        print("")
    return option



def add_question():
    print("")
    question = raw_input("Enter a question\n> ")
    print("")
    print("Ok, tell me the answer")
    answer =  raw_input("{0}\n> ".format(question))
    
    file  =  open("questions.txt", 'a')
    file.write(question + "\n")
    file.write(answer +"\n")
    file.close()

game_loop()