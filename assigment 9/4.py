# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
Input= ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
list1=[]
#    - Output: [30.5, 34.25, 27.0, 23.25]
for i in range(len(Input[0])):
    list1.append((Input[0][i]+Input[1][i]+Input[2][i]+Input[3][i])/4)

print(list1)

