# Ifs && lists

## if

Basic usage for example checking value of variable

```python
to_be = True
if to_be:
	print('I am alive')

to_be = False
if to_be:
	print('I am dead')
```

<br />

Something harder, reversing the output value. Changing **True &#8594; False** or **False &#8594; True**

```python
to_be = True

if not to_be:
	print('I am not alive')
```

<br />

Doing something if value is **True** and something else if it is **False**

```python
studen_present = True

if studen_present:
	print('Very good')
else:
	print('Bad student')
```

<br />

Now some real useage of **if** which is comparing staff

```python
participants = ['the_late_one', 'what_is_i', 'filip']
teacher = 'filip'

if participants[0] is teacher:
	print('Hello teacher the_late_one')

elif participants[1] is teacher:
	print('Hello teacher what_is_i')

elif participants[2] is teacher:
	print('Hello teacher filip')
```

<br />

## List

### **Adding values**

Add item to a list

```python
animals = ['dog', 'bird', 'cat']

animals.append('monkey')

print(animals)  # ['dog', 'bird', 'cat', 'monkey']
```

<br />

Joining two lists

```python
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8]

list1.extend(list2)

print(list1)  # [1, 3, 5, 7, 9, 2, 4, 6, 8]
```

<br />

### **Reading values**

Length of the list

```python
numbers = [1, 3, 4, 7, 3]

print(len(numbers))  # 5
```

<br />

Getting the position of our value

```python
animals = ['dog', 'bird', 'cat', 'monkey']

print(animals.index('bird'))  # 1
```

<br />

Counting how many times something appears in list

```python
numbers = [1, 3, 4, 7, 3]

print(numbers.count(3))  # 2
```

<br />

Reading more than one valeu

```python
numbers = [1, 3, 4, 7, 3]

print(numbers[-1])  # 3
print(numbers[1:])  # [3, 4, 7, 3]
print(numbers[:])  # [1, 3, 4, 7, 3]
```

<br />

Copying hole list

```python
numbers = [1, 3, 4, 7, 3]

numbers_copy = numbers.copy()
print(numbers_copy)
```

<br />

Sorting list

```python
numbers = [1, 3, 4, 7, 3]

prime_numbers.sort()
print(prime_numbers) #  [1, 3, 3, 4, 7]
```

<br />

### **Removing values**

Remove certain item

```python
numbers = [1, 3, 4, 7, 3]

numbers.remove(4)

print(numbers)  # [1, 3, 7, 3]
```

<br />

Remove item from certain position

```python
numbers = [1, 3, 4, 7, 3]

numbers.pop(1)

print(numbers)  # [1, 4, 7, 3]
```

<br />

Remove everything

```python
numbers = [1, 3, 4, 7, 3]

numbers.clear()

print(numbers)  # []
```

<br />
