a = input()
small = 0
BIG = 0
for sentence in a:
    if 'a' <= sentence <= 'z':
        small += 1
    else:
        if 'A' <= sentence <= 'Z':
            BIG += 1
print(small)
print(BIG)

