print("welcome to my first game!\n")

name = input("what is your name? ").capitalize()
age = int(input("How old are you? "))
if age >= 18:
    print(f"{name}! You are old enough to play the game.")
    want_to_play = input("do you want to play?(yes/no) ").lower()
    if want_to_play == "yes":
        print("lets begin...")
        user_answer = input("left or right? ").lower()
        if user_answer == "left":
            print("correct!")
        else:
            print("game over!")
    else:
        print("cya...")
elif age >= 14:
    print(f"{name}! You can play with your parents.")
else:
    print(f"{name}! You are not old enough.")
