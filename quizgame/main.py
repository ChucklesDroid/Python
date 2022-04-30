def new_game() :
    questionNumber = 1      # stores question number
    guesses = []            # Empty list to hold user guesses
    score = 0               # Stores score of the user
    correct_guesses = 0     # value of correct answes guessed
    print("----------------------Quiz Game----------------------")
    for key in Questions:
        print('{}.{}'.format(questionNumber,key))
        for opt in Options[questionNumber - 1]:
            print(opt)
        print("--------------------------------------------")
        guess = input("Enter most suitable option: ").upper()
        guesses.append(guess)
        if check_ans(Questions.get(key) , guess):
            correct_guesses += 1
            print("Correct Answer")
        else:
            print("Wrong Answer")
        print("--------------------------------------------")
        questionNumber += 1
    score(correct_guesses,guesses) 


def check_ans(answer,guess):
    if answer == guess:
        return 1
    else :
        return 0


def score( correct_guesses, guesses ):
    print("----------------------")
    print("Your Guesses: ", end="") 
    for i in guesses:
        print(i, end = " ")
    print("Correct Answers: ", end = "")
    for key in Questions:
        print(Questions.get(key), end = " ")
    print("----------------------")


def play_again() :
    pass

#  Questions are stored in a dictionary along with its correct answer option
Questions = {' Who was the founder of python? ':'A',
             ' When was python created ? ':'B',
             ' Is the Earth flat ?':'A',
             ' Which one of them is not one of open source organisations?':'C'}
#  Options for question are stored in 2d lists
Options = [[' A.Guido van Rossum',' B.Larry Page',' C.Brian Kerninghan',' D.Dennis Ritchie'],
           [" A.2005"," B.1991"," C.1978"," D.1995"],
           [" A.correct"," B.incorrect"," C.sometimes",' D.maybe'],
           [' A.North Star',' B.HaikuOS',' C.Cannonical',' D.CCextractor']]
repeat = 1                      # It controls the while loop
while repeat:                   # It asks if the user wants to play again
    new_game()
    repeat = play_again()
