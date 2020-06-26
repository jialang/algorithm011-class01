'''
Not sure what the questions are asking for
To append left or right, use a list is easy

'''
from collections import deque

def add_left(val, q):
    s = [val] + list(q)
    return deque(s)

def add_last(val, q):
    s = list(q) + [val]
    return deque(s)
