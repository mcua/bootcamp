import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# for image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters
import skimage.feature

# load images
phase_im = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im   = skimage.io.imread('data/bsub_100x_cfp.tif')

thresh   = 325
phaseThr = phase_im < thresh

selem    = skimage.morphology.square(3)
cfp_filt = skimage.filters.median(cfp_im,selem)

cfp_hist,cfp_bins = skimage.exposure.histogram(cfp_filt)

cfpThr = cfp_filt > 140

phase_thresh = skimage.filters.threshold_otsu(phase_im)
cfp_thresh   = skimage.filters.threshold_otsu(cfp_filt)
phase_otsu   = phase_im < phase_thresh
cfp_otsu     = cfp_filt < cfp_thresh

plt.close()
# plt.plot(cfp_bins,cfp_hist)
# plt.xlabel('Pixel Value')
# plt.ylabel('Counts')
with sns.axes_style('dark'):
    fig, ax = plt.subplots(1, 3, figsize=(10, 5))
    ax[0].imshow(phase_otsu, cmap=plt.cm.Greys_r)
    ax[1].imshow(cfp_otsu, cmap=plt.cm.Greys_r)
    ax[2].imshow(phase_otsu*(1-cfp_otsu),cmap=plt.cm.Greys_r)

plt.show()
#     plt.imshow(edge,cmap=plt.cm.gray)
#
# with sns.axes_style('dark'):
    # plt.imshow(cfpThr,cmap=plt.cm.viridis)

# plt.close()
# with sns.axes_style('dark'):
    # plt.imshow(cfp_filt[150:250,450:550]/cfp_filt.max(),cmap=plt.cm.viridis)

# plt.imshow(phase_im,cmap=plt.cm.viridis)

# Generate histogram
# hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
# plt.plot(bins_phase,hist_phase)
# plt.xlabel('pixel value')
# plt.ylabel('count')
