#!/usr/bin/env python
# coding: utf-8

# In[2]:


weight = int(input("Enter your weight in pounds: "))


# In[3]:


height = int(input("Enter your weight in inches: "))


# In[5]:


BMI = (weight * 703) / (height**2)

print(BMI)


# In[6]:


name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your weight in inches: "))

BMI = (weight * 703) / (height**2)

print(BMI)

if BMI > 0:
    if(BMI < 18.5):
        print(name + ",you are underweight.")
    elif (BMI <= 24.9):
        print(name + ", you are normal weight.")
    elif (BMI <= 29.9):
        print(name + ", you are overweight.")
    elif (BMI <= 34.9):
        print(name + ", you are obese.")
    elif (BMI <= 39.9):
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese.")
else:
    print("Enter valid input")


# In[ ]:




