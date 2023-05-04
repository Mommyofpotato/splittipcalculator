#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


print("Welcome to the tip calculator")


# In[3]:


total=input("What was the total bill?")


# In[7]:


total=float(total)


# In[8]:


people=input("How many people are splitting the bill?")


# In[9]:


people=int(people)


# In[11]:


split=total/people


# In[13]:


tip=input("How much would you like to tip?\n Press A for 15%, Press B for 18%, Press C for 20% and press D for 25%")


# In[17]:


tip=tip.lower()


# In[29]:


if tip=='a':
    pay=split*.15
    pay=pay+split
elif tip=='b':
    pay=split*.18
    pay=pay+split 
elif tip=='c':
    pay=split*.20
    pay=pay+split
else:
    pay=split*.25
    pay=pay+split
pay=round(pay,2)


# In[30]:


print("Everyone in your party should pay:",pay)


# In[ ]:




