number = int(input("Enter a number : "))

# print(f"The entered number is {number}")

if (number == 0):
    print("The number is zero")
elif number > 0:
    if number < 10:
        print("The number is less than 10")
    else:
        print("The number is greater than 10")
else:
    print("The number is negative")

# secret_num = 8

# guess = int(input("Enter a Number : "))
# if guess == secret_num:
#     print("You guessed it right!")
# elif guess > secret_num:
#     print("Your guess was too high..")
# else:
#     print("Your guess was too low..")


#------------------------------------
# while True:
#     guess = int(input("Enter a Number : "))
#     if guess == secret_num:
#         print("You guessed it right!")
#         break
#     elif guess > secret_num:
#         print("Your guess was too high..")
#     else:
#         print("Your guess was too low..")

#-----------------------------------------

#Walrus Operator
x=0
while ((x:=x+1) < 10):
    print(x)
print("something")
#The above expression is equivalent to 
# while True:
#     if x<10:
#         print(x)
#     else:
#         break
#     x =x+1
