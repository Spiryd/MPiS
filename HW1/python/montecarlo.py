import math
from pick import pick
import numpy as np

def main():
    title = "Choose option: "
    options = ["Symulate Integral x^1/3 on [0, 8] ", "Symulate Integral sin(x) on [0, pi] ", "Symulate Integral 4x(1 - x)^3 on [0, 1] ", "Pi form circle", "Exit"]
    exit = False
    while not exit:
        option, index = pick(options, title, indicator='=>')
        match index:
            case 0:
                print("0")
            case 1:
                print("1")
            case 2:
                print("2")
            case 3:
                print("3")
            case 4:
                exit = True
                
def
    

if __name__ == '__main__':
    main()
    