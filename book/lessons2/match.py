questions = [
    'What is 2+2?',
    'What is the squareroot of 16?'
]

for i in range(2):
    print(questions[i])
    option : int = int(input("Enter your choice : "))
    match option :
        case 4:
            print("Correct Answer")
        case _:
            print("Wrong Answer")


