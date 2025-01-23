import random
emoji={'r':'🪨','p':'📃','s':'✂️'}
ch=['r','p','s']
while True:
    user_choice=input("enter the ch (r/p/s)").lower()
    computer_generating = random.choice(ch)
    print(f"{emoji[user_choice]} {user_choice} user eneterd")
    print(f"{emoji[computer_generating]}{computer_generating} computer generated")
    if user_choice not in ch:
        print("invalid")
    elif user_choice==computer_generating:
        print("tie")
    elif user_choice=='r' and computer_generating=='p':
        print(emoji[user_choice], "and" ,emoji[computer_generating],"i am win")
    elif user_choice=='p' and computer_generating=='s':
        print(emoji[user_choice], "and" ,emoji[computer_generating],"i am win")
    elif user_choice=='s' and computer_generating=='r':
        print(emoji[user_choice], "and" ,emoji[computer_generating],"iam win")
    else:
        print(emoji[user_choice], "and" ,emoji[computer_generating],"computer will be win")
    continue_another_time=input("continue the game yes or no ?(y\n)").lower()
    if continue_another_time=='n':
        break