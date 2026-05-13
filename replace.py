name = 'kesha'
new_name = ''
for c in name:
    if c == 's':
        c = '$'
    elif c == 'e':
        c = '3'
    elif c == 'a':
        c = '@'
    new_name += c

print(new_name)
#relpaces any character w another character!!!
