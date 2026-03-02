words = ['level', 'radar', 'hello', 'world', 'madam']
check = lambda  n : n[::-1]==n
reverse = list( filter(check, words))
print(reverse)
     