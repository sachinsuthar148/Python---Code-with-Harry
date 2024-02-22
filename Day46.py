#os module in python

import os


# if(not os.path.exists("data")):
#     mkdir("data")


# for i in range(0,100):
#     os.mkdir(f"data/video {i+1}")



# for i in range(0,100):
#     os.rename(f"data/video {i+1}",f"data/tutorial {i+1}")


print(os.getcwd())

os.chdir("E:")
print(os.getcwd())