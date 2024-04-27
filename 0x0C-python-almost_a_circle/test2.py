x = 2
y = 4
width = 5
height = 3


for i in range(height):
    if i < y:
        print("" * width)
    else:
        print(" " * x + "#" * width)