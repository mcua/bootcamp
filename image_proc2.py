#Import Modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()
sns.set_style('dark')

# Import image processing Modules
import skimage.io
import skimage.filters
import skimage.measure
import skimage.morphology
import skimage.segmentation

# Load an example phase map
phase_im  = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')
phase_bk  = skimage.filters.gaussian(phase_im, 50.0)
phase_gd  = skimage.img_as_float(phase_im) - phase_bk

# Apply Otsu Thresholding
phase_thr = skimage.filters.threshold_otsu(phase_gd)
phase_seg = phase_gd < phase_thr

# Label Bacteria
seg_lab,numcells = skimage.measure.label(phase_seg,return_num=True,background=0)

# Compute regionproperties and extract area of each object
ip_dist = 0.063 # um/Pixel
props   = skimage.measure.regionprops(seg_lab)

# Get the ares as an array
areas = np.array([prop.area for prop in props])
cutoff = 300

im_cells = np.copy(seg_lab)>0
for i,ar in enumerate(areas):
    if ar < cutoff:
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells>0)

plt.imshow(area_filt_lab,cmap=plt.cm.Spectral_r)
plt.show()
