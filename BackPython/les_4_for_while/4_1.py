word = 'Австралия'
new_word=''
for i in range(len(word)):
  print(i)
  print(type(i))
  if i == 0 or i == 1:
    new_word=new_word+(word[i])
  elif i == len(word)-1:
    new_word = new_word+(word[i])
  else:
    new_word=new_word+'*'

print(new_word)

text = "734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5"
just_words = []
text = text.split(' ')
for i in text:
  if isalpha(text[i]):
    just_words.append(i)
text_cleaned = str(just_words)
print(text_cleaned)