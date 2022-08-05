from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
#plt.style.use(astropy_mpl_style)

#print(np.size('NGC5548.fits'))
#fits_image_filename = fits.util.get_testdata_filepath('NGC5548.fits')
"""image_file = get_pkg_data_filename('tutorials/FITS-images/HorseHead.fits')
fits.info(image_file)
image_data = fits.getdata(image_file, ext=0)
print(image_data.shape)
plt.figure()
plt.imshow(image_data, cmap='gray')
plt.colorbar()
plt.show()"""

from astroquery.simbad import Simbad
result_table = Simbad.query_object("NGC5548")
print(result_table)

"""
hdul = fits.open('NGC5548.fits')
hdul.info()
data = hdul[1].data
"""


from astroquery.simbad import Simbad
import astropy.units as u
result_table = Simbad.query_region("m81", radius=0.1 * u.deg)
# another way to specify the radius.
result_table = Simbad.query_region("m81", radius='0d6m0s')
print(result_table)


"""


SELECT
   m.ra AS ra1, m.dec AS dec1,
   n.objid, n.distance,
   o.ra AS ra2, o.dec AS dec2
FROM MyDB.MyRAandDEC AS m
   CROSS APPLY dbo.fGetNearestObjEq( m.ra, m.dec, 0.5) AS n
   JOIN PhotoObj AS o ON n.objid=o.objid


"""


"""
SELECT
   m.ra AS ra1, m.dec AS dec1,
   n.objid, n.distance, n.modelMag_g, n.modelMag_r, n.modelMag_i, n.cModelMag_g, n.cModelMag_r, n.cModelMag_i, n.petroMag_g, n.petroMag_r, n.petroMag_i, n.petroRad_g, n.petroRad_r, n.petroRad_i, 
   o.ra AS ra2, o.dec AS dec2
FROM MyDB.MyRAandDEC AS m
   CROSS APPLY dbo.fGetNearestObjEq( m.ra, m.dec, 0.5) AS n
   JOIN PhotoObj AS o ON n.objid=o.objid
"""