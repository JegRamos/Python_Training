# Sorting with lambdas

songs = [
    {"title" : "One Day", "genre" : ["pop", "blues", "rock"], "favorites" : 55},
    {"title" : "21 Guns", "genre" : ["rock", "pop"],  "favorites" : 40},
    {"title" : "Fright", "genre" : ["pop"],  "favorites" : 88}
]

#? Sort songs via favorites
sorted_songs = sorted(songs, key = lambda songs: songs["favorites"], reverse = True)
for song in sorted_songs:
    print(f"Title: {song['title']} - Favorites: {song['favorites']}")

#? Sort via number of genres
sorted_songs = sorted(songs, key = lambda song: len(song["genre"]), reverse = True)
for song in sorted_songs:
    print(f"Title: {song['title']} - Genres: {song['genre']}")

#? Who has the longest name?
names = {"Jego Carlo", "Sarah May", "Jonathan", "Virgie"}
longest_name = max(names, key = lambda n: len(n))
print(longest_name)

#? Most favorite song
favorite_song = max(songs, key = lambda song: song["favorites"])["title"]
print(favorite_song)