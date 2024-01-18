array = [[2,3,4,9], [2,3,5,9], [2,3,6,9], [2,3,7,9], [2,3,8,9], [2,4,5,9], [2,4,6,9], [2,4,7,9], [2,4,8,9]]

sortedArray = sorted(array, key=lambda x: (x[3], x[2], x[1], x[0]))
for arr in sortedArray:
    print(arr)