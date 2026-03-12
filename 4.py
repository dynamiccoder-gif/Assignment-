Str1="Python83737@#8496"
sum=0
num=0
for s in Str1:
    if s.isdigit() :
        num +=1
        sum =sum +int(s)
print("sum : ",sum)
print("avergae : " ,sum/num)
    
        