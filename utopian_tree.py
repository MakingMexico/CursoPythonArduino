n = int(input("How many cycles for the tree do you want to test?: "))
height = 1
for i in range(1, n+1):
    if i % 2 == 0:
        height += 1
    else:
        height *= 2

print("The tree height will be of", height, "meters after", n, "cycles.\n")