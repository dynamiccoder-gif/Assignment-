mylist = ['41','DROND','Sunbeam', '13','ZARA']
check_digit= lambda n: n.isdigit()
for list in mylist:
    if check_digit(list)==True:
        for i in  range(3):
            print(list)
    else:
        print(list+'#')
