import sys
import csv
import os


def menu():
    print("\nDictionary for a little programmer:\n")
    print("1) search explanation by apellation \n")
    print("2) add new definition \n")
    print("3) show all apellations alphabetically \n")
    print("4) show available definitions by first letter of apellation \n")
    print("0) exit \n")


def open_csv():
    '''Opens a given csv file containing dictionary'''
    definitions = {}
    with open("dictionary.csv", "r", newline='') as f:
        r = csv.reader(f, delimiter=' ')
        for row in r:
            definitions[row[0]] = (row[1], row[2])
        return definitions


def write_to_csv(defintions):
    '''Writes given dictionary into a csv file'''
    with open("dictionary.csv", "w", newline='') as f:
        w = csv.writer(f, delimiter=' ')
        for key in definitions:
            w.writerow([key, definitions[key][0], definitions[key][1]])


def search_appelation(definitions):
    '''Searches an appelation in dictionary and then prints it'''
    search = input("\n\nPlease enter an appellation:\n\n")
    search = search.lower()
    os.system('clear')
    if search in definitions:
        return search + "\n"*2 + definitions[search][0] + "\n"*2 + definitions[search][1]
    else:
        return "\n"*2 + "Sorry. We don't have a definition on that yet." + "\n"*2


def new_definition(definitions):
    '''Creates a new definition in a dictionary'''
    apel = input("\nPlease enter the definition name (apellation)\n")
    expl = input("\nPlease enter the explanation\n")
    sour = input("\nPlease enter the source\n")
    while apel == "" or expl == "" or sour == "":
        print("Sorry. Neither of those can be empty.")
        apel = input("\nPlease enter the definition name (apellation)\n")
        expl = input("\nPlease enter the explanation\n")
        sour = input("\nPlease enter the source\n")
    else:
        print("\n\n Definition added succesfully.")
        definitions[apel] = (expl, sour)
        return definitions


def show_apels_alphabet(definitions):
    '''Sorts and shows apellations in
    alphabetical order'''
    keys = []
    for key in definitions:
        keys.append(key)
    keys = sorted(keys)
    for key in keys:
        print("\n" + key + "\n")


def show_definitions_by_letter(definitions):
    ''' Shows definition starting with given letter'''
    defbylet = []
    let = input("Enter a letter:\n")
    for key in definitions:
        if key.startswith(let):
            defbylet.append(key)
    defbylet = sorted(defbylet)
    for definition in defbylet:
        print("\n" + definition + "\n")


def main():

    definitions = open_csv()

    while True:

        menu()
        choice = input("Please enter a responsive number: ")

        if choice == "1":
            print(search_appelation(definitions))
        elif choice == "2":
            definitions = new_definition(definitions)
            write_to_csv(definitions)
        elif choice == "3":
            show_apels_alphabet(definitions)
            print(search_appelation(definitions))
        elif choice == "4":
            show_definitions_by_letter(definitions)
            print(search_appelation(definitions))
        elif choice == "0":
                print("\nPleasure working with you! \n")
                sys.exit()


if __name__ == "__main__":
    main()
