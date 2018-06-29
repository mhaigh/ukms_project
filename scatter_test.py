import numpy as np
from scatter_plotting import scatterplot, corr

lists = np.random.rand(2,6,29)
#var_names = ['pressure','temp','wind speed']
var_names = ['a','b','c','d','e','f']

scatterplot(lists,var_names)
corr(lists,var_names)
