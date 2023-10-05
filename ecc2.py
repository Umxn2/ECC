import math
import numpy as np
import matplotlib.pyplot as plt

class fun:
    
    
    def geta():
        a = int(input("give value of a "))
        b = int(input("give value of b "))
        return a , b
    def plot(a, b, curveroot):
        
            x = np.arange(curveroot, 10.0, 0.01)
            y = (x**3+a*x+b)**0.5
        
            y = np.array(y)
            z=-y
            plt.plot(x,y)
            plt.plot(x,z)
            


class P(fun):
    def zero(a,b):
        ball = [1,0,a,b]
        root = np.roots(ball)
        i = 0 
        for i in range(len(root)):
            if np.real(root[i]) == root[i]:
                
                curveroot = np.real(root[i])
        return curveroot

    
   
    def calcY_cord(a,b, x_cord):
        y_cord=(x_cord**3+a*x_cord+b)**0.5
        return y_cord
      
    def calcCord(a, b, x_cord, y_cord, curveroot,n):
       
        ball = [1, 0, a-(3*x_cord*x_cord-a)/(2*y_cord), b - y_cord+x_cord*(3*x_cord*x_cord+a)/(2*y_cord)]
        root =   np.roots(ball)
        print(root)
        i = 0 
        for i in range(len(root)):
            if np.real(root[i]) == root[i]:
             
                
                x_new = np.real(root[i])
                if x_new < curveroot :
                    y_cord = y_cord*(-1)
                   
                  
                   
                    return  P.calcCord(a,b,x_cord, y_cord, curveroot, n)

      #  print(x_new)
        y_new = (x_new**3+a*x_new+b)**0.5
        print(y_new)
        x_cord= x_new

       
        
        y_cord=y_new*-1
      
        n=n-1
        if(n>0):
            plt.plot(x_cord, y_cord, 'ro')
            print(y_cord)
            
       
            return P.calcCord(a, b, x_cord, y_cord, curveroot, n)
            
        return x_cord, y_cord
    

        
fun()
a , b = fun.geta()

P()
curveroot = P.zero(a,b)
fun.plot(a,b, curveroot)
print(curveroot)
xcord = int(input("give xcord"))
y_cord = P.calcY_cord(a, b, xcord)
plt.plot(xcord, y_cord, 'ro')
n = int(input("give n"))
x_new, y_new = P.calcCord(a, b, xcord,  y_cord, curveroot, n) 
#plt.plot(x_new, y_new, 'ro')
plt.show()
print(x_new, y_new)



     




