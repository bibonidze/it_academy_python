a = input()
b = ''
for c in range(len(a)):
    if b.find(a[c]) == -1 and a[c] !='':
        b += a[c]
print(b.replace(" ", ''))