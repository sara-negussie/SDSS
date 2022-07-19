#Here is where I will gather data from SDSS via query
#Simbad: Basic data, cross-identifications, bibliography and measurements for astronomical objects outside the solar system.
#NED: NASA/IPAC Extragalactic Database. Multiwavelength data from both surveys and publications.
#SDSS: Sloan Digital Sky Survey data, including optical images, spectra, and spectral templates.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from astroquery.simbad import Simbad
from astroquery.sdss import SDSS
from astropy import coordinates as coords


#RA = 14h17m59.513s
#DEC = +25d08m12.45
#pos = coords.SkyCoord('14h17m59.513s +25d08m12.45', frame='icrs')
pos = coords.SkyCoord('14h17m59.5400s +25d08m12.603s', frame='icrs')
xid = SDSS.query_region(pos, spectro=True)
imgs = SDSS.get_images(matches=xid)
print(xid)

#print(SDSS.AVAILABLE_TEMPLATES)    
print("Hello")
#from astropy.io import fits
#fits_image_filename = fits.util.get_testdata_filepath('frame-g-004670-5-0113.fits')
#hdul = fits.open(fits_image_filename)
#hdul.info() 

from astropy import coordinates as coords
from astroquery.sdss import SDSS
co = coords.SkyCoord('0h8m05.63s +14d50m23.3s')
result = SDSS.query_region(co)
imgs = SDSS.get_images(matches=result)