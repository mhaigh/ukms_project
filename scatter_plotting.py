import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs

#==================================================

# Load list
#lists = np.load('lists.npy')
lists = np.random.rand(2,3,10)

# lists = [mean or variance, flow property, segment number]

Nv, Np, Ns = np.shape(lists) # Nv = 2 (mean or variance), Np = no of flow properties, Ns = no of segments




# Define width ratio of each subplot
grsp = gs.GridSpec(Np,Np)

for row in range(0,Np):
	for column in range(0,Np):
		plt.subplot(grsp[row,column])
		plt.scatter(lists[0,row,:],lists[1,column,:])
plt.show()
