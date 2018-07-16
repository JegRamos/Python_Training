song1 = {
    "title" : "All The Right Moves",
    "artist" : "One Republic",
    "album" : "Native",
    "minutes" : 3.4,
    "date_added" : "07-08-2009"
}

song2 = {
    "title" : "Conqueror",
    "artist" : "Aurora",
    "album" : "All My Demons Greeting Me As A Friend",
    "minutes" : 4.12,
    "date_added" : "06-05-2017"
}

song3 = {
    "title" : "Viva la Vida",
    "artist" : "Coldplay",
    "album" : "Magic",
    "minutes" : 4.11,
    "date_added" : "06-05-2008"   
}

song3 = {
    "title" : "Welcome To My Life",
    "artist" : "Simple Plan",
    "album" : "No Helmets Just Balls",
    "minutes" : 3.40,
    "date_added" : "06-05-2007"    
}

song4 = {
    "title" : "BBoom BBoom", 
    "artist" : "Momoland",
    "album" : "Kpop",
    "minutes" : 3.59,
    "date_added" : "08-06-2018"
}

songs = [song1, song2, song3, song4]

num_songs = 0
total_minutes = 0
for song in songs :
    num_songs += 1
    total_minutes += song["minutes"]

my_playlist = {
    "title" : "My Jam",
    "creator" : "Jeg Ramos",
    "num_songs" : num_songs,
    "minutes" : total_minutes,
    "songs" : songs
}

for key,desc in my_playlist.items() : 
    if key != "songs" :
        print(f"{key} - {desc}")
    else : 
        print(f"{key}: ")
        for song_detail in desc : 
            print("------------------")
            for key,desc in song_detail.items() :
                print(f"{key} - {desc}")
