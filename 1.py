s="The quick brown fox jumps over the lazy dog."
a='abcdefghijklmnopqrstuvwxyz'
s=s.lower()
for  al in a:
    if al not in s:
        print("The string is not a pangram.")
        break
else:    
    print("The string is a pangram.")