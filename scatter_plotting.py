import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs

#==================================================

#lists = np.random.rand(2,3,10)
#var_names = ['pressure','temp','wind speed']

def scatterplot(lists,var_names):

	# lists = [mean or variance, flow property, segment number]

	Nv, Np, Ns = np.shape(lists) # Nv = 2 (mean or variance), Np = no of flow properties, Ns = no of segments

	varmax = np.zeros((2,Np))
	varmin = np.zeros((2,Np))

	for pi in range(Np):
		varmax[0,pi] = np.max(lists[0,pi,:])
		varmax[1,pi] = np.max(lists[1,pi,:])
		varmin[0,pi] = np.min(lists[0,pi,:])
		varmin[1,pi] = np.min(lists[1,pi,:])

	# Define width ratio of each subplot
	grsp = gs.GridSpec(Np,Np)

	for row in range(0,Np):
		x = lists[0,row,:]
		row_ = Np - 1 - row
		for column in range(0,Np):
			y = lists[1,column,:]

			plt.subplot(grsp[row_,column])
			plt.scatter(y,x)

			plt.xticks(np.linspace(varmin[0,column],varmax[0,column],5),fontsize=0)
			plt.yticks(np.linspace(varmin[1,row],varmax[1,row],5),fontsize=0)
	
			#dx = (varmax[0,column] - varmin[0,column]) / 5
			#dy = (varmax[1,row] - varmin[1,row]) / 5
			#plt.xlim(varmin[0,column]-dx,varmax[0,column]+dx)
			#plt.xlim(varmin[1,row]-dx,varmax[1,row]+dy)

			if row_ == Np-1:
				plt.xlabel(var_names[column])
			if column == 0:
				plt.ylabel(var_names[row])

	plt.tight_layout(pad=0.3, w_pad=0.2, h_pad=0.2)
	plt.savefig('scatter.png')
	plt.show()
