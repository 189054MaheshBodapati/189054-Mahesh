import string
from collections import Counter
from itertools import permutations
# get span
def getspan(s,ss):
    start=s.index(ss)
    end=start+len(ss)-1
    return(start,end)
# Reverse words 
def reverseWords(s):
    words=s.split()
    return ' '.join(words[::-1])
# Removing punctuations in string
def removePunctuations(s):
    return''.join(char for char in s if char not in string.punctuation)
# count words
def countWords(s):
    words=s.split()
    return len(words)
#charcter map
def characterMap(s):
    return dict(Counter(s))
#Make Title
def makeTitle(s):
    return s.title()
# Normalization spaces in the string
def normalizeSpaces(s):
    return ' '.join(s.split())
# Trans forms 
def transform(s):
    return s[::-1].swapcase()
# get all the permutations of the string
def getPermutations(s):
    return [' '.join(p) for p in permutations(s)]
