#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to calculate the length of a string

def lenOfString(string):
    return len(string) 

print(lenOfString(input("Enter a string: ")))


# In[2]:


#Write a Python program to count the number of characters in a string. 

def characterCount(uniqueChar):
    charCount = {}
    for i in uniqueChar:
        charCount[i]= updatedString.count(i)
    return charCount
    
updatedString = input("Enter a string: ").lower()
uniqueChar = set(updatedString)
print(characterCount(uniqueChar))


# In[3]:


#Write a Python program to sum all the items in a list. 

def sumOfItems(items):  
    sum_numbers = 0  
    for x in range(len(items)):  
        sum_numbers += int(items[x])  
    return sum_numbers  

noOfItems = input("Enter no. of items: ")
listOfItems = []
for i in range(int(noOfItems)):
    listOfItems.append(input())
print(sumOfItems(listOfItems))


# In[4]:


#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def replaceOccurances(list1):
    firstChar = string[0]
    for i in range(1, len(string)):
        if string[i] == firstChar:
            string[i] = '$'
    return "".join(string)

string = list(input("Enter the string: ").lower())
print(replaceOccurances(string).capitalize())


# In[5]:


#Write a Python program to concatenate following dictionaries to create a new one.

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {**dict1, **dict2, **dict3}
print(dict4)


# In[6]:


#Write a Python program to check whether an element exists within a tuple.

tuple1 = ("1","2","3","abc",)
print("H" in tuple1)
print("2" in tuple1)


# In[7]:


#Write a Python program to find maximum and the minimum value in a set. 

value = set([2,4,6,8,10])
print(max(value))
print(min(value))


# In[9]:


#Write a program with python which could accept two parameter a and b to calculate and output the result of S, where
 #𝑆=3.14∗(1+𝑎/𝑏)3 S=3.14∗(1+a/b)3 

def s(a,b):
    if b == 0:
        return "Runtime Error: Attempt to divide by zero"
    exp = 1 + (a/b)
    return 3.14 * (1 + a/b)**3
parameter_a = int(input("Please enter a value for a : "))
parameter_b = int(input("Please enter a value for b : "))
print(" result: ", s(parameter_a, parameter_b))
    


# In[ ]:


#Write a Python program to randomly divide the students in this class into five groups for term projects, each group should have at least 3 students but no more than 5 students (including 5). Here is the students list:


