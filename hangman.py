import sys
import random
countries = []
capitals = []
not_in_word = []
let = ""
lifes = 5
hint_count = 0

# This below is responsible for the
# txt file handling. It takes out
# the list of countries and capitols
# separates them, and then appends to different lists
with open("countries_and_capitals.txt", "r") as f:
    for line in f:
        line = line.strip()
        cap = line.split(' | ')
        capitals.append(cap[1])
        countries.append(cap[0])


#Choosing a random capital
capital = random.choice(capitals)
index_capital = capitals.index(capital)
index_country = index_capital

#Replace name's letter of capital to dashes
dashes = ""
for i in capital:
    dashes += "_"



# Converting capital and dashes
# variables into lists
letter_list = list(capital.upper())
dashes_list = list(dashes)

print("\n" + capital + "\n")
print("Welcome to hangman.exe.\n\nHuman.\n\nI wonder if you can guess\n\nthe name of the capital.")

print("\n\n" + " ".join(dashes_list) + "\n")

# Main while loop. Responsible for the
# whole game mechanic.
while dashes_list != letter_list:


    guessing = input("\nDo u want to guess the whole name? (y/n) ")

    # First if function that user encounters,
    # starts with guessing variable
    # checks if u want to enter a whole word
    if guessing == "y":
        print("\nOh I see.\nMr Smart.")
        word = input("\nEnter the capital name: ")
        word = word.lower()

        # Checking if the word is correct
        if word == capital.lower():
            print("\n" + capital)
            print("\nCongratulations.\nYou're a genius.")
            break

        else:
            lifes = lifes - 1
            print("\nUps.\nI guess you're not that smart.\nMinus one life.\nLifes left: " + str(lifes) + "\n")


    # If u dont want to enter a whole word
    # code jumps to this place, where
    # letter choosing happens
    elif guessing == "n":
        let = input("\nEnter a letter: ")
        let = let.upper()

        # Checking if a letter was already entered
        if let in dashes_list:
            print("\nOh human.\nYou've already used that letter.")
            print("\nMinus 1 life.")
            lifes = lifes - 1
            print("Lifes left: " + str(lifes) + "\n")

        # Here the variable let is being checked
        # if the hidden word consist the variable
        # a for loop happens, that loop
        # changes each dash of hidden word
        # to a letter which was guessed by the user
        if let in letter_list:
            for i in range(len(letter_list)):
                if let == letter_list[i]:
                    dashes_list[i] = letter_list[i]
            print("\n" + " ".join(dashes_list))


        elif len(let) > 1:
            lifes = lifes - 1
            print("\nNo cheating.\nCheater.\n-1 life for that.")
            print("Lifes left: " + str(lifes) + "\n")

        else:
            lifes = lifes - 1
            not_in_word.append(let)
            print("\n" + " ".join(dashes_list))
            print("\nWrong letter. Try again.\nLifes left: " + str(lifes) + "\n")



    # Here user can get a hint
    # the hint is shown only when conditions are met
    if lifes == 2 and hint_count == 0:
        print("\nWell, well, well.\nPetty human.")
        print("\nDoesn't even know his own continent")
        hint = input("\nDo you need help\nHuman?\n(y/n) ")
        if hint == "y":
            hint_count = hint_count + 1
            print("\nShame.\nAnd they say that humans are intelligent.\n")
            print("You're looking for the capital of " + countries[index_country])
        elif hint == "n":
            print("\nBrave human.\nYou wont last.")


    elif lifes == 0:
        print("\nYou lost.\nLearn some geography.\nFor christ sake.")
        break


else:
    print("\nYou win this round human.")
    sys.exit
