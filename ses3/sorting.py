

#Create a function that takes a string as a parameter and returns a list.
#The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

vowels = "aeiouyæøåAEIOUYÆØÅ "
def stringInput(string):
    return sorted([char for char in string if char not in vowels])
    
print(stringInput("hejsa med dig"))



list = ["Claus", "Ib", "Per"]
#Sort this list by using the sorted() build in function.
print(sorted(list, reverse=True))

#Sort the list on the lenght of the name.
print(sorted(list, key=len))

#Sort the list based on the last letter in the name.
print(sorted(list, key=lambda e: e[-1]))


list = ["Claus", "Ib", "Per"]
#Sort the list in a way that the names that has an ‘a’ in it should be sorted first (still alphabetically).
print(sorted(list, key=lambda name: ('a' not in name, name)))


#Ex: Text editor plugin simulation
s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'
#Count the number of characters including blank spaces.
print(len(s))

#Count the number of characters excluding blank spaces.
print(len(s.replace(" ", "")))

#Count the number of words.
print(len(s.split(" ")))