def display_app_title():
    from pyfiglet import figlet_format
    from termcolor import colored

    app_name = "DAD JOKES 3000"
    app_name = figlet_format(app_name)
    app_name = colored(app_name, "green")
    print(app_name)

def get_dadjokes(search_item):
    import requests
    url = "https://icanhazdadjoke.com/search"

    response = requests.get(
        url,
        headers={"Accept" : "application/json"},
        params={"term" : {search_item}}
    )
    joke_data = response.json()
    return joke_data["results"]

def start_app():
    from random import randint

    exit_app = False
    while not exit_app:
        display_app_title()

        search_item = input("Search for a kool joke: ")
        joke_results = get_dadjokes(search_item)
        num_jokes = len(joke_results)

        while num_jokes == 0:
            search_item = input(f"I couldn't any jokes about {search_item}, try again: ")
            joke_results = get_dadjokes(search_item)
            num_jokes = len(joke_results)

        if num_jokes > 1:
            print(f"Okay, I found {num_jokes} jokes about {search_item}, here's one: ")
            random_joke = joke_results[randint(0, num_jokes - 1)]["joke"] #* we can also use chioce() from random module
            print(random_joke)
        elif num_jokes == 1:
            print(f"I found 1 kool joke about {search_item}, here it is: ")
            print(joke_results[0]["joke"])

        try_again = input("hek hek hek vey funny, search again? [y/n]: ").lower()
        while try_again != "y" and try_again != "n":
            try_again = input("Invalid input [y/n]: ").lower()
        if try_again == "n":
            exit_app = True

start_app()

