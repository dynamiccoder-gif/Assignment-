# Write a Python program to remove an empty tuple(s) from a list of tuples.
Input= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
# Output= [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
k =lambda n:len(n)>0
output= list(filter(k,Input))
print(output)
    
# print(Input)