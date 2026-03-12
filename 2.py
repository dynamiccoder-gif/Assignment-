student_details= [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
{'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
{'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]
for i in student_details:
        
        i['V+VI'] = (i['V'] + i['VI'])/2
        i.pop('V')
        i.pop('VI')
print(student_details)