import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
path="C:\\Users\\vojte\OneDrive\Plocha\data.csv"
data=pd.read_csv(path,index_col=0)
print(data)
print("\nrozdíl mezi lety:")
print(data.diff(axis=1))
fig, ax = plt.subplots()
header=list(data)
#negr
size=data.shape
for i in range(size[1]+1):
    nazev=data.index[i]
    obsah = data.iloc[[i]].values.tolist()
    ax.plot(header,obsah[0],label=nazev)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])
ax.legend(loc="upper center", bbox_to_anchor=(1.23, 0.9))
ax.grid(linestyle="--",linewidth=0.8)
ax.grid(which="minor",linestyle=":",linewidth=0.5)
ax.minorticks_on()
fig.set_size_inches(8, 5)
plt.show()