import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../data/data.csv')

clients = df['Cliente']
prices = df['TOTAL']

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} $)".format(pct, absolute)

plt.pie(prices, labels=clients, autopct=lambda pct: func(pct, prices))
plt.savefig('../figures/hotel-pie.png')