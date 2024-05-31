marks = [3,5,7]
print(marks[0])

names  = ["tarun","tanya","mummy","papa"]
print(type(names[0]))

if "tarun" in names:
    print("yes")
else:
    print("no")
    
#same things applies to strings as well 
#same way you index strings you can index list too!
#we can make list on the spot

#also known as list comprehension
lst = [i for i in range(4)]
print(lst)
evenLst = [i for i in range(10) if i%2 == 0 ]
print(evenLst)

list = [["a",1],["b",2],["c",3]]
for sec in list:
    for ques in sec:
        print(ques)