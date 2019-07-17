def bubble_sort(u):
    keep_sorting = True
    iteration_length = len(u)-1
    while keep_sorting:
        keep_sorting = False
        for i in range(iteration_length):
            if u[i] > u[i+1]:
                keep_sorting = True
                u[i], u[i+1] = u[i+1], u[i]
        iteration_length -= 1
    return u

def selection_sort(u):
    """Selection Sort."""
    for i in range(len(u)-1):
        minimum_value = u[i]
        for j in range(i+1, len(u)):
            if u[j] < minimum_value:
                minimum_value = u[j]
                u[i], u[j] = u[j], u[i]

def insertion_sort(u):
    """Insertion Sort."""
    for i in range(1, len(u)):
        temporal_value = u[i]
        index = i
        while index > 0 and temporal_value < u[index - 1]:
            u[index] = u[index - 1]
            index -= 1
        u[index] = temporal_value
