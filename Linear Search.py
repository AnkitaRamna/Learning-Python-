#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Linear Search Algorithm

L2 = [10,20,30,40,50,80,100]
Element = int(input("Enter Element which you want : "))

if Element in L2:
    print("Your Element At Index : ",L2.index(Element))
else:
    print("Sorry ! Element is not Found in List ")
 


# In[15]:


# Linear Search Algorithm

def Linear_Search(arr,element):
    for i in range(0,len(arr)):
        if(arr[i]==element):
            return i
    return -1
        

L2 = [10,20,30,40,50,80,100]
index =0
Elmt = int(input("Enter Element which you want : "))

index = Linear_Search(L2,Elmt)
if (index == -1):
    print("Sorry ! Element is not Found in List ")
else:
    print("Your Element At Index : ",L2.index(Elmt))
    

