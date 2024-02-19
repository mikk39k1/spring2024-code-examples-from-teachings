#Basic way
#f = open('textFiles/bohr.txt', 'r')
#print(f.read())

#With ContextManager
#with open('textFiles/bohr.txt', 'r') as f:
#    print(f.read())

#Write to files Basic
#f = open('textFiles/hello.txt', 'w')
#f.write('Hello')

#Write ot file with Context manager
#with open('textFiles/testContext.txt', 'w') as f:
#    f.write('Hello')


#Write 100 numbers to numbers.dat file
#with open('textFiles/numbers.dat', 'w') as f:
#    for count in range(100 + 1):
#        f. write(str(count) + '\n')


#Read from file and print every even number
with open('textFiles/numbers.dat', 'r') as f:
    for line in f:
        if line.strip().isdigit():
            number = int(line.strip())
            if number % 2 == 0:
                print(number)
 