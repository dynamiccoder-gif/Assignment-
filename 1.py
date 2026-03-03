lists=['apple', 'banana', 'cherry', 'rohit kumar', 'rohit baghel','aditiya pandit', 'siddthan rana', 'ashwini kumar']
max_number = lambda n : len(n)
maximum =0
max_number_list= list(map(max_number, lists))
max_number =max(max_number_list)

max_word = list(filter(lambda x: len(x) == max_number, lists))
print(max_word)
