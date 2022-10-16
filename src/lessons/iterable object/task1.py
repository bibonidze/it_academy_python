a = input()
b = []
good = True
for c in a:
    if c in '[{(':
        b.append(c)
    elif c in ']})':
        if len(b) == 0:
            good = False
            break
        opn = b.pop()
        if opn == '[' and c == ']':
            continue
        if opn == '(' and c == ')':
            continue
        if opn == '{' and c == '}':
            continue
        good = False
        break
if good:
    print('Verno')
else:
    print('Ne verno')
