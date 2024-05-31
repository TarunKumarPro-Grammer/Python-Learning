#setting the data in the form of a list
questions = [
    "What is the capital of India?",
    "Who is the current Prime Minister of India?",
    "Where is India's Silicon Valley located?",
    "What is the national sport of India?",
    "What is the national flower of India?",
    "What is the national language of India?",
    "India's space agency acronym?"
]
answers = [
    "New Delhi",
    "Narendra Modi",
    "Bangalore",
    "Hockey",
    "Lotus",
    "Hindi",
    "ISRO"
]


def lowerList(list:list[str]) :
    temp = []
    for i in list:
        temp.append(i.lower())
    return temp
    


loweranswers= lowerList(answers)

counter = 0
money =0
chances: int = 1



while True:
    if counter < len(loweranswers):
        print(questions[counter],"\n")
    else:
        break
    temp = input("Enter a valid response(don't worry about the case) :")
    if chances != 0:
        if temp.lower() == loweranswers[counter]:
            print("You guessed it right!")
            money = money + 100
            print(f"Your have {money} in your wallet\n")
            
            counter = counter + 1
            continue
        else:
            
            print("You guessed it wrong!\n")
            money = 0
            chances -= 1
            print(f"You Lost all your money and you now have {money}")
    else:
        print("You have no more chances!")
        break
    counter += 1
    
