import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pick import pick
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

def gen_data():
    s_time = time.time() 
    for n in range(1, 101):
        unit_s_time = time.time() 
        table = bnb_experiment(n * 1000)
        df =  pd.DataFrame(columns=["B", "U", "L", "C", "D", "D-C"])
        for row in table:
            df.loc[len(df)] = row
        df.to_csv(f"data/{n}.csv")
        unit_e_time = time.time()    
        print(unit_e_time - unit_s_time)
    e_time = time.time()
    print(e_time - s_time)

def to_vars():
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
    # a
    to_be_charted = pd.read_csv("processed_data/avg_B.csv", index_col=0)
    to_be_charted['a1'] = to_be_charted['value']/to_be_charted['n']
    sns.scatterplot(data=to_be_charted, x='n', y='a1')
    plt.savefig("charts/a1.png")
    plt.clf()
    to_be_charted['a2'] = to_be_charted['value']/np.sqrt(to_be_charted['n'])
    sns.scatterplot(data=to_be_charted, x='n', y='a2')
    plt.savefig("charts/a2.png")
    plt.clf()
    # b
    to_be_charted = pd.read_csv("processed_data/avg_U.csv", index_col=0)
    to_be_charted['b1'] = to_be_charted['value']/to_be_charted['n']
    sns.scatterplot(data=to_be_charted, x='n', y='b1')
    plt.savefig("charts/b1.png")
    plt.clf()
    # c
    to_be_charted = pd.read_csv("processed_data/avg_L.csv", index_col=0)
    to_be_charted['c1'] = to_be_charted['value']/np.log(to_be_charted['n'])
    sns.scatterplot(data=to_be_charted, x='n', y='c1')
    plt.savefig("charts/c1.png")
    plt.clf()
    to_be_charted['c2'] = to_be_charted['value']/np.log(np.log(to_be_charted['n']))
    sns.scatterplot(data=to_be_charted, x='n', y='c2')
    plt.savefig("charts/c2.png")
    plt.clf()    
    to_be_charted['c3'] = to_be_charted['value']/(np.log(to_be_charted['n'])/np.log(np.log(to_be_charted['n'])))
    sns.scatterplot(data=to_be_charted, x='n', y='c3')
    plt.savefig("charts/c3.png")
    plt.clf()
    # d
    to_be_charted = pd.read_csv("processed_data/avg_C.csv", index_col=0)
    to_be_charted['d1'] = to_be_charted['value']/to_be_charted['n']
    sns.scatterplot(data=to_be_charted, x='n', y='d1')
    plt.savefig("charts/d1.png")
    plt.clf()
    to_be_charted['d2'] = to_be_charted['value']/(to_be_charted['n'] * np.log(to_be_charted['n']))
    sns.scatterplot(data=to_be_charted, x='n', y='d2')
    plt.savefig("charts/d2.png")
    plt.clf()
    to_be_charted['d3'] = to_be_charted['value']/(to_be_charted['n']**2) 
    sns.scatterplot(data=to_be_charted, x='n', y='d3')
    plt.savefig("charts/d3.png")
    plt.clf()
    # e
    to_be_charted = pd.read_csv("processed_data/avg_D.csv", index_col=0)
    to_be_charted['e1'] = to_be_charted['value']/to_be_charted['n']
    sns.scatterplot(data=to_be_charted, x='n', y='e1')
    plt.savefig("charts/e1.png")
    plt.clf()
    to_be_charted['e2'] = to_be_charted['value']/(to_be_charted['n'] * np.log(to_be_charted['n']))
    sns.scatterplot(data=to_be_charted, x='n', y='e2')
    plt.savefig("charts/e2.png")
    plt.clf()
    to_be_charted['e3'] = to_be_charted['value']/(to_be_charted['n']**2) 
    sns.scatterplot(data=to_be_charted, x='n', y='e3')
    plt.savefig("charts/e3.png")
    plt.clf()
    # f
    to_be_charted = pd.read_csv("processed_data/avg_D.csv", index_col=0)
    tmp = pd.read_csv("processed_data/avg_C.csv", index_col=0)
    to_be_charted['c'] = tmp['value']
    to_be_charted['f1'] = (to_be_charted['value'] - to_be_charted['c'])/to_be_charted['n']
    sns.scatterplot(data=to_be_charted, x='n', y='f1')
    plt.savefig("charts/f1.png")
    plt.clf()
    to_be_charted['f2'] = (to_be_charted['value'] - to_be_charted['c'])/(to_be_charted['n'] * np.log(to_be_charted['n']))
    sns.scatterplot(data=to_be_charted, x='n', y='f2')
    plt.savefig("charts/f2.png")
    plt.clf()
    to_be_charted['f3'] = (to_be_charted['value'] - to_be_charted['c'])/(to_be_charted['n'] * np.log(np.log(to_be_charted['n'])))
    sns.scatterplot(data=to_be_charted, x='n', y='f3')
    plt.savefig("charts/f3.png")
    plt.clf()

def main():
    title = "Choose option: "
    options = ["Generate data", "Process initial data", "Process to avg", "Generate charts", "Exit"]
    exit = False
    while not exit:
        option, index = pick(options, title, indicator='=>')
        match index:
            case 0:
                gen_data()
            case 1:
                to_vars()
            case 2:
                to_avg()
            case 3: 
                gen_charts()
            case 4:
                exit = True
                
if __name__ == '__main__':
    main()