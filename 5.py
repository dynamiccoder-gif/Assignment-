list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
add=  lambda x,y : x+y
addittion = list(map(add, list1 , list2 ))
print("addition of two list is:", addittion)