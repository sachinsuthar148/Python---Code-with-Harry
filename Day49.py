# File IO in python

'''
There are three modes in python 1. read 2. write 3. append
'''

# Opening in read mode
f=open('file1.txt','r')
text=f.read()
print(text)
f.close()
print()

#Opening file in write mode

#w=open('file2.txt','w')
text="this is the content to be written in the file"
#f.write(text)
print("The content is written in the file2.txt")
w.close()
print()

#opening a file in read mode

a=open('file2.txt','a')
text=" This is the text that is going to append the end of the file2.txt"
a.write(text)
print("The content is appended in the file2.txt")
a.close()
print()


#SHORT HAND TO READ A FILE

with open('file1.txt','r') as f:
    text=f.read()
    print(text)
