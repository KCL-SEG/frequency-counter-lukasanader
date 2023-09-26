"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        item=str(item)
        if item in frequencies:
            frequencies[item]=frequencies.get(item)+1
        else:
            frequencies[item]=1
    return frequencies

