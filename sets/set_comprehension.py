# Systax
# { __ for __ in __ }

book_titles = { "a song of fire and ice", "harry potter", "the gifted", "american gods" }
books = { title.title() for title in book_titles }
print(books)

string = "hello world"
all_vowels = ', '.join({ char for char in string if char in "aeiou" })
print(all_vowels)