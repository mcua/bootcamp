# Import Modules
import glob
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize

# sns.set()
sns.set_style('dark')

# Import image processing Modules
import skimage.io
import skimage.filters
import skimage.measure
import skimage.morphology
import skimage.segmentation

# Get tif files
tif_list = glob.glob('data/bacterial_growth/bacillus*.tif')
framePer = 15; #minutes
ip_dist  = 0.0645 #µm

def main():
    """Loads in data from tif_list, and quantifies amount of bacteria per image"""
    im_stack  = load_files_in_list(tif_list)
    n_timepts = len(im_stack)
    seg_stack = []
    num_bac   = np.empty(n_timepts)

    # Get # Bacteria
    for ind,im in enumerate(im_stack):
        seg = detect_bacteria(im)
        nb  = count_bacteria_area(seg)
        seg_stack.append(seg)
        num_bac[ind] = nb

    # Add Curve Fit
    timevec = np.arange(0,55*15,15)
    a0      = 665
    rate    = 0.004
    bckgnd  = num_bac[0]
    p0      = [a0,rate]
    logp, _ = scipy.optimize.curve_fit(exp_logmodel,timevec, num_bac, p0=np.log(p0))
    p       = np.exp(logp)
    datfit  = exp_model(timevec,*tuple(p))
    # Plots Results

    plt.figure(1)
    plt.plot(timevec,num_bac,marker ='*',linestyle='none')
    plt.plot(timevec,datfit,color='gray')
    plt.xlabel('Time (min)')
    plt.ylabel('Total Bacteria Area (µm$^2$)')
    ind    = int( n_timepts//2)
    segmap = seg_stack[ind]
    im_rgb = np.dstack(3 * [im_stack[ind] / im_stack[ind].max()])
    im_rgb[segmap, 1] = segmap[segmap]

    # Show the result
    with sns.axes_style('dark'):
        fig, ax = plt.subplots(3, 3)
        plots = np.round(np.linspace(0,54,9))
        for i in range(0,3):
            for j in range(0,3):
                ind = int(plots[i*3+j])

                # Build RGB image by stacking grayscale images
                segmap = seg_stack[ind]
                im_rgb = np.dstack(3 * [im_stack[ind] / im_stack[ind].max()])
                im_rgb[segmap, 1] = segmap[segmap]

                # Add Scale Bar

                ax[i][j].imshow(im_rgb)

                if i == 0 and j == 0:
                    scalebar_len = 10
                    scalebar_pix = scalebar_len/ip_dist
                    r,c,_ = np.shape(im_rgb)
                    cst   = np.round(c*0.9-scalebar_pix)
                    cen   = np.round(c*0.9)
                    ax[i][j].plot([cst,cen],[0.9*r]*2,color='w')

                ax[i][j].set_title('Frame #: ' + str(ind))
                ax[i][j].axis('off')
        fig.tight_layout()

    plt.show()
    return seg_stack, num_bac, p

def exp_logmodel(x,log_a0,log_rate):
    a0,rate = np.exp([log_a0,log_rate])
    return exp_model(x,a0,rate)

def exp_logdata(x,log_a0,rate):
    """Fits on the log of the values"""
    return log_a0 + x*rate

def exp_model(x,a0,rate):
    """Models bacterial growth"""
    return a0*np.exp(x*rate)

def count_bacteria_area(seg,ip_dist = 0.0645):
    """Count area of Bacteria in segmented image"""
    return np.sum(seg)*(0.645**2)

def detect_bacteria(im):
    """Separates bacteria from background in image"""
    thr = skimage.filters.threshold_otsu(im)
    seg = im > thr

    return seg

def load_files_in_list(tif_list):
    """Loads all files in list"""
    im_stack = []

    for files in tif_list:
        print('Loading ', files)
        im = skimage.io.imread(files)
        im_stack.append(im)

    return im_stack
