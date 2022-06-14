print('''1. Final velocity
2. Initial velocity
3. Time
4. Acceleration''')

print("Enter what you find (eg. 1 or 2 or 3 or 4")
n = int(input("Enter your choice"))

if(n < 5 and n > 0):
    if(n == 1):
        u = (int(input("Enter your initial velocity: ")))
        a = (int(input("Enter your accelration: ")))
        t = (int(input("Enter your time: ")))

        v = u + a * t
        print (v)
    elif(n == 2):
        v = (int(input("Enter your final velocity: ")))
        a = (int(input("Enter your accelration: ")))
        t = (int(input("Enter your time: ")))

        u = v - a * t
        print(u)
    elif(n == 3):
        u = (int(input("Enter your initial velocity: ")))
        a = (int(input("Enter your accelration: ")))
        v = (int(input("Enter your final velocity: ")))

        t = (v - u)/a
        print (t)
    elif(n == 4):
        u = (int(input("Enter your initial velocity: ")))
        v = (int(input("Enter your final velocity: ")))
        t = (int(input("Enter your time: ")))

        a = (v-u)/t
        print (a)
else:
    print("Enter a valid choice")