inp = int(input("Enter a number : "))



# print(inp)


match inp:
    case 0:
        print("You Entered Zero as your number!")
    case 1:
        print("You entered 1 as your number!")
    case _ if inp == 12: # _ means default like how it was in java 

        print("I don't know")
    case _ :
        print("Lets what happens")
        
# questions = [
#     'What is 2+2?',
#     'What is the squareroot of 16?'
# ]

# for i in range(2):
#     print(questions[i])
#     option : int = int(input("Enter your choice : "))
#     match option :
#         case 4:
#             print("Correct Answer")
#         case _:
#             print("Wrong Answer")
