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
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ''
        for x in s:
            if x.isalpha(): 
                a += x.lower()
            if x.isnumeric(): 
                a += x
        return a == a[::-1]
