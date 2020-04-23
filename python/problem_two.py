import numpy as np

# represent clear and rainy ratio of business for large store in matrices
clear_matrix = np.array([[.5, .9], [.1, .6],])
rain_matrix  = np.array([[.5, .1], [.9, .8],])

# combine matricies knowing it rains 60% of the time
total_matrix = (0.6 * clear_matrix) + (0.4 * rain_matrix)

# find the minimax
minimax = max([min(total_matrix[0]), min(total_matrix[1])])
# find the maximin
maximin = min([max(total_matrix.transpose()[0]),
               max(total_matrix.transpose()[1])])

if minimax == maximin: # True if saddle value exists
    print(f"A saddle point exists with a value of {minimax}")
    print(f"Each store's most optimal choice is to choose "
          f"their respective row/col which includes the saddle value.")
    print(f"Therefore both business should always have the sidewalk sale")

