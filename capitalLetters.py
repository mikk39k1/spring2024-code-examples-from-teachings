#print([chr(char) for char in range(ord('A'),ord('Z') + 1) if char not in range(ord('F'),ord('O') + 1, 2)])


#colors = ['Black', 'White']
#sizes = ['s', 'm' , 'l', 'xl']
#sold_out = [('Black','m'), ('White','s')]

#print([(color, size) for color in colors for size in sizes if (color,size) not in sold_out])

even_numbers = [i for i in range(0,21, 2)]
square_numbers = [i**2 for i in range (0,11)]
list_of_vowels = 'aeiouyæøåAEIOUYÆØÅ'
def getVowelsFromString(string):
    return [char for char in string if char in list_of_vowels]


print(getVowelsFromString("alexander"))
print(even_numbers)
print(square_numbers)