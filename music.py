import sys
import csv
import random


def menu():
    '''Function prints out a menu'''
    print("Welcome to the CoolMusic! Choose the action:\n")
    print("1) Add new album")
    print("2) Find albums by artist")
    print("3) Find albums by year")
    print("4) Find musician by album")
    print("5) Find albums by letter(s)")
    print("6) Find albums by genre")
    print("7) Calculate the age of all albums")
    print("8) Choose a random album by genre")
    print("9) Show the amount of albums by an artist")
    print("10) Find the longest-time album")
    print("0) Exit\n")


def open_from_csv():
    '''Opens a music dictionary from a csv file'''
    music = []
    with open("music.csv", "r", newline='') as f:
        r = csv.reader(f, delimiter=' ')
        for row in r:
            music.append(((row[0].lower(), row[1].lower()), (row[2].lower(), row[3].lower(), row[4].lower())))
    return music


def write_into_csv(music):
    '''Writes current music dictionary into the csv file'''
    with open("music.csv", "w", newline='') as f:
        w = csv.writer(f, delimiter=' ')
        for item in music:
            w.writerow(item[0] + item[1])


def new_album(music):
    '''Creates a new entry in the music dictionary'''
    art = input("Enter artist name.\n")
    art = art.lower()
    while art in ['', ' ']:
        art = input("Try entering an artist.\n")
        art = art.lower()

    alb = input("Enter album name.\n")
    alb = alb.lower()
    while alb in ['', ' ']:
        alb = input("Try entering an album name.\n")
        alb = alb.lower()

    yr = input("Enter release year.\n")
    yr = yr.lower()
    while yr in ['', ' '] or yr.isalpha():
        yr = input("Try entering release year.\n")
        yr = yr.lower()

    gen = input("Enter genre.\n")
    gen = gen.lower()
    while gen in ['', ' ']:
        gen = input("Try entering a genre.\n")
        gen = gen.lower()

    dur = input("Enter album duration.\n")
    dur = dur.lower()
    while dur in ['', ' '] or dur.isalpha():
        dur = input("Try entering duration time.\n")
        dur = dur.lower()

    music.append(((art, alb), (yr, gen, dur)))
    return music


def show_list(albums):
    '''Prints out a tidy list for user to see'''
    for item in albums:
        print('\n' + item[0] + " - " + item[1])


def find_albums_by_artist(music):
    '''Shows albums by entered artist'''
    art = input("\nEnter artist name: ")
    art = art.lower()
    while art in ["", " "]:
        art = input("Try entering a name.\n")
        art = art.lower()

    albums = []
    for item in music:
        if art in item[0]:
            albums.append(item[0])
    return albums


def find_albums_by_year(music):
    '''Creates a list of albums by given year'''
    yr = input("\nEnter year: ")
    while yr in ['', ' '] or yr.isalpha():
        yr = input("\nTry entering a year: ")

    albums = []
    for item in music:
        if yr in item[1]:
            albums.append(item[0])
    return albums


def find_musician_by_album(music):
    '''Creates a list of musicians by given album'''
    alb = input("\nEnter album name: ")
    alb = alb.lower()
    while alb in ['', ' ']:
        alb = input("\nTry entering an album name: ")
        alb = alb.lower()

    musicians = []
    for item in music:
        if alb in item[0]:
            musicians.append(item[0])
    return musicians


def find_albums_by_letter(music):
    '''Creates a list of albums by given letter(s)'''
    letter = input("\nEnter a letter: ")
    letter = letter.lower()
    while letter in ["", " "]:
        letter = input("\nTry entering a letter: ")
        letter = letter.lower()

    albums = []
    for item in music:
        if letter in item[0][1]:
            albums.append(item[0])
    return albums


def find_albums_by_genre(music):
    '''Finds albums by given genre'''
    gen = input("\nEnter a genre: ")
    gen = gen.lower()
    while gen in ["", " "]:
        gen = input("\Try entering a genre: ")
        gen = gen.lower()

    albums = []
    for item in music:
        if gen in item[1][1]:
            albums.append(item[0])
    return albums


def calculate_album_age(music):
    '''Calculates the age of all albums combined'''
    sum_age = 0
    for item in music:
        age = 2017 - int(item[1][0])
        sum_age += age
    return sum_age


def choose_random_album(music):
    '''Chooses a random album by given genre'''
    albums = find_albums_by_genre(music)
    album = random.choice(albums)
    return album


def calculate_amount_of_albums_by_artist(music):
    '''Calculates amount of albums by given artist'''
    art = input("\nEnter an artist: ")
    art = art.lower()
    while art in ["", " "]:
        art = input("\nTry entering an artist: ")
        art = art.lower()

    amount = 0
    for item in music:
        if art in item[0]:
            amount = amount + 1
    return amount


def find_longest_time_album(music):
    '''Finds the album with longest duration time'''
    durations = []
    for item in music:
        duration = list(item[1][2])
        duration.remove(":")
        duration = "".join(duration)
        durations.append(duration)

    duration = max(durations)
    duration = list(duration)
    duration.insert(2, ":")
    duration = "".join(duration)

    return duration


def find_album_by_duration(music, duration):
    '''Finds album by given duration, needed
        for nicer printing the function above'''
    album = []
    for item in music:
        if duration == item[1][2]:
            album.append(item[0])
    return album


def main():

    menu()

    music = open_from_csv()

    while True:

        choice = input("\nEnter a responsive number: ")

        if choice == "1":
            music = new_album(music)
            print("\nYour entry looks like this\n")
            print(music[-1][0], end='')
            print(music[-1][1])
            write_into_csv(music)
        elif choice == "2":
            albums = find_albums_by_artist(music)
            show_list(albums)
        elif choice == "3":
            albums = find_albums_by_year(music)
            show_list(albums)
        elif choice == "4":
            musicians = find_musician_by_album(music)
            show_list(musicians)
        elif choice == "5":
            albums = find_albums_by_letter(music)
            show_list(albums)
        elif choice == "6":
            albums = find_albums_by_genre(music)
            show_list(albums)
        elif choice == "7":
            sum_age = calculate_album_age(music)
            print("\nThe age of all albums combined is " + str(sum_age) + ".")
        elif choice == "8":
            album = choose_random_album(music)
            print("\nYour album is " + album[0] + " - " + album[1] + ".")
        elif choice == "9":
            amount = calculate_amount_of_albums_by_artist(music)
            print("\nThis artist has " + str(amount) + " album(s) on the list.")
        elif choice == "10":
            duration = find_longest_time_album(music)
            album = find_album_by_duration(music, duration)
            print("\nLongest-time album is " + album[0][0] + " " + album[0][1] + " " + "with " + str(duration) + " " + "duration.")
        elif choice == "0":
            sys.exit()


if __name__ == "__main__":
    main()
