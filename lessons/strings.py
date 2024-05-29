# you can multiply strings with a number

# print("hi"*3)#prints hi 3 time

a = " example    "
name = "tarun"
b = "hi!!!!!!!!!!"

# print(a)
# print(a[0:3]) #from 0 index to index 3 but excluding it basically n to to n-1 index 
# print(int(len(a)))
# # you can also invert the string with a trick 
# print(a[::-1]) #basically it represents (start index:stop index excluding it:step, basically means to skip by how much)

#upper and lower methods are functions that returns a string that is in uppercase or lowercase

# print(a.upper())
# print(a.lower())

# strip method removes any white spaces before and after a string if present

# print(a.strip())

#rstrip method removes trailing characters given in function parameters'
# print(b)
# print(b.rstrip("!"))

# replace method replaces """"all"""" occurences of a string with another string
# print(name)
# print(name.replace("tarun","tanya"))


#split method splits a string into a list of strings separated by spaces or the given parameters in form of a list
# list = "hi its a sPlit funcTion"
# print(list.split(" "))

#capitalize method capitalizes the first character ofS a string and it doesn't matter if its first character is already capitalized

# print(list.capitalize())

#count method counts the number of occurrences of a substring in a string

# print(b.count("!"))

#The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
# str1 = "Welcome to the Console !!!"
# print(str1.endswith("!!!"))

#We can even also check for a value in-between the string by providing start and end index positions.

# str1 = "Welcome to the Console !!!"
# print(str1.endswith("to", 4, 10)) # from "come to"

#The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("is"))

#The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Tarun"))

#As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not

# --------------------------------------------------------

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())

#The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

# str1 = "Welcome"
# print(str1.isalpha())

# The islower() method returns True if all the characters in the string are lower case, else it returns False.
# str1 = "hello world"
# print(str1.islower())

# str2 = "LETS GO SOMEWHERE"
# print(str2.isupper())

#The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
# str1 = "We wish you a Merry Christmas\n" #\n is not a printable character
# print(str1.isprintable())


#The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
# str1 = "We wish you a Merry Christmas" #escape sequences are not printabel
# print(str1.isprintable())


#The isspace() method returns True only and only if the string contains white spaces, else returns False.
# space = "Hi i am from india"
# print(space.isspace())
# onlySpace = "   "
# print(onlySpace.isspace()) # returns true only if the string contains only spaces



#The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
str = "Hi Lets Go Somewhere"
# print(str.istitle())


#The startswith() method checks if the string starts with a given value. If yes then return True, else return False.
print(str.startswith("Hi"))

#The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

print(str.swapcase())

#The title() method capitalizes each letter of the word within the string.

print(str.title( ))