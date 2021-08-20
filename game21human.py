import random
while True:
    s21 = 0
    rd = random.randint(0, 1)
    if rd == 0:
        s21_player="you"
    else:
        s21_player="me"

    while s21 <= 21:

        print("The s21 is " + str(s21)+".")
        print()
        if s21_player == "you":
            print("Add 1, 2, or 3. Do not pass 21. The player who lands on 21 loses.")

            you_choice = input("What will you add? ")
            while you_choice not in ["1", "2", "3"]:
                you_choice = input("NO,add 1, 2 or 3.What will you add? ")

            you_choice = int(you_choice)
            s21 = s21 + you_choice
            print()

            if s21 >= 21:
                print("The current number is " + str(s21) + ".")
                print()
                print("Sorry, you lose.")
                break
            else:
                s21_player = "me"
        else:
            me_choice = random.randint(1,3)
            print("My turn. I choses " + str(me_choice)+".")
            s21= s21 + me_choice
            if s21 >= 21:
                print("The current number is " + str(s21) + ".")
                print()
                print("Well done, you won!")
                break
            else:
                s21_player ="you"
    play_again = input("Do you want to play again? ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Goodbye")
        break
