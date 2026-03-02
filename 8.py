tuple1 = (12,13,14,16,18,20,21,14,18,14)

print("enter the element you want to find repeated or not")
n =int(input())

repeat = lambda num : n==num
l1 =list(filter(repeat,tuple1))
if(len(l1)==0):
    print("not repeted")
else:
    print("repeted")




