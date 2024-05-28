# def add(x:int,y:int):
#     return x+y

# n1 = int(input("Enter the first number : "))
# n2 = int(input("Enter the second number : "))

# s = add(n1,n2)
# print(add(n1,n2))

# def average(a=1,b=4):
#     print(a,b)

# average() #default params are passed to print statement
# average(5) # overides the param value of a

#--------------------------------------------------------
#important = variable number argument, simple average to any amount of numbers so what write 100 arguments for it, no

def average(*numbers): #numbers is now iterable, like a list of somesort
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum/len(numbers))
average(1,2,3) # we did'nt had to write 10 arguments to accept 10 arguments
