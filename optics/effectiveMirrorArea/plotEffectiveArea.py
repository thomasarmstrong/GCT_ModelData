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

def plotEffectiveArea(telNow, newDatFileName):

    if not checkDatFile(newDatFileName):
        return

    newDatFile = open(newDatFileName, 'r')
    newData = np.loadtxt(newDatFile)

    xTitle = 'Off-axis angle [$^{\circ}$]'
    yTitle = 'Effective mirror area [$m^2$]'

    plt.plot(newData[:,0], newData[:,1], '-o', color='mediumblue', linewidth=2.0, label='With structure (10/04/18)')
    plt.xlabel(xTitle, fontsize=18, labelpad=0)
    plt.ylabel(yTitle, fontsize=18)
    plt.tick_params(axis='both', which='major', labelsize=15)

    plt.plot(newData[:,2], newData[:,3], '-^', color='orange', linewidth=2.0, label='Without structure (10/04/18)')
    plt.xlabel(xTitle, fontsize=18, labelpad=0)
    plt.ylabel(yTitle, fontsize=18)
    plt.tick_params(axis='both', which='major', labelsize=15)

    # sim_telarray parameterization
    # projectedMirrorArea = 9.2
    # theta = np.arange(min(newData[:,0]), max(newData[:,0]), 0.01)
    # pars = [0.881, 1, 0.0131, 2.06, 1.66]
    # r3 = (pars[3]*np.pi)/180
    # effectiveMirrorArea = projectedMirrorArea*pars[0]/(1. + pars[2]*np.power(np.sin(np.deg2rad(theta))/r3, pars[4]))
    # plt.plot(theta, effectiveMirrorArea, '--', color='orange', linewidth=3.0, label='sim_telarray parameterization')

    plt.title('%s effective mirror area' % (telNow), fontsize=15, y=1.02)
    legend = plt.legend(loc='lower left', shadow=False, fontsize='x-large')
    plt.grid(True)
    plt.gca().set_axisbelow(True)
    plt.tight_layout()
    plt.savefig("effectiveMirrorArea" + "-" + telNow + ".pdf")

    plt.close('all')

if __name__ == '__main__':

    cwd = os.getcwd()
    telNow = cwd.split('/')[len(cwd.split('/')) - 2]
    plotEffectiveArea('SST-2M-GCT', 
                            'effective-area-GCT-comparison.txt')



