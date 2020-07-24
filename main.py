char = input('>> enter a char: ')
num = int(input('>>enter a positive number(>5): '))

for i in range(1, num + 1):
  text = ' '
  for j in range(i):
    text += char
  print(text)

for i in range(1, num + 1):
  text = ' '
  for j in range(num - i):
    text += char
  print(text)
