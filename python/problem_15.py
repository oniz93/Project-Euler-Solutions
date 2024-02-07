import math


# We have a 20x20 matrix. So position starts with [0,0] and ends with [20,20]
# We can find paths only going down or right so if x,y are the positions we can do only x+1 or y+1
# Starting from [0,0] i'll make a list of lists for each path
def find_path(x, y):
    max_grid = 20
    if x == max_grid and y == max_grid:
        global count_paths
        count_paths = count_paths + 1
        return 1
    if x + 1 <= max_grid:
        find_path(x + 1, y)
    if y + 1 <= max_grid:
        tmp = find_path(x, y + 1)
    return 1


count_paths = 0


# This way unluckly isn't good for big matrixes where "big" is over 10x10


# Math way, given a nxn grid
# The formula is (2n)! / n! / n!
def find_path_math(n):
    n_fact = math.factorial(n)
    return math.factorial(2 * n) / n_fact / n_fact


print("Solution is: " + str(find_path_math(20)))
