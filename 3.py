string= input("Enter a string: ")
for s in range(len(string)):
     string= string[1:]+ string[0:1]
     print(string)
