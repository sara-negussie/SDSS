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

"""
#RA = 14h17m59.513s
#DEC = +25d08m12.45
#pos = coords.SkyCoord('14h17m59.513s +25d08m12.45', frame='icrs')
pos = coords.SkyCoord('14h17m59.5400s +25d08m12.603s', frame='icrs')
xid = SDSS.query_region(pos, spectro=True)
imgs = SDSS.get_images(matches=xid)
print(xid)
"""
#print(SDSS.AVAILABLE_TEMPLATES)    
print("Hello")
#from astropy.io import fits
#fits_image_filename = fits.util.get_testdata_filepath('frame-g-004670-5-0113.fits')
#hdul = fits.open(fits_image_filename)
#hdul.info() 

"""
from astropy import coordinates as coords
from astroquery.sdss import SDSS
co = coords.SkyCoord('0h8m05.63s +14d50m23.3s')
result = SDSS.query_region(co)
imgs = SDSS.get_images(matches=result)

"""


from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
#plt.style.use(astropy_mpl_style)

#print(np.size('NGC5548.fits'))
#fits_image_filename = fits.util.get_testdata_filepath('NGC5548.fits')
#image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
image_file = get_pkg_data_filename('testcoor.fits')
fits.info(image_file)
image_data = fits.getdata(image_file, ext=0)
print(image_data.shape)
plt.figure()
plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.show()

"""
hdul = fits.open('NGC5548.fits')
hdul.info()
data = hdul[1].data
"""



""""

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
#plt.style.use(astropy_mpl_style)

#print(np.size('NGC5548.fits'))
#fits_image_filename = fits.util.get_testdata_filepath('NGC5548.fits')
#image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
image_file = get_pkg_data_filename('NGC5548.fits')
fits.info(image_file)
image_data = fits.getdata(image_file, ext=0)
print(image_data.shape)
plt.figure()
plt.imshow(image_data, cmap='gray')
plt.colorbar()

"""
hdul = fits.open('NGC5548.fits')
hdul.info()
data = hdul[1].data
"""



"""