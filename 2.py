numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), numbers))


print("Original list:", numbers)
print("Numbers divisible by 19 or 13:", result)