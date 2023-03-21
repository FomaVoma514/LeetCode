# Задача 1
number = int(input()) 
last = number 
rev = 0 
while number > 0: 
    number_1 = number % 10 
    rev = rev * 10 + number_1
    number = number // 10 
if last == rev: 
    print('True') 
else: 
    print('False')


# Задача 2
word = input()
simvole = word[::-1]
if word == simvole:
  print('True')
else:
  print('False')
