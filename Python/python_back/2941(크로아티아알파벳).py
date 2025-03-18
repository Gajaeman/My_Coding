L = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
text = input()
for i in L :
    text = text.replace(i, "*")
print(len(text))