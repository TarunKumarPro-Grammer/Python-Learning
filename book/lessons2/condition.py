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
    #see you can use vim commmands now but still slow
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

#     x =x+1
