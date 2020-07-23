ch = input("character: ")
num =int(input("number: "))

for i in range(1, num + 1):
    for j in range(1, i + 1 ):
        print(ch , end = '  ')
    print()


for i in range(1, num + 1):
    for j in range(1, num - i + 2 ):
        print(ch , end = '  ')
    print()
  
  
