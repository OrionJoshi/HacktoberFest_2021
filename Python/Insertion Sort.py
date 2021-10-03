#!/usr/bin/env python
# coding: utf-8

# In[1]:


def insertion_sort(arr):                 #Creating a Function named 'Insertion Sort'
    for ele in range(len(arr)):          #For loop for itterating through each element
        j=ele-1                          #Declaring j as i-1
        temp=arr[ele]                    #Declaring a variable named Temp which stores the ith element
        while j>=0 and arr[j]>temp:      #Two basic condition 
            arr[j+1]=arr[j]              #If my preceeding element is greater than ith then shifting the terms to their right place
            j=j-1                        #Decrementing J
        arr[j+1]=temp                    #After shifting the maximum , now placing the smaller term to the right position
arr=[int(x) for x in input().split()]    #List comprehension for taking the input
insertion_sort(arr)                      #Calling the function 
print(arr)                               #As we know that array are mutable so calling the same array

