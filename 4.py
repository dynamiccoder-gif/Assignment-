numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))
sum=0
print("odd numbers are:", odd_numbers)
def sumofsquare(n):
    global sum
    sum=sum+(n*n)
list(map(sumofsquare,odd_numbers))
print("sum of square :", sum)
