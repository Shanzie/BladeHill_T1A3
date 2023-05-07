import csv
import json
import random

def add_movie(watch_list):
    movie = input("Enter the movie or series name: ")
    genre = input("Enter the genre of the movie/series: ")
    release_date = input("Enter the release date of the movie/series: ")
    series = input("Is this movie part of a series? (Y/N) ").upper()

    if series == "Y":
        series_name = input("Enter the series name: ")
        episode_number = input("Enter the episode number: ")
        
        watch_list[movie] = {"genre": genre, "release_date": release_date, "series_name": series_name, "episode_number": episode_number}
    else:
        watch_list[movie] = {"genre": genre, "release_date": release_date}

    print(f"{movie} has been added to your watchlist.")

def edit_movie(watch_list):
    movie = input("Enter the movie/series you want to edit: ")
    if movie in watch_list:
        genre = input(f"Enter the new genre for {movie}: ")
        release_date = input(f"Enter the new release date for {movie}: ")
        series = input(f"Is {movie} part of a series? (Y/N) ").upper()
        if series == "Y":
            series_name = input("Enter the new series name: ")
            episode_number = input("Enter the new episode number: ")

            watch_list[movie] = {"genre": genre, "release_date": release_date, "series_name": series_name, "episode_number": episode_number}
        else:
            watch_list[movie] = {"genre": genre, "release_date": release_date}
        
        print(f"{movie} has been edited.")
    else:
        print(f"{movie} not found on watchlist.")

def remove_movie(watch_list):
    movie = input("Enter the movie/series you want to remove: ")
    if movie in watch_list:
        watch_list.pop(movie)
        print(f"{movie} has been removed from your watchlist.")
    else:
        print(f"{movie} not found on watchlist.")

def print_watchlist(watch_list):
    if watch_list:
        print("Here's your current watchlist:")
        for movie, details in watch_list.items():
            print(f"{movie} ({details['genre']}, {details['release_date']})")
    else:
        print("Your watchlist is empty.")

def sort_by_genre(watch_list):
    genre = input("Enter the genre you want to view: ")
    genre_list = []
    for movie, details in watch_list.items():
        if details["genre"].lower() == genre.lower():
            genre_list.append(movie)
    if genre_list:
        print(f"Here are your movies/series with genre '{genre}':")
        for movie in genre_list:
            print(movie)
    else:
        print(f"No movies or series found with genre '{genre}' in your watchlist.")

def sort_by_release_date(watch_list):
    release_date_list = []
    for movie, details in watch_list.items():
        release_date_list.append((movie, details["release_date"]))
    release_date_list = sorted(release_date_list, key=lambda x: x[1])
    print("Here are your movies and series sorted by release date:")
    for movie in release_date_list:
        print(f"{movie[0]} ({movie[1]})")

def display_watchlist():
    with open("watch_list.json", "r") as f:
        watch_list = json.load(f)
    print("Your Watchlist:")
    print("{:<30} {:<20} {:<10}".format("Movie Name", "Genre", "Release Date"))
    for movie in watch_list:
        print("{:<30} {:<20} {:<10}".format(movie["name"], movie["genre"], movie["release_date"]))

def pick_random_movie():
    with open("watch_list.json", "r") as f:
        watch_list = json.load(f)
    if not watch_list:
        print("Your Watchlist is empty.")
    else:
        random_movie = random.choice(watch_list)
        print(f"Randomly selected movie: {random_movie['name']}")
        print(f"Genre: {random_movie['genre']}")
        print(f"Release Date: {random_movie['release_date']}")

def main():
    with open("watch_list.json", "r") as f:
        watch_list = json.load(f)

    while True:
        print(" __          __    _                                 _            ____   _             _       _     ")
        print(" \ \        / /   | |                               | |          |  _ \ | |           | |     ( )    ")
        print("  \ \  /\  / /___ | |  ___  ___   _ __ ___    ___   | |_  ___    | |_) || |  __ _   __| |  ___|/ ___ ")
        print("   \ \/  \/ // _ \| | / __|/ _ \ | '_ ` _ \  / _ \  | __|/ _ \   |  _ < | | / _` | / _` | / _ \ / __|")
        print("    \  /\  /|  __/| || (__| (_) || | | | | ||  __/  | |_| (_) |  | |_) || || (_| || (_| ||  __/ \__ \ ")
        print("     \/  \/  \___||_| \___|\___/ |_| |_| |_| \___|   \__|\___/   |____/ |_| \__,_| \__,_| \___| |___/")
        print("            __          __     _         _      _  _       _      _______             _              ")
        print("            \ \        / /    | |       | |    | |(_)     | |    |__   __|           | |             ")
        print("             \ \  /\  / /__ _ | |_  ___ | |__  | | _  ___ | |_      | |  ___    ___  | |             ")
        print("              \ \/  \/ // _` || __|/ __|| '_ \ | || |/ __|| __|     | | / _ \  / _ \ | |             ")
        print("               \  /\  /| (_| || |_| (__ | | | || || |\__ \| |_      | || (_) || (_) || | _           ")
        print("                \/  \/  \__,_| \__|\___||_| |_||_||_||___/ \__|     |_| \___/  \___/ |_|(_)          ")
        print("                                                                                                     ")
        print("1. Add movie/series")
        print("2. Edit movie/series")
        print("3. Remove movie/series")
        print("4. Print your watchlist")
        print("5. Sort by genre")
        print("6. Sort by release date")
        print("7. Mark movie as watched")
        print("8. Select a random movie from your watchlist (under construction)")
        print("9. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_movie(watch_list)
        elif choice == "2":
            edit_movie(watch_list)
        elif choice == "3":
            remove_movie(watch_list)
        elif choice == "4":
            print_watchlist(watch_list)
        elif choice == "5":
            sort_by_genre(watch_list)
        elif choice == "6":
            sort_by_release_date(watch_list)
        elif choice == "7":
            watched_movie = input("Enter the movie/series you've watched: ")
            if watched_movie in watch_list:
                with open("watched_movies.txt", "a") as f:
                    f.write(watched_movie + "\n")
                    print(f"{watched_movie} has been added to your watched list.")
                watch_list.pop(watched_movie)
            else:
                print(f"{watched_movie} not found on watchlist.")
        elif choice == "8":
            pick_random_movie()
        elif choice == "9":
            with open("watch_list.json", "w") as f:
                json.dump(watch_list, f)
            print("Thanks for using Blade's Watchlist Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()