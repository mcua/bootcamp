# Import Modules
import glob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize
import pandas as pd
import bootcamp_utils as bu

# Image processing Modules#
sns.set()
sns.set_style('dark')

# Import image processing Modules
import skimage.io
import skimage.filters
import skimage.measure
import skimage.morphology
import skimage.segmentation

FITC_list = glob.glob('data/HG105_images/*FITC*')
phaselist = glob.glob('data/HG105_images/*phase*')

def main2():
    # Load Data
    FITC_stack  = load_tiffs_in_list(FITC_list)
    phasestack  = load_tiffs_in_list(phaselist)
    numDat      = len(FITC_stack)
    data        = []
    segStack    = []

    # Process Each Image
    for i in range(0,numDat):
        print('Processing Image #:',i,'/',numDat)
        FITC_im = FITC_stack[i]
        phaseim = phasestack[i]

        # Segment Phase Image
        segmap,numcells = proc_phase(phaseim,siz_bac=0.5)
        print('   ',numcells,' cells detected')
        segStack.append(segmap)

        # Quantify Fluorescence
        props = skimage.measure.regionprops(segmap,intensity_image=FITC_im)

        # Get mean fluorescence
        for prop in props:
            data.append(prop.mean_intensity)

    plt.hist(data,bins = 100)
    plt.show()

    return data, segStack, phasestack, FITC_stack

def hacker_stats(data):
    reps_ave,ci_ave = bu.draw_bs_reps(data,func=np.mean,sz = 10000)
    reps_std,ci_std = bu.draw_bs_reps(data,func=np.std,sz = 10000)

    dat = np.array([[reps_ave,ci_ave],[reps_std,ci_std]])
    print([np.mean(reps_ave),ci_ave])
    print([np.mean(reps_std),ci_std])

    return dat

def load_tiffs_in_list(tif_list):
    """Loads all files in list"""
    im_stack = []

    for files in tif_list:
        print('Loading ', files)
        im = skimage.io.imread(files)
        im_stack.append(im)

    return im_stack

def proc_phase(phase_im,siz_bac = 0,ip_dist=0.063):
    """
    Processes phase image:
        1.Correct for uneven illumination.
        2.Correct for "hot" or "bad" pixels in an image.
        3. Perform a thresholding operation.
        4. Remove bacteria or objects near/touching the image border.
        5. Remove objects that are too large (or too small) to be Bacteria
        6. Remove improperly segmented cells.
        7. Return a labeled segmentation mask.
    """

    # Remove background
    sigma     = len(phase_im)/25
    phase_bk  = skimage.filters.gaussian(phase_im, sigma)
    phase_gd  = skimage.img_as_float(phase_im) - phase_bk
    phase_gd  = phase_gd - phase_gd.min()

    # Filter Images
    selem     = skimage.morphology.square(3)
    phase_gd1 = skimage.filters.median(phase_gd,selem)

    # Apply Otsu Thresholding
    phase_thr = skimage.filters.threshold_otsu(phase_gd1)
    phase_seg = phase_gd1 < phase_thr

    # Label Bacteria
    seg_lab,numcells = skimage.measure.label(phase_seg,return_num=True,background=0)

    # Compute regionproperties and extract area of each object
    props   = skimage.measure.regionprops(seg_lab)

    # Get the ares as an array
    areas  = np.array([prop.area for prop in props])
    pixar  = ip_dist**2
    if siz_bac == 0:
        siz_bac = np.median(areas)/2

    pixcut = np.round( 0.9*siz_bac/pixar )

    im_cells = np.copy(seg_lab)>0
    for prop in props:
        if prop.area < pixcut or prop.eccentricity < 0.85:
            im_cells[seg_lab==prop.label] = 0

    filt_lab,numcells = skimage.measure.label(im_cells>0,return_num=True,background=0)

    # plt.close()
    # with sns.axes_style('dark'):
    #     fig, ax = plt.subplots(1, 2, figsize=(8, 5))
    #     ax[0].imshow(phase_im)
    #     ax[1].imshow(filt_lab)
    # plt.show()

    return filt_lab,numcells
