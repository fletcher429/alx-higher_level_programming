#!/usr/bin/python3
def add(a, b):
	return int(a) + int(b)


a = "School"
b = 5
result = add(a, b)
try:
    print(result)
except Exception as e:
    print(e)
