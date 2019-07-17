"""Selection Sort."""
from random import sample

def selection_sort(u):
    """Selection Sort."""
    for i in range(len(u)-1):
        minimum_value = u[i]
        minimum_postion = i
        for j in range(i+1, len(u)):
            if u[j] < minimum_value:
                minimum_value = u[j]
                minimum_postion = j
        u[i], u[minimum_postion] = u[minimum_postion], u[i]

n = int(input("Random numbers to sort: "))
random_numbers = sample(range(1, n+1), n)
print("Unsorted:", random_numbers)
selection_sort(random_numbers)
print("Sorted:", random_numbers)