import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
file = open("../mc_sim.txt","r").readlines()
data = []
for i in file:
    arr = i[1:-2].split(", ")
    arr = [float(j) for j in arr]
    data.append(arr)
    
data = np.array(data)

for index in range(len(data[0])):
    mu = np.mean(data[:,index])
    std = np.std(data[:,index])
    x = np.arange(mu - 3*std, mu + 3*std, 0.001)
    plt.hist(data[:,index],bins = 20, density=True)
    plt.plot(x, norm.pdf(x, mu, std))
    #plt.show()
    plt.savefig("plot_"+str(index)+".png")
    plt.close()
