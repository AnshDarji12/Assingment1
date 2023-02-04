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


# In[ ]:




