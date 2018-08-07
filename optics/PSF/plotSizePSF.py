#!/usr/bin/python

import os.path
import os
import numpy as np
import matplotlib as mlp
from matplotlib import pyplot as plt
from scipy import optimize
import math

def checkDatFile(datFileName):
    if not os.path.isfile(datFileName):
        print (datFileName + " is not a file!\n")
        return False
    return True

def plotSizePDF(telNow, newDatFileName):

    if not checkDatFile(newDatFileName):
        return

    newDatFile = open(newDatFileName, 'r')
    newData = np.loadtxt(newDatFile, usecols=(0,1))

    xTitle = 'Off-axis angle [$^{\circ}$]'
    yTitle = 'PSF [cm]'

    plt.plot(newData[:,0], newData[:,1], '-o', color='mediumblue', linewidth=2.0, label='New (10/04/18)')
    plt.xlabel(xTitle, fontsize=18, labelpad=0)
    plt.ylabel(yTitle, fontsize=18)
    plt.tick_params(axis='both', which='major', labelsize=15)

    plt.title('%s PSF (80%% contaiment radius)' % (telNow), fontsize=15, y=1.02)
    legend = plt.legend(loc='upper left', shadow=False, fontsize='x-large')
    plt.grid(True)
    plt.gca().set_axisbelow(True)
    plt.tight_layout()
    plt.savefig("PSF" + "-" + telNow + ".pdf")

    plt.close('all')

if __name__ == '__main__':

    cwd = os.getcwd()
    telNow = cwd.split('/')[len(cwd.split('/')) - 2]
    plotSizePDF('SST-2M-GCT', 
                            'psf-size-GCT.txt')



