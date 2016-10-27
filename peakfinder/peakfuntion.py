import numpy as np
#import matplotlib.pyplot as plt
from math import pi, e
import peakutils

from scipy.signal import find_peaks_cwt

#cb = np.array([-0.010223, ... ])
#indexes = find_peaks_cwt(cb, np.arange(1, 550))

def myfind_peak(xdata,ydata, min_height, min_dis):
    """this functions should get the data as an x vector and a y vector
    and return the vector with the indexes and the position in x (x[indexes]) of all the peaks in de signal y
    """
    indexes=peakutils.indexes(ydata,thres=min_height, min_dist=min_dis)
    return indexes,xdata[indexes]
    