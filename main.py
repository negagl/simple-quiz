# First we welcome the player
print("Welcome to this mini-quiz about League of Legends!!!")

# Wants to play?
playing = input("Do you want to play? (y/n): ").lower()
if playing != "y" and playing != "yes":
    if playing == "n" or playing == "no":
        print("You typed '" + playing + "'. Quitting...")
        quit()
    else:
        print("You typed '" + playing + "'. That's not a valid choice. Quitting...")
        quit()

# Creating point system
point = 0

# If playing then we ask the questions
answer = input("Which programming language is this quiz built on?: ").lower()
if answer == 'python':
    print("That's right!!! One point to griffyndor")
    point += 1
else:
    print("Ugh, that's incorrect ):")

# And more questions
# Question 1
answer = input("Last one was not a LOL question hehe. What is my favorite league champion?: ").lower()
if answer == 'thresh':
    print("That's right!!! Love that one")
    point += 1
else:
    print("Ugh, that's incorrect ): answer is Thresh")

# Question 2
answer = input("What is Ruined King's actual name?: ").lower()
if answer == 'viego':
    print("Correct! You rock on this")
    point += 1
else:
    print("Oops, nope ):")

#  Question 3
answer = input("What's that one game mode which is played in a single rail?: ").lower()
if answer == 'aram':
    print("Correct!")
    point += 1
else:
    print("Meh, no ):")

print("Total questions answered correctly: " + str(point) + "/4")
print("you got " + str(int((point * 100)/4)) + "% correct.")
