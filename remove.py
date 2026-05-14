sentence = 'The e key on my keyboard is broken'
new_sentence = ''
for c in sentence:
    if c != 'e':
        new_sentence += c
print(new_sentence)
