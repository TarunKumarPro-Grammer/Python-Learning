# tup = (1,2,3,5)
# print(tup)

# details = ("Abhijeet", 18, "FYBScIT", 9.8)
# print(details)


country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]     
# print(country[0])
# print(country[1])
# print(country[2])

# print(country[-1])
# print(country[-2])
# print(country[-3])

# for i in country:
#     print(i)

#we can check if an element is present in a tuple

if "India" in country :
    print("India in present!")
else:
    print("India is not present!")

#Tuple[start : end(excluded) : jumpIndex]
num = (1,2,3,4,5,6,7,8,9,10)
print(num[::2])