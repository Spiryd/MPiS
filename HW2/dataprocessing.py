import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    for col in ["B", "U", "L", "C", "D", "D-C"]:
        cols = [str(i)  for i in range(1, 51)]
        processed = pd.DataFrame(columns=cols)
        for n in range(1, 101):
            to_be_processed = pd.read_csv(f"data/{n}.csv", index_col=0)
            to_be_processed = to_be_processed[col]
            to_be_processed = to_be_processed.tolist()
            processed.loc[len(processed)] = to_be_processed
        processed.to_csv(f"processed_data/{col}.csv")
        
    for col in ["B", "U", "L", "C", "D"]:
        to_be_processed  = pd.read_csv(f"processed_data/{col}.csv", index_col=0)
        processed = pd.DataFrame()
        to_be_processed = to_be_processed.mean(axis=1)
        processed = processed.assign(value = to_be_processed)
        processed['n'] = (processed.index + 1) * 1000
        processed.to_csv(f"processed_data/avg_{col}.csv")
                
if __name__ == '__main__':
    main()