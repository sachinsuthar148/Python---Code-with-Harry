# seek() , tell(), truncate() function in python

#1. seek() function

with open('file1.txt','r') as f:
    # move to the 10th byte in the file
    f.seek(10)  #--> ye cursor ko jo specified  jagah vha pe la deta hai...
    #Read the next 5 bytes
    x=f.read(5) #--> fir jha cursor aayega vha se pdhna start krega
    print(x)

    

# 2. tell() function

with open('file1.txt', 'r') as w:
    #seek the saved position
    w.seek(10)
    #save the current position
    current_position=w.tell()    #cursor ki position btata hai..
    print(current_position)
    
    y=w.read()
    print(y)
    
#3. truncate function

with open('sample.txt','w') as b:
    b.write("HELLO WORLD")
    b.truncate(5)   #file is size ko kam kr deta h


with open('sample.txt','r') as h:
    print(h.read())