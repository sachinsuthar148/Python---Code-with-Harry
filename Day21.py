# Function Arguments in python

'''
There are four types of Arguments in python
1. Default Arguments
2. Keyword Arguments
3. Variable length Arguments
4. Required Arguments
'''

def average(a,b):  #Required Arguments
    print("Average is",(a+b)/2)
# average(10,20)


def average1(a,b=10,c=43):
    print("average is",(a+b+c)/3)
# average1(2,3,4)



def fullName(name,mname="Kumar",lname="Suthar"):   # Default Arguments
    print("Hi",name,mname,lname)
# fullName("Sachin")
# fullName("papa",mname="king")      # Keyword Arguments



#Variable length Argument

def average3(*numbers):   #Takes input as a tuple       
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is ",sum/len(numbers))
    # return sum/len(numbers)

average3(3,4,5,6,7)


def name(**name):               #It takes input as a "DICTIONARY"
    print("Hello",name["fname"],name["mname"],name["lname"])
name(fname="sachin",mname="bhai",lname="suthar")