import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt


class Net(nn.Module):
    def __init__(self,n):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1, n)
        self.fc2 = nn.Linear(n, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def nextnum(x):
    dat = x[0]
    n = dat[-1]
    net = Net(n)
    dat = np.array(dat)
    x_train = dat[:-1]
    y_train = dat[1:]
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=0.01)

    for epoch in range(1000):
        inputs = torch.from_numpy(x_train).float().unsqueeze(1)
        labels = torch.from_numpy(y_train).float().unsqueeze(1)

        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    x_test = np.array([n])
    y_test = net(torch.from_numpy(x_test).float().unsqueeze(1))
    return round(y_test.item())

path="C:\\Users\\vojte\OneDrive\Plocha\data.csv"
data=pd.read_csv(path,index_col=0)
print(data)
print("\nrozdíl mezi lety:")
print(data.diff(axis=1))


fig, ax = plt.subplots()
header=list(data)
size=data.shape
for i in range(size[1]+1):
    nazev=data.index[i]
    obsah = data.iloc[[i]].values.tolist()
    line,= ax.plot(header,obsah[0],label=nazev)
    ax.plot(str(int(header[-1])+1), nextnum(obsah), marker="x", markersize=5, color=str(line.get_color()))
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])
ax.legend(loc="upper center", bbox_to_anchor=(1.23, 0.9))
ax.grid(linestyle="--",linewidth=0.8)
ax.grid(which="minor",linestyle=":",linewidth=0.5)
ax.minorticks_on()
fig.set_size_inches(8, 5)
plt.show()