import numpy as np
import scipy
from pick import pick
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numba



def lcg(x, a, c, m):
    while True:
        x = (a * x + c) % m
        yield x
        
def lcg_random_uniform_sample(n, interval, seed=0):
    a, c, m = 1103515245, 12345, 2 ** 31
    bsdrand = lcg(seed, a, c, m)

    lower, upper = interval[0], interval[1]
    sample = []

    for i in range(n):
        observation = (upper - lower) * (next(bsdrand) / (2 ** 31 - 1)) + lower
        sample.append(round(observation))

    return sample

def task1():
    lcg_resault = lcg_random_uniform_sample(100, [0, 1])
    pcg64 = np.random.Generator(np.random.PCG64(100))
    pcg64_resaults = np.random.randint(0, 2, 10000) #pcg64.integers(0, 2, 10000)
    for i in pcg64_resaults:
        print(i, end="")
    print(pcg64_resaults)
    
def task2():
    n = [5, 10 , 15, 20, 30, 100]
    cols = [x for x in range(1, 100001)]
    vals = np.array((-1, 1), dtype= np.int8)
    data = pd.DataFrame()
    for i in n:
        print(f"N = {i}")
        row = []
        for j in cols:
            x = 0
            for k in range(i):
                x += np.random.choice(vals)
            row.append(x)
        print(np.mean(x))


def main():
    title = "Choose option: "
    options = ["Task 1", "Taks 2", "Exit"]
    exit = False
    while not exit:
        option, index = pick(options, title, indicator='=>')
        match index:
            case 0:
                task1()
            case 1:
                task2()
            case _:
                exit = True
                
if __name__ == '__main__':
    main()