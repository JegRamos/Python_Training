students =  { 
    201312416 : "Jeg Ramos",
    201312455 : "Carlo Ramos",
    201356699 : "Ramirez",
    666666666 : "Totally not Satan"
}

# copy method
students_copy = students.copy()
print(students_copy)

# The clear method
students.clear()
print(students)

#fromkeys method
word_1 = {}.fromkeys(["Strong"], ["Definition 1", "Definition 2", "Definition 3"]) # pass an iterable key then seperated with a comma, pass in the value
print(word_1)

new_user = {}.fromkeys(["name", "age", "sex", "bio"], "unknown")
print(new_user)

game_properties = [
    "ammo",
    "money",
    "grenades",
    "gold",
    "melee weapon"
]

initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)

# get method
songs = {}.fromkeys(["Don't look back in anger", "Wonder Wall", "Champagne Supernova"], "Oasis")
oasis_song = songs.get("Champagne Supernova") # you can only pass a key
print(oasis_song)

# pop method
nba_players = {
    24 : "Kobe Brayant",
    6 : "Lebron James",
    23 : "Michael Jordan",
    30 : "Steph Curry"
}

goat = nba_players.pop(23)
print(goat)
print(nba_players)

# popitem - remove an item randomly. It takes no parameters
sgoat = nba_players.popitem()
print(sgoat)

# update method
programming_languages = {
    "Python" : "The best!",
    "Java" : "Verbose, I like it",
    "C#" : "Uhmm... Java?", 
    "Php" : "Me no likey"
}

frontend_languages = {
    "Javascript" : "I understand it is very famous",
    "Html" : "Ah yes, were it all started",
    "Css" : "Where will we'd be without you"
}

programming_languages.update(frontend_languages)
for language,comment in programming_languages.items() : 
    print(f"{language} - {comment}")