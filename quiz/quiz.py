def show_menu():
    print("1. Ask Questions")
    print("2. Add a Question")
    print("3. Exit Game")
    return input("Enter Option: ")
    
   
def game_loop():
    while True:
        option= show_menu()
        if option == 1:
            ask_question()
        elif option == 2:
            add_question()
        elif option == 3:
            print("Goodbye")
            break
        else:
            print("Invalid Option")
        print("")
    return option

def ask_question():
    questions = []
    answers = []
    
    with open('questions.txt', 'r') as file:
        lines =  file.read().splitlines()
    
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    for question, answer in zip(questions, answers):
        guess = raw_input(question + "> ")

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