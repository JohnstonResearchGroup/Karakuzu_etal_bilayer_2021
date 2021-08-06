# by Seher Karakuzu

# %%
import sys
import os
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from scipy import linalg
from scipy.optimize import minimize
from numpy.linalg import inv

from scipy.interpolate import *
from mpl_toolkits.axes_grid1 import make_axes_locatable

from matplotlib import pyplot as plt
from matplotlib import cm

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']


akw = np.loadtxt("./Akw_n0pt85_tp2pt8.txt") #, usecols = range(0,33))
omega = np.loadtxt("./omega_n0pt85_tp2pt8.txt") #, usecols = range(0,33))
nkSeg = 80
nktot = 3*nkSeg

akw_blk = np.loadtxt("./Akw_n0pt9_tp2pt3.txt") #, usecols = range(0,33))
omega_blk = np.loadtxt("./omega_n0pt9_tp2pt3.txt") #, usecols = range(0,33))

print("shape of akw: ",akw.T.shape)
# %%
fig, (ax1,ax2)= plt.subplots(1,2,figsize=(10,6),sharex=True, sharey=True)

import matplotlib.colors as co
im = ax2.imshow(akw.T,origin='lower',aspect='auto',extent=(0,nktot,omega.min(),omega.max()),norm=co.LogNorm(vmin=1.0e-3, vmax=akw.max()),cmap='jet')
ax2.set(ylim=(-10,15))

ax2.set(xticks=[0,nkSeg,2*nkSeg,3*nkSeg],xticklabels=[r"$\Gamma$","M","X",r"$\Gamma$"])

ax2.set_xlabel('$k$', fontsize=28)
ax1.set_ylabel(r"$\omega$", fontsize=28)

ax2.grid(True,lw=0.25)
ax2.axhline(y=0,color="red",lw=1,linestyle="-")

im_1 = ax1.imshow(akw_blk.T,origin='lower',aspect='auto',extent=(0,nktot,omega_blk.min(),omega_blk.max()),norm=co.LogNorm(vmin=1.0e-3, vmax=akw_blk.max()),cmap='jet')
ax1.set(ylim=(-10,15))

ax1.set(xticks=[0,nkSeg,2*nkSeg,3*nkSeg],xticklabels=[r"$\Gamma$","M","X",r"$\Gamma$"])
ax1.grid(True,lw=0.25)
ax1.axhline(y=0,color="red",lw=1,linestyle="-")
ax1.set_xlabel('$k$', fontsize=28)

divider = make_axes_locatable(ax2)
cax = divider.append_axes('right', size='5%', pad=0.05)
fig.colorbar(im, cax=cax, orientation='vertical');
cax.tick_params(labelsize=15)

divider = make_axes_locatable(ax1)
cax = divider.append_axes('right', size='5%', pad=0.05)
cb1 = fig.colorbar(im_1, cax=cax, orientation='vertical')
cax.tick_params(labelsize=15)


ax2.tick_params(labelsize=20)
ax1.tick_params(labelsize=20)


fig.tight_layout()
plt.show()

