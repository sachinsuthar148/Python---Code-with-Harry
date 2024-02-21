# Exercise 2 : for print good morning and good evening

import time

timestamp= time.strftime('%H:%M:%S')
print(timestamp)
timeHour= int(time.strftime('%H'))
print(timeHour)
timeMinute= int(time.strftime('%M'))
print(timeMinute)
timeSecond=int( time.strftime('%S'))
print(timeSecond)
print(type(timestamp))

if(timeHour>=0 and timeHour<12):
    print("Good Morning")
elif(timeHour>=12 and timeHour<17 ):
    print("Good afternoon")
elif(timeHour>=17 and  timeHour<=20):
    print("Good Evening")
elif(timeHour>=20 and timeHour<=24):
    print("Good Night")
    