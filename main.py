# '''
# Creating List
# '''

# #  List items are enclosed in square brackets
# #  Lists are ordered
# #  Lists are mutable
# #  Lists elements do not need to be unique
# #  Elements can be of different data types

# #  empty lists 
# List = []
# # list of intergers
# list= [ 1,2,3 ]
# # list of strings
# list = [ "orange","apple", "pear", "apple", "banana" ]
# # list is mixed with data types
# list = [ 1, "Hello", 5.0 ]

#  ============

''''
list indexing
'''

fruits = [ 'orange', 'apple', 'pear', 'apple','banana' ]
fruits[0]
print(fruits[0]) # output ===> orange
fruits[ 1 ] 
print(fruits[1]) # outut  ===> apple
fruits[ 2 ]
print(fruits[2]) # output ===> pear
fruits[ 3 ]
print(fruits[3]) # output ===> apple
fruits[ 4 ]
print(fruits[4])  # output ====> banana
fruits[ -1 ]
print(fruits[-1]) # output ====> banana
fruits[ -5 ]
print(fruits[-5]) # output ===> orange

''''
Nested Indexing
'''

fruits= [ 'orange', [ 'apple', 'orange' ] ]
fruits[ 1 ][ 0 ]
print(fruits[1][0]) # ==> apple
fruits[ 1 ][ 1 ]
print(fruits[1][1]) # ==> orange

'''
How to slice lists in python
'''
fruits = ['orange', 'apple', 'pear','grapes','banana' ]
# beginning to end
fruits[:]
print(fruits[:]) # output ==> ['orange','apple','pear','grapes','banana']

# index 2 to 5th item
fruits[2:5] 
print(fruits[2:5]) # output ==> ['pear','grapes','banana']

# remove last two items
fruits[:-2] 
print(fruits[:-2]) # output ==> ['orange', 'apple', 'pear']

# return first two items
fruits[:2] 
print(fruits[:2]) # output ==> ['orange','apple']

# index 2 to the end
fruits[2:]
print(fruits[2:]) # output ==> ['pear, 'grapes','banana']

# every 2nth item
fruits[::2]
print(fruits[::2]) # output ==> ['orange','pear','banana']

# reverse list
fruits[::-1]
print(fruits[::-1]) # output ==> ['banana','grapes','pear','apple','orange',]

# ===============

''''
Add element to the list
'''
# changing a list after it is created (mutable)
fruits= ['orange', 'apple', 'pear', 'grapes', 'banana']
# change first item
fruits[0]= 'berries'
print(fruits) # output ==>[ 'berries', 'apple', 'pear', 'grape', 'banana']

# change item in index 1 to 4th item
fruits[1:4] = ['mandarins', 'peaches', 'plums']
print(fruits[1:4]) # output ==> ['orange','mandarins','peaches','plums','banana' ]

# add limes to the end of the list
fruits=['orange','apple','pear','grapes','banana']
fruits.append('Limes')
print(fruits) # output ==> ['orange', 'apple', 'pear', 'grapes', 'banana', 'Limes' ]

#  =====

'''
Remove and Delete list items
'''

fruits= [ 'Orange', 'Apple', 'Pear', 'Grapes', 'Banana']
# delete 0nth index position
# del fruits[0]
# print(fruits)

# delete the items from index position 1 to 5th item
del fruits[1:5] 
print(fruits)

#  ===========

'''
Python list methods
'''

# print(dir(list))
# print(help(list.append))
# print(help(list.insert))

fruits= ['Orange', 'Apple', 'Pear', 'Grapes', 'Banana' ]

fruits.append('cashew')
print(fruits)

#  ======

fruits.insert( 0,'guava' )
print(fruits)

# =======

# fruits=['Orange', 'Apple', 'Pear', 'Grapes','Banana']

# fruits.pop(1)
# print(fruits)
#  ======

# print(fruits.index('Banana'))

#  ========

# pos = fruits.index('Banana')
# fruits.pop(pos)

# print(fruits)

#  ======

fruits= ['orange', 'apple','pear','apple','banana','banana','banana']

# print(fruits.count('banana'))

# result = {}
# for x in fruits:
#     result [ x ] = fruits.count ( x ) 

# print(result)

# ========

# easy way to count by using Counter

from collections import Counter

print(Counter(fruits))

#  ========

'''
List Membership Test
'''

fruits= ['apple', 'pear', 'apple', 'banana' ]
print('apple' in fruits) # output => True












