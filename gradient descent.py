import numpy as np

def gradient_descent(x,y):
    m = 0
    b = 0
    n = len(x)
    iterations = 100
    rate = 0.001
    
    for i in range(iterations):
        y_predict = m * x + b
        cost = (1/2*n)*sum([val**2 for val in (y - y_predict)])
        md = (1/n)*sum(x*(y-y_predict))
        bd = (1/n)*sum((y-y_predict))
        m = m - rate * md
        b = b - rate * bd
        print(y_predict,m,b)
        
        
    
    
    
    
    
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])

gradient_descent(x,y)