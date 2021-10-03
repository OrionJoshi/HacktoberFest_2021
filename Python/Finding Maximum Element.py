#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxi(arr):                        #Creating a function named 'Maxi'
    for i in range(len(arr)-1):       #For loop for itterating through each elemet in array
        maxindex=i                    #Declaring a variable named Maxindex
        for j in range(i+1,len(arr)): #For loop for comparing each element with adjacent element
            if arr[j]>arr[i]:         #Comparing the adjacent element
                mxindex=j             #If the adjacant element is greater then shift the maxindex to the index of the adjacent element 
    return arr[maxindex]              #Returning the max-element
arr=[int(x) for x in input().split()] #List comprehension for taking the input
res=maxi(arr)                         #Calling the function which is created 
print(res)                            #printing out the result which was saved in variable called res.

