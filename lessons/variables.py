x: int = 8; # explicit typecasting

print(x)

x = "joker"
# another way to initialize a string
y: str = "joker"

print(x,y)

#we can also use if else for assignment

num1: int = input("Enter a number : ")
num2: int = input("Enter another number : ")

largerNum = num1 if num1>num2 else num2
print(f"The larger of the two number entered : {largerNum}")