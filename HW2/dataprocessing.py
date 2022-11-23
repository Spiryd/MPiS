import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pick import pick
import os

def to_vars():
    os.makedir(os.getcwd(), "processed_data")
    for col in ["B", "U", "L", "C", "D", "D-C"]:
        cols = [str(i)  for i in range(1, 51)]
        processed = pd.DataFrame(columns=cols)
        for n in range(1, 101):
            to_be_processed = pd.read_csv(f"data/{n}.csv", index_col=0)
            to_be_processed = to_be_processed[col]
            to_be_processed = to_be_processed.tolist()
            processed.loc[len(processed)] = to_be_processed
        processed.to_csv(f"processed_data/{col}.csv")
        
def to_avg():
    for col in ["B", "U", "L", "C", "D", "D-C"]:
        to_be_processed  = pd.read_csv(f"processed_data/{col}.csv", index_col=0)
        processed = pd.DataFrame()
        to_be_processed = to_be_processed.mean(axis=1)
        processed = processed.assign(value = to_be_processed)
        processed['n'] = (processed.index + 1) * 1000
        processed.to_csv(f"processed_data/avg_{col}.csv")
        
def gen_charts():
    
    os.mkdir(os.path.join(os.getcwd(), "charts"))
    #fist set of charts
    for col in ["B", "U", "L", "C", "D", "D-C"]:
        to_be_charted = pd.read_csv(f"processed_data/{col}.csv", index_col=0)
        to_be_charted['n'] = (to_be_charted.index + 1) * 1000
        to_be_charted_melted = to_be_charted.melt('n',  var_name='cols', value_name='val')
        chart_avg = pd.read_csv(f"processed_data/avg_{col}.csv", index_col=0)
        sns.scatterplot(data=to_be_charted_melted, x="n", y="val")
        sns.scatterplot(data=chart_avg, x='n', y='value', color="red")
        plt.tight_layout()
        plt.savefig(f"charts/{col}.png")
        plt.clf()

def main():
    print(os.getcwd())
    title = "Choose option: "
    options = ["Process initial data", "Process to avg", "Generate charts", "Exit"]
    exit = False
    while not exit:
        option, index = pick(options, title, indicator='=>')
        match index:
            case 0:
                to_vars()
            case 1:
                to_avg()
            case 2: 
                gen_charts()
            case 3:
                exit = True
                
if __name__ == '__main__':
    main()