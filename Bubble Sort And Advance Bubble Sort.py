#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Bubble Sort using Python 

size = int(input("Enter The Size Of Array : "))
L1=[]
temp=0

print("Enter Element of Array : ")
for i in range(0,size):
    L1.append(int(input()))
    
for i in range(0,size-1):
    for j in range(0,size-i-1):
        if(L1[j]>L1[j+1]):
            temp=L1[j]
            L1[j]=L1[j+1]
            L1[j+1]=temp
print("After Sort Using Bubble Sort : ",L1)


# In[6]:


# Advance Bubble Sort using Python 

size = int(input("Enter The Size Of Array : "))
L1=[]
temp=0
count=0

print("Enter Element of Array : ")
for i in range(0,size):
    L1.append(int(input()))
    
for i in range(0,size-1):
    for j in range(0,size-i-1):
        if(L1[j]>L1[j+1]):
            temp=L1[j]
            L1[j]=L1[j+1]
            L1[j+1]=temp
            count+=1
    if(count==0):
        break;
            
print("After Sort Using Bubble Sort : ",L1)


# In[ ]:




