import pprint

pp = pprint.PrettyPrinter(indent=4)


def calculate_max_sum(triangle):
    # Copy the last row of the triangle
    max_sum = list(triangle[-1])

    # Iterate from the second last row up to the first row
    for row in range(len(triangle) - 2, -1, -1):
        # For each element in the current row, add the maximum of the two possible values in the next row
        for i in range(len(triangle[row])):
            max_sum[i] = triangle[row][i] + max(max_sum[i], max_sum[i + 1])

    # The first element of max_sum now contains the maximum sum
    return max_sum[0]


triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]

print("Solution is: " + str(calculate_max_sum(triangle)))
