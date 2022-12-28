#!/usr/bin/env python
# coding: utf-8

# # Write a Python function to sum all the numbers in a list.

# In[1]:


sample_list=[8,2,3,0,7]
sum=0
for i in sample_list:
    sum=sum+i
print("Expected output:",sum)


# # Write a Python program to reverse a string.

# In[2]:


string=input("Enter string:")
print("Expected output:",string[::-1])


# # Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# In[4]:


s=input("sample string:")
u=0
l=0
for i in s:
    if i.isupper():
        u=u+1

    elif i.islower():
        l=l+1
print("No. of Upper case characters :", u)
print("No. of Lower case Characters :",l)


# In[ ]:




