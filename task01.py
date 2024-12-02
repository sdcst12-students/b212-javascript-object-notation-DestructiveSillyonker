#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json


def findnum(filename):
    return json.loads(open(filename, 'r').read())

print(max(findnum('task01a.txt')))
print(max(findnum('task01b.txt')))
print(max(findnum('task01c.txt')))
