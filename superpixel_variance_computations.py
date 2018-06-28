"""

Functions for analysing the ensemble variability in averages of properties across the superpixels.

"""

def Get_Super_Pixel_STDs(variable,segments) : 

    """
    
    Given a segmentation into superpixels we compute the variance
    in a given variable across ensemble members for each superpixel.
    
    We then return the variance across the
    
    """

    #variable = 'air_temperature'


    STD_Vals = [ ]
    Variance_Vals = [ ]

    for PIXEL in range(np.max(segments)):

        #Loop over ensembles within a superpixel: 
        num_ensemble_members = 12   
        Averages_in_this_pixel = [ ]

        print("Pixel = " + str(PIXEL))

        for i in range(num_ensemble_members) : 
            f = mogreps.download_data('mogreps-uk', mogreps.make_data_object_name('mogreps-uk',2013,2,1,3,i,3),data_folder=Path('.')  )
            data_set = netCDF4.Dataset(f)
            average_for_this_ensemble_member_in_this_super_pixel = np.mean( data_set.variables[variable][0][0].data[segments==PIXEL]) 
            Averages_in_this_pixel.append(average_for_this_ensemble_member_in_this_super_pixel)

        #compute the varaiance for this superpixel:

        Variance_for_this_pixel = np.var(Averages_in_this_pixel)
        STD_for_this_pixel = np.std(Averages_in_this_pixel)
        STD_Vals.append(STD_for_this_pixel)
        Variance_Vals.append(Variance_for_this_pixel)
        
    return STD_Vals ,Variance_Vals 




STD_Vals ,Variance_Vals  = Get_Super_Pixel_STDs('air_temperature',segments)
