import datetime
from random import sample
from functions import sorting

n = int(input("Random numbers to sort: "))
random_bubble_numbers = sample(range(1, n+1), n)
random_selection_numbers = random_bubble_numbers
random_insertion_numbers = random_bubble_numbers

initial_time_bubble = datetime.datetime.now()
print("Unsorted:", random_bubble_numbers)
sorting.bubble_sort(random_bubble_numbers)
print("Sorted:", random_bubble_numbers)
final_time_buble = datetime.datetime.now() - initial_time_bubble

initial_time_selection = datetime.datetime.now()
print("Unsorted:", random_selection_numbers)
sorting.selection_sort(random_selection_numbers)
print("Sorted:", random_selection_numbers)
final_time_selection = datetime.datetime.now() - initial_time_selection

initial_time_insertion = datetime.datetime.now()
print("Unsorted:", random_insertion_numbers)
sorting.insertion_sort(random_insertion_numbers)
print("Sorted:", random_insertion_numbers)
final_time_insertion = datetime.datetime.now() - initial_time_insertion

print(
"""TIEMPOS:
Método de burbuja: {}
Método de selección: {}
Método de inserción: {}
""".format(final_time_buble, final_time_selection, final_time_insertion)
)