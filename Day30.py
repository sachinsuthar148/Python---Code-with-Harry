# Recursion function 

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

'''
5 * factorial(4)
5 *4* factorial(3)
5 *4*3 factorial(2)
5 *4*3*2 factorial(1)
5 *4*3**2*1  => 120
'''

# f(0)=0
# f(1)=1
# f(2)= f(1)+f(0)
# f(n)=f(n-1)+f(n-2)


def febonacci(n):
        if(n==0):
            return 0
        elif(n==1):
            return 1
        else:
            return febonacci(n-1) + febonacci(n-2)

for i in range(10):
    print(febonacci(i),end=' ')
        