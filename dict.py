import sys
import csv
# Menu
print("\nDictionary for a little programmer:\n")
print("1) search explanation by apellation \n")
print("2) add new definition \n")
print("3) show all apellations alphabetically \n")
print("4) show available definitions by first letter of apellation \n")
print("0) exit \n")
choice = input("Choose an option by typing a responsive number \n")

definitions = {}

# Main dictionary
with open("dictionary.csv", "r", newline='') as f:
    r = csv.reader(f, delimiter=' ')
    for row in r:
        definitions[row[0]] = row[1]


# Saving the dictionary
def writingcsv():
    with open("dictionary.csv", "w", newline='') as f:
        w = csv.writer(f, delimiter=' ')
        for i in definitions:
            w.writerow([i, definitions[i]])


# Searching function. It's a function that searches.
def searching():
    search = input("Please enter an appellation:\n")
    search = search.lower()
    if search in definitions:
        return definitions[search]
    else:
        return "Sorry. We don't have a definition on that yet."


# New definition function. Based on variables.
def newdefinition():
    apel = input("Please enter the definition name (apellation)\n")
    expl = input("Please enter the explanation\n")
    sour = input("Please enter the source\n")
    while apel == "" or expl == "" or sour == "":
        print("Sorry. Neither of those can be empty.")
        apel = input("Please enter the definition name (apellation)\n")
        expl = input("Please enter the explanation\n")
        sour = input("Please enter the source\n")
    else:
        definitions[apel] = (expl, sour)
        print("Congratulations!")
        print("Your definitions looks like this:")
        print(definitions[apel])


# Showing apellations alphabetically
def apelalpha():
    keys = []
    for key in definitions:
        keys.append(key)
    keys = sorted(keys)
    return keys


def definitionsbylet():
    defbylet = []
    let = input("Enter a letter:\n")
    for key in definitions:
        if key.startswith(let):
            defbylet.append(key)
    defbylet = sorted(defbylet)
    return defbylet


# Idiiotproofing the option selection
while choice not in ["1", "2", "3", "4", "0"]:

    choice = input("Wrong input. Please select from following options (1, 2, 3, 4, 0)\n")

# Calling functions from the choice variable`
if choice == "1":
    print(searching())
elif choice == "2":
    newdefinition()
    writingcsv()
elif choice == "3":
    print(apelalpha())
    print(searching())
elif choice == "4":
    print(definitionsbylet())
    print(searching())
elif choice == "0":
        sys.exit
