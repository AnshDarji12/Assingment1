#!/usr/bin/env python
# coding: utf-8

# # Q1. write a program to accept percentage from the user and display the grade according to the following.

# In[5]:


a = int(input("Enter your Marks"))
if a>90:
    print("A")
elif a>80 and a<=90:
    print("B")
elif a >=60 and a<=80:
    print("C")
else:
    print("D")
    


# # Q2. Write a program to accept the cost of a bike and display the road tax to be paid according to the following criteria.

# In[19]:


A =int(input("Enter your Price"))

if A >100000:
    tax=15*100/100
    print(tax)
elif A>50000 and A<=100000:
    tax=10*100/100
    print(tax)
else:
    tax=5*100/100 
    print(tax)
    
rt=A*tax
print(rt,"your price is")


# # Accept any  city from the user and display monuments of that city.

# In[22]:


city = input("Enter the city")
if city.upper() == "DEHLI":
    print("RED FORT")
elif city.pupper() == "AGRA":
    print("TAJ MAHAL")
elif city.upperer() == "JAIPUR":
    print("JAL MAHAL")
else:
    print("Enter valid city")


# # check how many times a given number can be divided  by 3 before it's less then or equal to 10.

# In[42]:


num1=3 
if(num1%3==0):
    print("{} is divisible by 3".format(num1))
else:
    print("{} is not divisible by 3".format(num1))


# # Why and when to use while loop in python give a detail description with example.

# In[43]:


#Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. 
#And when the condition becomes false, the line immediately after the loop in the program is executed.
#While loop falls under the category of indefinite iteration. Indefinite iteration means that the number 
#of times the loop is executed isn’t specified explicitly in advance. 
#Statements represent all the statements indented by the same number of character spaces after a programming 
#construct are considered to be part of a single block of code. Python uses indentation as its method of 
#grouping statements. When a while loop is executed, expr is first evaluated in a Boolean context and if 
#it is true, the loop body is executed. Then the expr is checked again, if it is still true then the body 
#is executed again and this continues until the expression becomes false.


# # Use nested while loop to print 3 different pattern.

# In[44]:


i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    print("")
    i=i+1 


# In[60]:


i=1  
while i<=5:
    j=1
    while j<=i:
        print(j,end="*")
        j=j+1
    print("*")
    i=i+1


# # Reverse a while loop to display numbers 10 to 1.

# In[61]:


i = 10
while i > 0:
    print(i)
    i = i - 1 


# In[4]:





# #  Create a python program to sort the given list of tuples based on integer value using a  lambda function.  
# [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
# 

# In[4]:


subject_marks = [('Sachin Tendulkar',34357 ), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
subject_marks.sort(key = lambda x: x[1])
print(subject_marks)


# # Write a Python Program to find the squares of all the numbers in the given list of integers using  lambda and map functions. 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# 

# In[11]:


x =[1,2,3,4,5,6,7,8,9,10]
a=list(map(lambda x:x**2,x))


# In[12]:


a


# # . Write a python program to convert the given list of integers into a tuple of strings. Use map and  lambda functions 
# Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10') 
# 

# In[13]:


nums_list = [1,2,3,4]
nums_tuple = (0, 1, 2, 3) 
print("Original list and tuple:")
print(nums_list)
print(nums_tuple)
result_list = list(map(str,nums_list))
result_tuple = tuple(map(str,nums_tuple))
print("\nList of strings:")
print(result_list)
print("\nTuple of strings:")
print(result_tuple)


# # Write a python program using reduce function to compute the product of a list containing numbers  from 1 to 25.

# In[17]:



import functools


lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))


# In[19]:


#Q5


# In[18]:



import numpy as np
# Initialisation of list
lis1 = np.array([1, 2, 3, 4, 5])

# Using numpy method
is_even = lis1[lis1 % 2 == 0]


# Printing output
print(is_even)


# # Write a python program to find palindromes in the given list of strings using lambda and filter  function. 
# ['python', 'php', 'aba', 'radar', 'level'] 
# 

# In[20]:


texts = ["php", "aba", "Python", "radar", "level"]
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
print("\nList of palindromes:")
print(result) 


# In[ ]:




