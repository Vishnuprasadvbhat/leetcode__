"""
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
"""
# s = "racecar"
# t = "carrace"

s = "jar"
t = "jam"

def checkk_anagram(s,t):
    if len(s) != len(t):
        print(False)
    counts ,countt = {}, {}
    for i in s:
           if i in counts:
               counts[i] += 1
           else:
               counts[i] = 1
    for i in t:
           if i in countt:
               countt[i] += 1
           else:
               countt[i] = 1
    if counts == countt:
        print(True)
    else:
        print(False)

checkk_anagram(s,t)
