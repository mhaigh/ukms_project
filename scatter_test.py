import numpy as np
from scatter_plotting import scatterplot, corr

lists = np.random.rand(2,3,29)
var_names = ['pressure','temp','wind speed']

scatterplot(lists,var_names)
corr(lists,var_names)
