
to_be = True

if to_be:
    print('I am alive')

if not to_be:
    print('I am dead')
else:
    print('I am not dead')

participants = ['the_late_one', 'what_is_i', 'filip']
teacher = 'filip'

if participants[0] is teacher:
    print('Hello the_late_one')
elif participants[1] == teacher:
    print('Hello teacher what_is_i')
elif participants[2] is teacher:
    print('Hello teacher filip')
else:
    print('No teacher')

for i in range(3):
    if participants[i] == teacher:
        print('Hello', participants[i])

for student in participants:
    # print(student)
    if student is teacher:
        print('Hello my teacher', student)

# Adding values
animals = ['dog', 'bird', 'cat']
print(animals)

animals.append('monkey')
print(animals)

animals2 = ['elephant', 'pikachu', 'snake']

animals.extend(animals2)
print(animals)

print(animals[1])

print('Length of our list', len(animals))

print('Index of pikachu:', animals.index('pikachu'))

numbers = [1, 3, 4, 7, 3, 9, 0]

print('Count of 3 in numbers:', numbers.count(3))

food = ['chips', 'franke', 'soup', 'pizza']  # Rodzynkowa 2

# len(food) to 4
# len(food) - 1 to 3
# food[3] to 'pizza'

print(food[len(food) - 1])
print(food[-1])
print(food[-2])

print(food[1:])
print(food[0:3])

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

# removing items

numbers.remove(4)
print(numbers)

numbers.pop(0)
print(numbers)

numbers.clear()
print(numbers)

