list1 =[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list1.sort(key=lambda x: x[1])
print(list1)

# tuplle1=tuple()
# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if list1[i][1] > list1[j][1]:
#             tuplle1 = list1[i]
#             list1[i] = list1[j]
#             list1[j] = tuplle1
# print(list1)    