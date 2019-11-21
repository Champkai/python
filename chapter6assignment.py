##Chapter 6 assigment
##Question 1
import random

def write():
    object_file = open('random_numbers.txt', 'w')
    how_many = int(input('Enter a number how many random number:'))
    for i in range(how_many):
        number = random.randrange(1, 501)
        number = str(number)
        object_file.write(number)
        object_file.write('\n')
    object_file.close()
write()

print('##########################')
##Question 2
def read():
    object_file = open('random_numbers.txt', 'r')
    total = 0
    count = 0
    for i in object_file: 
        i = i.rstrip('\n')
        i = int(i)
        print(i)
        total += i
        count += 1
    print(total)
    print(count)
    object_file.close()
read()

print('##########################')
##Question 3
def write():
    member = int(input('Enter the number of member: '))
    object_file = open('golf.txt', 'w')
    for i in range(member):
        name = input('Enter a player\'s name: ')
        score = input('Enter his or her score: ')
        object_file.write(name + '\n')
        object_file.write(score + '\n')
    object_file.close()
    return object_file
def read():
    object_file = open('golf.txt', 'r')
    for i in object_file:
        i = i.rstrip('\n')
        print(i)
write()
read()
