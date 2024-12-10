# readline() and writelines() function in python

#readline() function:

f=open('file1.txt','r')
while True:
    line= f.readline()
    if not line:
        break
    print(line)
f.close()


f1=open('file2.txt','r')
student=0
while True:
    student=student+1
    line=f1.readline()
    if not line:
        break;
    marks1=line.split(",")[0]
    marks2=line.split(",")[1]
    marks3=line.split(",")[2]
    
    print(f"marks of student {student}")
    print(f"The marks of subject first is {marks1}")
    print(f"The marks of subject Second is {marks2}")
    print(f"The marks of subject third is {marks3}")
f1.close()    
    
# writelines() function in python
'''writes a sequence of strings to a file. The sequence can be any itereable object, such as list or a tuple'''

w=open('file3.txt','w')
lines=['line1\n','line2\n','line3\n']
w.writelines(lines)
print("Data is inseted and file is to be closed")
w.close()

