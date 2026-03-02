list=[]
size =int(input("enter teh size of the list :"))
for i in range(size):
        print("enter the 1st : ", end="")
        list.append(int(input()))
def histogram(list):
    
    for n in list:
        for k in range(n):
            print("*", end="")
        print('\n')
histogram(list)
        