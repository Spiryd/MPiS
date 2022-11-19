import numpy as np
import pandas as pd
import time
from numba import jit, cuda

@jit(target_backend='cuda')
def bnb_experiment(n):
    table = []
    for k in range(50):
        all_no_zero = False
        all_no_one = False
        first_collison = False
        bins = np.zeros(n, np.uint32)
        row = np.zeros(6, np.uint32)
        counter = 0
        while(not all_no_one):
            counter += 1
            bins[np.random.randint(0, n)] += 1
            if not first_collison and np.max(bins) == 2:
                row[0] = counter
            if counter == n:
                row[1] = n - np.count_nonzero(bins)#ilosc - pełne
                row[2] = np.max(bins) 
            if(not all_no_zero and np.min(bins) == 1):
                all_no_zero = True
                row[3] = counter
            if (all_no_zero and np.min(bins) == 2):
                all_no_one = True
                row[4] = counter
                row[5] = row[4] - row[3]
        table.append(row)
    return(table)
        
def main():
    s_time = time.time() 
    for n in range(1, 101):
        unit_s_time = time.time() 
        table = bnb_experiment(n * 1000)
        df =  pd.DataFrame(columns=["B", "U", "L", "C", "D", "D-C"])
        for row in table:
            df.loc[len(df)] = row
        df.loc[len(df)] = df.agg(np.mean)
        df.to_csv(f"{n}.csv")
        unit_e_time = time.time()    
        print(unit_e_time - unit_s_time)
    e_time = time.time()
    print(e_time - s_time)

if __name__ == '__main__':
    main()
    