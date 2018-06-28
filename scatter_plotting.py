import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs

#==================================================

#lists = np.random.rand(2,3,10)
#var_names = ['pressure','temp','wind speed']

def scatterplot(lists,var_names):

	"""
	Function to create an array of scatter plots.
	"""

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

	for row in range(Np):
		x = lists[0,row,:]
		row_ = Np - 1 - row
		for column in range(Np):
			y = lists[1,column,:]

			plt.subplot(grsp[row_,column])
			plt.scatter(y,x)

			plt.xticks(np.linspace(varmin[0,column],varmax[0,column],5),fontsize=0)
			plt.yticks(np.linspace(varmin[1,row],varmax[1,row],5),fontsize=0)

			if row_ == Np-1:
				plt.xlabel(var_names[column])
			if column == 0:
				plt.ylabel(var_names[row])
		
			#plt.xlabel('MEAN',fontsize=16)
			#plt.ylabel('VAR',rotation=90,fontsize=16)

	plt.tight_layout(pad=0.3, w_pad=0.2, h_pad=0.2)
	#plt.savefig('scatter.png')
	plt.show()


#==================================================

def corr(lists,var_names):

	"""
	Function to calculate and plot the correlation between means and variances of a set of variables.
	"""

	Nv, Np, Ns = np.shape(lists)
	print(Nv)
	# Find correlation coefficients.
	corr = np.zeros((Np,Np))
	for row in range(Np):
		for column in range(Np):
			corr[row,column] = np.corrcoef(lists[0,row,:],lists[1,column,:])[0,1]
	
	fig, ax = plt.subplots()
	fig.subplots_adjust(bottom=0.25,left=0.25) # Make room for labels

	heatmap = ax.pcolor(corr,vmin=-1.,vmax=1.)
	cbar = plt.colorbar(heatmap)

	# Set ticks in center of cells
	ax.set_xticks(np.arange(corr.shape[1]) + 0.5, minor=False)
	ax.set_yticks(np.arange(corr.shape[0]) + 0.5, minor=False)

	# Rotate the xlabels
	ax.set_xticklabels(var_names,rotation=45,fontsize=14)
	ax.set_yticklabels(var_names,fontsize=14)

	plt.xlabel('MEAN',fontsize=16)
	plt.ylabel('VAR',rotation=90,fontsize=16)

	plt.tight_layout()
	plt.show()
	
#==================================================












