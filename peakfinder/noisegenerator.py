import numpy as np

def noisegen(x,m,sd):
    """This function outputs Gaussian distributed noise for incoming data x
    First argument x := the data
    Second argument m:= the mean
    third argument sd:= the standard deviation of the Gaussian distribution from which it samples"""
    
    noise = (x + np.random.normal(m,sd,len(x)))
    return noise