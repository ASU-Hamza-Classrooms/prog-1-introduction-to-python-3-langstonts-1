#!/bin/python3

#import the code in string1.py

from stringlib import *
from worker import *
import sys

#Function to test the functions in the stringlib module
def testStringLib(inputStr):
    #Add code to call each of the functions and print the results
    print('\nInput string is ' + inputStr)
    print('\nReverse of string is ' + reverseStr(inputStr))
    print('\nDoes string contain apple? ' + containsWord(inputStr, 'apple'))
    print('\nDoes string contain banana? ' + containsWord(inputStr, 'banana'))
    print('\nIs string a palindrome? ' + isPalindrome(inputStr))
    print('\nUppercase of string is ' + upperCaseStr(inputStr))
    return

#Function to test the methods in the Worker class in the worker module
def testWorkerClass(inputStr):
    #Add code to create a Worker object
    #Use the object to call each of the methods in the Worker class
    #Print the result of each call
    x = Worker(inputStr)
    print('\nInput string is ' + inputStr)
    print('\nReverse of string is ' + x.reverseStr())
    print('\nDoes string contain apple? ' + x.containsWord("apple"))
    print('\nDoes string contain banana? ' + x.containsWord("banana"))
    print('\nIs string a palindrome? ' + x.isPalindrome())
    print('\nUppercase of string is ' + x.upperCaseStr())
    return

#check to make sure there is a string command line argument
if (len(sys.argv) < 2):
    print("usage: driver1.py <string>")
else:
    #call the functions that test the library and the Worker class
    print("\nTest stringlib:")
    testStringLib(sys.argv[1])
    print("\nTest Worker class:")
    testWorkerClass(sys.argv[1])




