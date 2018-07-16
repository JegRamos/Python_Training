# lambdas
add = lambda a, b : a + b
print(add(5, 10))

say_hello = lambda word : word 
print(say_hello("Hi!"))

# map
people = [ "jeg", "sarah", "jona", "virgie", "shirley" ]
PEOPLE = list(map(lambda name : name.upper(), people )) # map will take a lambda or fn and a iterable
print(PEOPLE)

square = list(map(lambda num : num * 2, range(1, 11)))
print(square)

names = [
    {"first_name" : "jeg", "last_name" : "ramos"},
    {"first_name" : "sarah", "last_name" : "opena"},
    {"first_name" : "jona", "last_name" : "padios"},
    {"first_name" : "rommy", "last_name" : "historillo"},
]

first_names = list(map(lambda name : name["first_name"], names))
print(first_names)

first_names = [ name["first_name"] for name in names ] # list comprehension equivalent
print(first_names)

# filter
numbers = list(range(1, 11))
evens = list(filter(lambda num : num % 2 == 0, numbers))
print(evens)

names = ["Jeg", "Mark", "Apple", "Mary", "Austin", "axel", "alyssa"]
starts_with_a = list(filter(lambda name : name[0].lower() == "a", names))
print(starts_with_a)

# reach out to people who don't tweet
users = [
    { "username" : "jeg", "tweets" : ["I love cats", "I hate trump"] }, 
    { "username" : "sarah", "tweets" : [] },
    { "username" : "jona", "tweets" : ["Punta ako ng NTC"] },
    { "username" : "rein", "tweets" : ["Hello guys", "kumain na kayo?"] },
    { "username" : "gie", "tweets" : [] }
]

no_tweet_users = list(filter(lambda user : user["tweets"] == [], users))
print(no_tweet_users)
for user in no_tweet_users : 
    print(f"Hi there {user['username']}, I noticed you haven't been tweeting. Please tweet, thanks")

# using list comprehension. This is recommended.
no_tweet_users = [ user for user in users if user["tweets"] == [] ]
print(no_tweet_users)
for user in no_tweet_users : 
    print(f"Hi there {user['username']}, I noticed you haven't been tweeting. Please tweet, thanks")
    