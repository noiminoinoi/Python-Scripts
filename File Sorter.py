#!/usr/bin/env python
# coding: utf-8

# In[32]:


import os, shutil


# In[33]:


path = r"C:/Users/Noemie/Desktop/Data Analyst Portfolio/Python Project/"


# In[34]:


file = os.listdir(path)


# In[35]:


folder_names = ['pdf files', 'image files', 'text files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
    
for file in file_name:
    if ".pdf" in file and not os.path.exists(path + 'pdf files/' + file):
        shutil.move(path + file, path + 'pdf files/' + file)
    elif ".png" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)
    elif ".jpg" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)    
    elif ".docx" in file and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file, path + 'text files/' + file)


# In[37]:


os.listdir(path)


# In[15]:





# In[31]:





# In[ ]:





# In[ ]:




