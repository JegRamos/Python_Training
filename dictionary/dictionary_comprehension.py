# Systax
# { __:__ for __ in __ }

# Minus 5 O'matic
prelim_grades = { "science" : 85, "math" : 90, "p.e." : 65, "english" : 80 }
final_grades = { subject.title() : grade - 5 for subject,grade in prelim_grades.items() }
print(final_grades)

# inter-weaving lists
list1 = [ "A", "B", "C" ]
list2 = [ 1, 2, 3 ]
combo = { list1[i] : list2[i] for i in range(0, len(list1)) }
print(combo)

# Is it odd or even?
numbers = list(range(0, 11))
numbers_with_desc = { number : ("ODD" if number % 2 != 0 else "EVEN") for number in numbers }
print(numbers_with_desc)

# making a dictionary out of a paired list
person = [ ["name", "jared"], ["job", ["musician", "actor"]], ["city", "bern"] ]
dictionary = { key:desc for key,desc in person }
print(dictionary)

# or if you prefer a more vulgar but easier way
dictionary = dict(person)
print(dictionary)

# Okay, these are vowels
vowels = {}.fromkeys("aeiou", "vowel")
print(vowels)

# okay that was stupid
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet = { letter:("VOWEL" if letter in "AEIOU" else "CONSONANT") for letter in letters }
print(alphabet)
