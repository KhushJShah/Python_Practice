# Author: Khush Shah(G23239366)
#This repository contains the solutions to the Hackerank Python Practice Module.
#%%[markdown] 
#Q. You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#For Example:
#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2  
#Function Description
#Complete the swap_case function in the editor below.#
#swap_case has the following parameters:
#string s: the string to modify
#Returns
#string: the modified string
#Input Format
#A single line containing a string .
#Constraints
#Sample Input 0
#HackerRank.com presents "Pythonist 2".
#Sample Output 0
#hACKERrANK.COM PRESENTS "pYTHONIST 2".
def swap_case(s):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in s])

    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#%%
'''
In Python, a string can be split on a delimiter.

Example:

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string
Input Format
The one line contains a string consisting of space separated words.

Sample Input

this is a string   
Sample Output

this-is-a-string
'''
def split_and_join(line):
    # write your code here
    line = '-'.join(line.split())
    return line  
     
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)