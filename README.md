#UKMS Project

##

###

Project overview
-----------------

This mini project aims to develop an understanding of the spatial dependence of weather predicatability in the UK region. The idea is to decompose the area of the UK into "superpixels", each containing a relatively homogeneous area with respect to some meteorological property. Statistical techniques are then applied on the set of superpixels (superpixel-mean MOGREPS data) in order to understand what determines unpredictability in and around the UK. 


Python Notebook files
----------------------

- slic.ipynb 

This notebook is used to spatially decompose the UK into superpixel segments. The segmentation clusters pixels by taking into account pixel proximity in addition to certain physical properties. For example, an initial decomposition may cluster pixels by proximity and topography height. 

- visualisedata.ipynb

The role of this notebook is to look at variances of certain physical properties (e.g. air temperature, pressurre...) and how these depend on the superpixel segmentation. We concentrate on the number of segments in the decomposition.

- Mogreps_Presentation.ipynb

Here methods and results are collated into a presentation-style notebook. 
