import numpy as np
import random


with open("data.csv", 'w', encoding='utf-8') as f:
    f.write("n, B, U, L, C, D, D-C")
    for n in range(1, 101):
        n = n * 1000
        for k in range(50):
            counter = 0
            all_no_zero = False
            all_no_one = False
            bins = np.zeros(n, np.uint16)
            while(not all_no_one):
                counter += 1
                shot = np.random.randint(0, n-1)
                bins[shot] += 1
                if counter == n:
                    u = n - np.count_nonzero(bins)#ilosc - pełne
                    l = np.max(bins)              
                if(not all_no_zero and np.min(bins) == 1):
                    all_no_zero = True
                    c = counter
                if (np.min(bins) == 2):
                    all_no_one = True
                    d = counter
                    
                

                
                
    