"Function to plot UK topography from MOGREPS data"

def plot_topo():
    
    topo = data_set['surface_altitude']
    xdim,ydim = np.shape(r)
    scale = 50.
    cm = 'binary'

    plt.figure(figsize=(xdim/scale,ydim/scale))
    plt.pcolormesh(r,cmap=cm)
    plt.axis('off')
    plt.savefig('topo.png')
    