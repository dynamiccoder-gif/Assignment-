lists=['apple', 'banana', 'cherry', 'rohit kumar', 'rohit baghel','aditiya pandit', 'siddthan rana', 'ashwini kumar']
word_sizer = lambda n : len(n)
max_number_list= list(map(word_sizer, lists))
max_number =max(max_number_list)

max_word = list(filter(lambda x: len(x) == max_number, lists))
print(max_word)
