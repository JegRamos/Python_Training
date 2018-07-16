# Works with any iterable value but does not change the original list/tuple
t = ( 3, 4, 5, 7 )
s = [ 3, 7, 2, 9, 5 ]
print(sorted(s)) # regular 
print(sorted(s, reverse = True)) # reverse

# sort dictionaries
users = [ 
    { "username" : "jegramos", "age" : 21, "city" : "pasay" },
    { "username" : "sarahopena", "age" : 21, "city" : "taguig" },
    { "username" : "jona", "age" : 27, "city" : "taguig" },
 ]

sorted_users = sorted(users, key = lambda user : user["username"])
print(sorted_users)

fb_users = [
    { "username" : "jegramos", "posts" : ["Hi", "langya naman this", "like and share"] },
    { "username" : "sarahopena", "posts" : ["Hi", "langya naman this"] },
    { "username" : "jona", "posts" : [] }    
]

sorted_fb_users = sorted(fb_users, key = lambda fb_user : len(fb_user["posts"]), reverse = True) # sort users from most active to least active
extracted_username_sorted_fb_users = [ user["username"] for user in sorted_fb_users ] # only get the username
print("Users ordered from most active to least active: ")
for user in extracted_username_sorted_fb_users : # print all of them
    print(user)

songs = [
    { "title" : "Murder Song", "play_count" : 20 },
    { "title" : "Hayaan Mo Sila", "play_count" : 1 },
    { "title" : "Don't Look Back in Anger", "play_count" : 30 },
    { "title" : "Counting Stars", "play_count" : 18 },
]
    
songs_by_popularity = sorted(songs, key = lambda song : song["play_count"], reverse = True) # sort by play_count
bill_board_chart = [ song["title"] for song in songs_by_popularity ]

print("TOP SONGS: ")
i = 0
while i < len(bill_board_chart) : 
    print(f"{i + 1} {bill_board_chart[i]}")
    i += 1

# max - Can take any iterable
print(max(98, 55, 100))
print(max("a", "h", "b", "x", "X"))
nums = [88, 10, 52, 90]
print(max(nums))
# min
print(min(nums))

names = [ "Arya", "Ned", "Jon", "Sansa", "Rob" ] # who has the longest name?
print(max( names, key = lambda names : len(names) ))

# find out the song that has the lowest play_count 
print("Most unpopular song is: ")
most_unpopular_song = min(songs, key = lambda song : song["play_count"])["title"]
print(most_unpopular_song)

# sort songs by least popular
unpopular_songs = sorted(songs, key = lambda song : song["play_count"])
unpopular_songs = [ song["title"] for song in unpopular_songs ]
print(unpopular_songs)