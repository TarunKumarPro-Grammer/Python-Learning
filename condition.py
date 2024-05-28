secret_num = 8

guess = int(input("Enter a Number : "))
if guess == secret_num:
    print("You guessed it right!")
elif guess > secret_num:
    print("Your guess was too high..")
else:
    print("Your guess was too low..")


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
