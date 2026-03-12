# In following text count occurrence of each letter (irrespective of case). Hint: convert string to same case e.g. text.lower().
#    ```python
text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."""
text =text.lower()
dict1={}
for  a in text:
    if(a.isalpha()):
        if(a in dict1):
         dict1[a] +=1
        else:
         dict1[a]=1
print(dict1)