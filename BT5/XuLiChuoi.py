
s = input()
ls = ["a","o","y","e","u","i"]
s=s.lower()
for char in ls:
    s = s.replace(char,"")
ls2 = ['.'+c for c in s]
print("".join(ls2))