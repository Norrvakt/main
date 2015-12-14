import math


def bounce(n):
    if n == 0:
        print 0
    else:
        print n
        bounce(n-1)
        print n
        

def bounce2(n):
    for x in range(n,-1,-1):
        print x
    for y in range(1,n+1,1):
        print y

def tvarsumman(n):
    if(n>0):
        n = (n%10)+(n/10)
        print n

def tvarsumman2(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s
    
def derivative(f,x,h):
    return (f(x+h) - f(x-h)) / (2.0*h) 
    

def solve(f,x0,h):
    lastx = x0
    nextx = lastx + 10 * h
    while(abs(lastx - nextx) > h):
        newy = f(nextx)
        lastx = nextx
        nextx = lastx - newy / derivative(f,lastx,h)
    return nextx

        
def function1(x):
    return 2*x*x-5*x+1

result1 = solve(function1,5,0.01)
print result1

print "------------------------"

def function2(x):
    return(2**x)-1

result2 = solve(function2,5,0.01)
print result2

print "------------------------"
    
def function3(x):
    return x-math.e**-x

result3 = solve(function3,5,0.01)
print result3

print "------------------------"
    
derivative(math.sin,math.pi,0.0001)

tvarsumman2(12)

print "------------------------"

tvarsumman(99)

bounce(3)
print "------------------------"
bounce2(3)
print "------------------------"
