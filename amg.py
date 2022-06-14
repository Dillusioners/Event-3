num = int(input("Enter the number you want to check"))
num_retainer = num
c = 0
while num > 1: #This while loop will run until number doesn't become 1.
    c = c + (num % 10) ** 3 #c will store the value of the sum of the cubes of the digits of the numbers
    num = num // 10
if c == num_retainer:
    print(num_retainer, "is an amstrong number")
else:
    print(num_retainer, "not an amstrong number")