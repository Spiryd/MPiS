import numpy as np
import scipy.stats
from pick import pick
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
from numba import jit, cuda

@jit
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
    lcg_resault = lcg_random_uniform_sample(100000000, [0, 1])
    with open('data/lcg_data.txt', 'w') as f:
        for i in lcg_resault:
            f.write(str(i))
    pcg64 = np.random.Generator(np.random.PCG64())
    pcg64_resaults = pcg64.integers(0, 2, 100000000)
    with open('data/pcg_data.txt', 'w') as f:
        for i in pcg64_resaults:
            f.write(str(i))

@jit
def random_walk(n):
    walk = np.empty(n, dtype=np.int32)
    vals = np.array((-1, 1), dtype= np.int8)
    height = 0
    for i in range(n):
        height += np.random.choice(vals)
        walk[i] = height
    return walk
    
def task2():
    N = [5, 10 , 15, 20, 25, 30, 100]
    data = pd.DataFrame()
    for n in N:
        print(f"N = {n}")
        column = []
        for i in range(100000):
            column.append(random_walk(n)[n-1])
        data[f'{n}'] = column
    data.set_index(data.index + 1, inplace=True)
    data.to_csv("./data/task2.csv")

@jit
def up_time(walk):
    time = 0
    prev = 0
    for s in walk:
        if s > 0 or prev > 0:
            time += 1
        prev = s
    return time

def task3():
    N = [100, 1000, 10000]
    data = pd.DataFrame()
    for n in N:
        print(f"N = {n}")
        column = []
        for k in range(5000):
            p = up_time(random_walk(n))/n
            column.append(p)
        data[f'{n}'] = column
    data.set_index(data.index + 1, inplace=True)
    data.to_csv("./data/task3.csv")

def acrsin_pdf(x):
    return(1/(np.pi*np.sqrt(x*(1 - x))))

def gen_charts():
    task3_data = pd.read_csv("./data/task3.csv", index_col=0)
    sns.set_context("paper")
    sns.histplot(data=task3_data, x="100", bins=20, stat="percent")
    plt.savefig("charts/100.png")
    plt.clf()
    sns.histplot(data=task3_data, x="1000", bins=20, stat="percent")
    plt.savefig("charts/1000.png")
    plt.clf()
    sns.histplot(data=task3_data, x="10000", bins=20, stat="percent")
    plt.savefig("charts/10000.png")
    plt.clf()
    task2_data = pd.read_csv("./data/task2.csv", index_col=0)
    sns.histplot(data=task2_data, x="5", cumulative=True)
    plt.show()

    
def main():
    title = "Choose option: "
    options = ["Task 1", "Taks 2", "Task 3", "Generate Charts", "Exit"]
    exit = False
    while not exit:
        option, index = pick(options, title, indicator='=>')
        match index:
            case 0:
                task1()
            case 1:
                task2()
            case 2:
                task3()
            case 3:
                gen_charts()
            case _:
                exit = True
                
if __name__ == '__main__':
    main()
