list1 = [1,2,3,4,5,6,7,8,9]
list2 =(10,20,30,40,50,60,70,80,90)

list_to_string = lambda n: str(n)
string_list1 = list(map(list_to_string, list1))
print(" list to string :",string_list1)
string_list2 = list(map(list_to_string, list2))
print("tuple to string :",string_list2)