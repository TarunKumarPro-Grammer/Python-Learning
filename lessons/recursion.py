# def factorial(n):
#     if n == 0 or n== 1:
#         return 1
#     else:
#         return (n * factorial(n-1))
    
# print(factorial(4))

def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (f(n-1)+f(n-2))

inp : int = int(input("Enter the number till you want to print fibonacci series : "))

for i in range(inp):
    print(f(i))