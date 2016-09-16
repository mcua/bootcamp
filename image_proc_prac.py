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

def proc_fluorescence(file):


def proc_phase_im(filename,siz_bac = 0,ip_dist=0.063):
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

    phase_im  = skimage.io.imread(filename)

    # Remove background
    sigma     = len(phase_im)/25
    phase_bk  = skimage.filters.gaussian(phase_im, sigma)
    phase_gd  = skimage.img_as_float(phase_im) - phase_bk

    # Apply Otsu Thresholding
    phase_thr = skimage.filters.threshold_otsu(phase_gd)
    phase_seg = phase_gd < phase_thr

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

    plt.close()
    with sns.axes_style('dark'):
        fig, ax = plt.subplots(1, 2, figsize=(8, 5))
        ax[0].imshow(phase_im)
        ax[1].imshow(filt_lab)
    plt.show()

    return filt_lab,numcells
