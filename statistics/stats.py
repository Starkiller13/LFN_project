import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

file = open("../results/mc_sim3.txt","r").readlines()
data = []
for i in file:
    arr = i[1:-2].split(", ")
    arr = [float(j) for j in arr]
    data.append(arr)

data = np.array(data)

means = []
sigmas = []
for index in range(len(data[0])):
    mu = np.mean(data[:,index])
    std = np.std(data[:,index])
    means.append(mu)
    sigmas.append(std)
    '''
    x = np.arange(mu - 4*std, mu + 4*std, 0.001)
    
    plt.hist(data[:,index],bins = 20, density=True)
    plt.plot(x, norm.pdf(x, mu, std))
    plt.legend(["mean: %.2f \nstd %.2f"%(mu,std)],loc = 'upper left')
    plt.xlabel("occurrencies")
    plt.ylabel("density")
    #plt.show()
    plt.savefig("img/plot_"+str(index)+".png")
    plt.close()
    '''

print("expectations: "+str(["%.4f"%item for item in means]))
print("stds :"+str(["%.4f"%item for item in sigmas]))

mot = [153801, 36648, 65143, 3706, 440712, 169731, 79]#, 2910, 2048, 729665, 1621, 9377, 13752]

zscore = []
pvalue = []

for i in range(0,7):
    z = (mot[i]-means[i])/sigmas[i]
    zscore.append(z)

print("z-scores: "+str(["%.4f"%item for item in zscore]))

for i in zscore:
    p = norm.pdf(abs(i))
    pvalue.append(p)

print("p-values: "+str(["%.4f"%item for item in pvalue]))