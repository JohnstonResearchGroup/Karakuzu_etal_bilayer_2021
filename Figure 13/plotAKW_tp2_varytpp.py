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


akw = np.loadtxt("Akw_tpp0.0.txt") #, usecols = range(0,33))
omega = np.loadtxt("omega_tpp0.0.txt") #, usecols = range(0,33))
nkSeg = 80
nktot = 3*nkSeg

akw1 = np.loadtxt("Akw_tpp0.3.txt") #, usecols = range(0,33))
omega1 = np.loadtxt("omega_tpp0.3.txt") #, usecols = range(0,33))

akw2 = np.loadtxt("Akw_tpp0.6.txt") #, usecols = range(0,33))
omega2 = np.loadtxt("omega_tpp0.6.txt") #, usecols = range(0,33))

akw3 = np.loadtxt("Akw_tpp0.9.txt") #, usecols = range(0,33))
omega3 = np.loadtxt("omega_tpp0.9.txt") #, usecols = range(0,33))


print("shape of akw: ",akw.T.shape)
# %%
fig, ((ax2,ax1,ax3,ax4))= plt.subplots(1,4,figsize=(16,6),sharex=True, sharey=True)

import matplotlib.colors as co
im = ax2.imshow(akw.T,origin='lower',aspect='auto',extent=(0,nktot,omega.min(),omega.max()),norm=co.LogNorm(vmin=1.0e-3, vmax=akw.max()),cmap='jet')
ax2.set(ylim=(-10,15))

ax2.set(xticks=[0,nkSeg,2*nkSeg,3*nkSeg],xticklabels=[r"$\Gamma$","M","X",r"$\Gamma$"])
ax2.set_xlabel('$k$', fontsize=28)
ax2.set_ylabel(r"$\omega/t$", fontsize=28)


ax2.grid(True,lw=0.25)
ax2.axhline(y=0,color="red",lw=1,linestyle="-")

im_1 = ax1.imshow(akw1.T,origin='lower',aspect='auto',extent=(0,nktot,omega1.min(),omega1.max()),norm=co.LogNorm(vmin=1.0e-3, vmax=akw1.max()),cmap='jet')
ax1.set(ylim=(-10,15))

ax1.set(xticks=[0,nkSeg,2*nkSeg,3*nkSeg],xticklabels=[r"$\Gamma$","M","X",r"$\Gamma$"])
ax1.grid(True,lw=0.25)
ax1.axhline(y=0,color="red",lw=1,linestyle="-")
ax1.set_xlabel('$k$', fontsize=28)

im_2 = ax3.imshow(akw2.T,origin='lower',aspect='auto',extent=(0,nktot,omega2.min(),omega2.max()),norm=co.LogNorm(vmin=1.0e-3, vmax=akw2.max()),cmap='jet')
ax3.set(ylim=(-10,15))

ax3.set(xticks=[0,nkSeg,2*nkSeg,3*nkSeg],xticklabels=[r"$\Gamma$","M","X",r"$\Gamma$"])

ax3.set_xlabel('$k$', fontsize=28)

ax3.grid(True,lw=0.25)
ax3.axhline(y=0,color="red",lw=1,linestyle="-")


im_3 = ax4.imshow(akw3.T,origin='lower',aspect='auto',extent=(0,nktot,omega3.min(),omega3.max()),norm=co.LogNorm(vmin=1.0e-3, vmax=akw3.max()),cmap='jet')
ax4.set(ylim=(-10,15))

ax4.set(xticks=[0,nkSeg,2*nkSeg,3*nkSeg],xticklabels=[r"$\Gamma$","M","X",r"$\Gamma$"])

ax4.set_xlabel('$k$', fontsize=28)

ax4.grid(True,lw=0.25)
ax4.axhline(y=0,color="red",lw=1,linestyle="-")






ax1.set_xlabel('$k$', fontsize=28)



divider = make_axes_locatable(ax2)
cax = divider.append_axes('right', size='5%', pad=0.05)
fig.colorbar(im, cax=cax, orientation='vertical');
cax.tick_params(labelsize=15)

divider = make_axes_locatable(ax1)
cax = divider.append_axes('right', size='5%', pad=0.05)
cb1 = fig.colorbar(im_1, cax=cax, orientation='vertical')
cax.tick_params(labelsize=15)

divider = make_axes_locatable(ax3)
cax = divider.append_axes('right', size='5%', pad=0.05)
cb2 = fig.colorbar(im_2, cax=cax, orientation='vertical')
cax.tick_params(labelsize=15)

divider = make_axes_locatable(ax4)
cax = divider.append_axes('right', size='5%', pad=0.05)
cb3 = fig.colorbar(im_3, cax=cax, orientation='vertical')
cax.tick_params(labelsize=15)






ax2.tick_params(labelsize=20)
ax1.tick_params(labelsize=20)
ax3.tick_params(labelsize=20)
ax4.tick_params(labelsize=20)

ax2.text(5.6, -9.0, r"$t_{\perp}^{\prime} = 0.0 $", fontsize=18)
ax1.text(5.6, -9.0, r"$t_{\perp}^{\prime} = 0.3t$", fontsize=18)
ax3.text(5.6, -9.0, r"$t_{\perp}^{\prime} = 0.6t$", fontsize=18)
ax4.text(5.6, -9.0, r"$t_{\perp}^{\prime} = 0.9t$", fontsize=18)

fig.tight_layout()
plt.show()

