#4collections.py

# 4.1 PYTHON Lists

fruits = ["kiwi", "pineapple", "apple"]

# 4.1.1 Print the second item in the fruits list.
# TODO: Write your code below
print('Second item in the list : ', fruits[1])


# 4.1.2 Change the value from "kiwi" to "orange", in the fruits list.
# TODO: Write your code below
fruits[0] = "orange"
print('uploaded fruits list :', fruits)


# 4.1.3 Use the insert method to add "lemon" as the second item in the fruits list.
# TODO: Write your code below
fruits.insert(1,'lemon')
print('updated fruits list after inserting lemon :',fruits)


# 4.1.4 Use the remove method to remove "pineapple" from the fruits list.
# TODO: Write your code below
fruits.remove('pineapple')
print('pineapple removed from list :', fruits)

# 4.1.5 Use negative indexing to print the last item in the list.
# TODO: Write your code below
print('last item in fruits :', fruits[-1])

# 4.1.6 Use a range of indexes to print the third, fourth, and fifth item in the list fruits2.

fruits2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# TODO: Write your code below
print('third, fourth and fifth items in fruits2 list',fruits2[2:5])

# 4.1.7 Use the correct syntax to print the number of items in the list fruits
# TODO: Write your code below
print('item count in fruits', len(fruits))


# 4.1.8  Write a program that add the average of numbers in a list scores.
# you are not allowed to use the sum() or len() functions.

scores = [50, 55, 56, 70, 80, 60, 66]
length=0
total=0
for x in scores:
    #TOTAL=TOTAL+X
    total+=x
    #LENGTH=LENGTH+1
    length+=1

print('sum of items :', total)
print('item count', length)
print('average of items in the scores list', total/length)
print('average of items in the scores list', round(total/length,5) )
# TODO: Write your code below


# 4.1.9 Write a program that calculates the highest number in a list scores
# you are not allowed to use the max or min functions.
scores = [50, 55, 56, 70, 80, 60, 66]

# TODO: Write your code below
highest_score = scores[0]

highest_score = scores[0]
    for score in scores:
        if score > highest_score:
            highest_score = score

print("Highest score:", highest_score)

# 4.1.10






# 4.2. PYTHON Dictionaries

car =	{
  "brand": "Renault",
  "model": "Clio",
  "year": 2018
}

# 4.2.1 Use the get method to print the value of the "model" key of the car dictionary.
# TODO: Write your code below
print('value for model in car dictionnary:', car.get('model'))
print('value for model in car dictionnary:', car['model'])


# 4.2.2 Change the "year" value from 2018 to 2020 in the car dictionary.
# TODO: Write your code below
car['year'] = 2020
print('updated value of year in car dictionnary:', car['year'])


# 4.2.3 TODO: Add the key/value pair "color" : "blue" to the car dictionary.
# TODO: Write your code below
car['color']='blue'
print('updated dictionnary car', car)


# 4.2.4 Use the pop method to remove "model" from the car dictionary.
# TODO: Write your code below
car.pop('model')
print('model removed from car dict : ',car)


# 4.2.5 Use the clear method to empty the car dictionary.
# TODO: Write your code below
car.clear()
print('cleared car dict:', car)
