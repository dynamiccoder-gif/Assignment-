lists=['apple', 'banana', 'cherry', 'rohit kumar', 'rohit baghel','aditiya pandit', 'siddthan rana', 'ashwini kumar']
max_number = lambda n : len(n)
maximum =0
max_number= list(map(max_number, lists))
print(max_number)
def max(n):
    global maximum
   
    if(n>maximum):
        maximum=n
        
        return True
        
    else:
        return True
        
list(filter(max, max_number))
print("maximum is of length:", maximum)