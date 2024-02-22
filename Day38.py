#rays custom error in python

try:
  x=int(input("Enter a number between 5 and 8:"))
  if(x>5 or x<5):
      raise ValueError("Value should be between 5 and 8")
  else:
      print(x)
except Exception as e:
    print(e)



    