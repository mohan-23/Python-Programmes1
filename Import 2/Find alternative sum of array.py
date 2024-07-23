array = [2,7,9,3,1]

summation = [0, 0]
for i in range(len(array)):
    if i % 2:
        summation[1] += array[i]
    else:
        summation[0] += array[i]

print(f'sum of even and odd indices', summation)