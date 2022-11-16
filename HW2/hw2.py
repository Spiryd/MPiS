import numpy as np
import pandas as pd
import time

s_time = time.time()

df = pd.DataFrame(columns=["B", "U", "L", "C", "D", "D-C"])

for n in range(1, 101):
    n = n * 1000
    for k in range(50):
        counter = 0
        all_no_zero = False
        all_no_one = False
        bins = np.zeros(n, np.uint32)
        row = np.zeros(6, np.uint32)
        while(not all_no_one):
            counter += 1
            shot = np.random.randint(0, n)
            bins[shot] += 1
            if counter == n:
                row[1] = n - np.count_nonzero(bins)#ilosc - pełne
                row[2] = np.max(bins)              
            if(not all_no_zero and np.min(bins) == 1):
                all_no_zero = True
                row[3] = counter
                row[0] = counter + 1
            if (np.min(bins) == 2):
                all_no_one = True
                row[4] = counter
                row[5] = row[4] - row[3]
        df.loc[len(df)] = row
    df.to_csv(f"{n}.csv")
            
    e_time = time.time()    
    print(e_time - s_time)
                