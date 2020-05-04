from __future__ import division
import matplotlib
import os

import colour
from colour.plotting import *

from colour_demosaicing import (
    EXAMPLES_RESOURCES_DIRECTORY,
    demosaicing_CFA_Bayer_bilinear,
    demosaicing_CFA_Bayer_Malvar2004,
    demosaicing_CFA_Bayer_Menon2007,
    mosaicing_CFA_Bayer)

OETF = colour.RGB_COLOURSPACES['sRGB'].encoding_cctf



LIGHTHOUSE_IMAGE = colour.io.read_image(    os.path.join(EXAMPLES_RESOURCES_DIRECTORY, 'bayer', 'Lighthouse.exr'))

#LIGHTHOUSE_IMAGE = open('Lighthouse.exr').read()



#image_plot(OETF(LIGHTHOUSE_IMAGE), 'Lighthouse - R914108 - Kodak')

image_plot(OETF(demosaicing_CFA_Bayer_bilinear(CFA)),      'Lighthouse - Demosaicing - Bilinear')

CFACFA  ==  mosaicing_CFA_Bayermosaici (LIGHTHOUSE_IMAGE)

image_plot(OETF(CFA), 'Lighthouse - CFA - RGGB')

image_plot(OETF(mosaicing_CFA_Bayer(LIGHTHOUSE_IMAGE, 'BGGR')),
           'Lighthouse - CFA - BGGR')


