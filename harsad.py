a = int(input("Enter a number: ")) # taking the number from user
c = a # storing the actual value of a in c
sum_of_a = 0
a = str(a)
i = len(a)
a = int(a)
while i != 0:
    z = a % 10 # z stores the mod of a
    sum_of_a = sum_of_a + z # z adds itself to k
    a = a // 10 # a gets floor divided
    i -= 1
if c % sum_of_a == 0: # checks if the sum of a is divisible by the original number
    print(c, "is a harshad number")
else:
    print(c, "is not a harshad number")