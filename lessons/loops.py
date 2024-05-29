colors = ["red" , "green" , "blue", "brown" ]

# for color in colors:
#     print(color)

# name = "Tarun"
# for char in name:
#     print(char,end=" ")

# for i in range(3): #for iterating over for finite number of times
#     print(i)


# for i in range(3,8,2):
#     print(i)

# Else with While Loop

# x = 5
# while x> 0:
#     print(x)
#     x -= 1  
# else:
#     print("Counter is now zero")
    
#do while syntax in python
# while True:
#     inp = int(input("Enter a number : "))
#     print(inp)
#     # if not inp%2 ==0: # not will also negate the condition variable
#     #     print("Oops You entered a odd number !")
#     #     break   
#     if  inp%2 !=0: # not will also negate the condition variable
#         print("Oops You entered a odd number !")
#         break
for i in range(12):
    
    if i == 10:
        print("Skipped")
        continue #skips the current iteration and moves to next iteration
    print(i)