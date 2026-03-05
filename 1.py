people = {'Arham': 'Blue', 'Vinod': 'Purple', 'Jenny': 'Pink','Lisa': 'Yellow'}

# Find out how many students are in the list
num_students = len(people)
print(f"A. Number of students: {num_students}")

#Change Lisa’s favourite colour 
people['Lisa'] = 'Green'

#Remove 'Jenny' and her favourite colour
del people['Jenny']

#Sort 
print("Sorted students and colours:")
for name in sorted(people.keys()):
    print(f"{name}: {people[name]}")