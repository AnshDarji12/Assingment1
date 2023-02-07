#!/usr/bin/env python
# coding: utf-8

# In[8]:


""""Create a function which will take a list as an argument and return the product of all the numbers
after creating a flat list.
Use the below-given list as an argument for your function.
list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']"""


# In[11]:


from collections.abc import Iterable
def product_of_numbers(lst):
    flat_list = []
    def flatten(l):
        for el in l:
            if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
                flatten(el)
            else:
                flat_list.append(el)
    flatten(lst)
    product = 1
    for i in flat_list:
        if type(i) == int or type(i) == float:
            product *= i
    return product

list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
print(product_of_numbers)


# # Q2.

# In[12]:


def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            char = chr(ord(char) - 1)
        elif char == " ":
            char = "$"
        encrypted_message += char
    return encrypted_message

input_sentence = "I want to become a Data Scientist."
print(encrypt_message(input_sentence))


# In[ ]:





# 

# In[ ]:





# 

# In[ ]:





# In[ ]:




