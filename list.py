# print("hello RBS")

cars=['Toyota','Honda','BMW','Merchandise ']

# print(cars)

mix_list=['Honda',2,'true','BMW']
#last element of the list
print(mix_list[-1])

# 2D List or Matrix
'''
1 2 3 4 5

6 7 8 9 10

11 12 13 14 15

'''
# nested Matrix

matrix=[
    [1, 2, 3, 4, 5],
    [6, 7, 'sayem', 9, 10],
    [11, 12, 13, 14, 15]
]

for i in matrix :
    for y in i :
        print(y,end=' ')
    print()

# List Slicing

print(cars[0:2])

#List Iteration by for Loop

for car in cars:
    print(car)

# sum of list numbers
a=[4,5,10,1,10,5]

sum=0
for i in a:
    sum=sum+i
print("Sum is {no}".format(no=sum))

# Adding Item

mix_list.append('Rang Rover')
print(mix_list)

# anotherway to adding item

mix_list+=['Merchandise']
print(mix_list)

mix_list.insert(2,'hyundai')
print(mix_list)

# Deleting item
'''
del mix_list[0:5]
print(mix_list)
'''

carpop=cars.pop()
print(cars,"\n",carpop)

# Remove item by value
numbers=[1,2,3,4,12,121,22]

numbers.remove(121)
print(numbers)

# splitting String into List items

import re

name=" sayem ,Fahim,hassanvai,Boss"
nameList=re.split(',',name)
print(nameList)

# sort

cars.sort()
print(cars)