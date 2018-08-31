import random
import time

#usernmame
name = input(" What is your name? ")

#responses
ans_1 = "Yes"
ans_2 = "No"
ans_3 = "Probably"
ans_4 = "Up To You"
ans_5 = "Maybe"
ans_6 = "Who knows"

while True:
    #question
    question = input(" What would you like to know? ")

    #randoms
    answers = [ans_1, ans_2, ans_3, ans_4, ans_5, ans_6]

    #entire_statement
    print(name + " your answer is " + random.choice(answers))

    cmd = input(" Do you want to[q]uit or [c]ontinue: ")
    if cmd == "q":
        break
    else: 
        continue 
    
