#   Strings methods in python

#  in python strings are immutable means it can not be chanage after placing the value into any position. 
#  Any method of string does not change the original string . it creates a new string and then gives the output


a="sachin"
a1="!! sachin suthar !!!"
print(len(a))  #it gives the length of string
print(a.upper())   #converts into upper case
print(a.lower())   #converts  into lower case
print(a.rstrip("!"))   # it strips the trailling of the string 
print(a.replace("sachin","suthar"))    #it replaces the given string

a2= "Hello this is my video number 13. i am continously updated on this channel"
print(a1.capitalize())    #It converts first letter into capital letter and other letters in small case
print(a.center(50))    #it is used to center the given string 50= length of string + total white spaces

a3= "Hello is this course benefial for all... is it good?"
print(a2.count("is"))   #to count the occurence of a particular charcter in the string

print(a1.endswith("!!!")) # to check that string is ending with given input or not 
print(a3.endswith("is,2,9"))


print(a2.find("is"))   #it gives the index of the first occurence of the given string ..otherwise gives -1
# print(a2.index("adf"))   # it is used when character is known and find the index


a4="Sachin Suthar2002 \n"  
a5="    "   
print(a4.isalnum())   #it check wheater string is alphanumeric or not [A-Z,a-z,0-9]
print(a4.isalpha())   #[a-z,A-Z]


print(a4.islower())   #to check all character are in small case or not
print(a4.isupper())   #to check all character are in upper case or not

print(a4.isprintable())   #to check string is printable or not
print(a5.isspace())    #to check string is white space or not.

print(a4.istitle())    # to check string is title or not
print(a1.startswith("!!"))    #to check string is starting with given input or not


print(a4.swapcase())  #to swap the characters 
print(a4.title())   # to make the title type