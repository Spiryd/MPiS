import math
from pick import pick
import numpy as np
import random
    
N = [50*i for i in range(1,101)]

def main():
    title = "Choose option: "
    options = ["Symulate Integral x^1/3 on [0, 8] ", "Symulate Integral sin(x) on [0, pi] ", "Symulate Integral 4x(1 - x)^3 on [0, 1] ", "Pi form circle", "Exit"]
    exit = False
    while not exit:
        option, index = pick(options, title, indicator='=>')
        match index:
            case 0:
                firstIntegral()
            case 1:
                secondIntegral()
            case 2:
                thirdtIntegral()
            case 3:
                piFromCircle()
            case 4:
                exit = True
                
def firstIntegral():
    m = 2
    a = 0
    b = 8
    
    counter = 0# n's under curve
    
    results = np.empty(50)#to calc avg
    
    with open("a_1.csv", 'w', encoding='utf-8') as f:
        #headrer
        f.write("n,")
        for p in range(1, 51):
            f.write(f"{p},")
        f.write("avg\n")
        #meat    
        for n in N:
            f.write(f"{n},")
            for p in range(50):
                counter = 0
                for k in range(n):
                    x = random.uniform(a, b)
                    y = random.uniform(0, m)
                    if np.cbrt(x) >=y:
                        counter += 1
                result = (counter/n)*(b-a)*m
                results[p] = result
                f.write(f"{result},")
            f.write(str(np.average(results)))
            f.write("\n")
                                  
def secondIntegral():
    m = 1
    a = 0
    b = math.pi
    
    counter = 0# n's under curve
    
    results = np.empty(50)#to calc avg
    
    with open("a_2.csv", 'w', encoding='utf-8') as f:
        #headrer
        f.write("n,")
        for p in range(1, 51):
            f.write(f"{p},")
        f.write("avg\n")
        #meat    
        for n in N:
            f.write(f"{n},")
            for p in range(50):
                counter = 0
                for k in range(n):
                    x = random.uniform(a, b)
                    y = random.uniform(0, m)
                    if math.sin(x) >= y:
                        counter += 1
                result = (counter/n)*(b-a)*m
                results[p] = result
                f.write(f"{result},")
            f.write(str(np.average(results)))
            f.write("\n")
        
def thirdtIntegral():
    m = 2
    a = 0
    b = 1
    
    counter = 0# n's under curve
    
    results = np.empty(50)#to calc avg
    
    with open("a_3.csv", 'w', encoding='utf-8') as f:
        #headrer
        f.write("n,")
        for p in range(1, 51):
            f.write(f"{p},")
        f.write("avg\n")
        #meat    
        for n in N:
            f.write(f"{n},")
            for p in range(50):
                counter = 0
                for k in range(n):
                    x = random.uniform(a, b)
                    y = random.uniform(0, m)
                    if 4*x*((1-x)**3) >= y:
                        counter += 1
                result = (counter/n)*(b-a)*m
                results[p] = result
                f.write(f"{result},")
            f.write(str(np.average(results)))
            f.write("\n")      
        
def piFromCircle():
    a = 0
    b = 2
    m = 2
    counter = 0# n's under curve
    
    results = np.empty(50)#to calc avg
    
    with open("b.csv", 'w', encoding='utf-8') as f:
        #headrer
        f.write("n,")
        for p in range(1, 51):
            f.write(f"{p},")
        f.write("avg\n")
        #meat    
        for n in N:
            f.write(f"{n},")
            for p in range(50):
                counter = 0
                for k in range(n):
                    x = random.uniform(a, b)
                    y = random.uniform(0, m)
                    if (x-1)**2 + (y-1)**2 <= 1:
                        counter += 1
                result = (counter/n)*(b-a)*m
                results[p] = result
                f.write(f"{result},")
            f.write(str(np.average(results)))
            f.write("\n")       

if __name__ == '__main__':
    main()
    