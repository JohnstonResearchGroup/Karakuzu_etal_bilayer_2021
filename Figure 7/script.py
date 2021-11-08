import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import h5py
import sys
import os
from matplotlib.pyplot import *

iQ=16

data_n0pt95_tp2pt3 = np.loadtxt("Gbetahalf_n0pt95_tp2pt3.txt"+str(iQ))
data_n0pt9_tp2pt3 = np.loadtxt("Gbetahalf_n0pt9_tp2pt3.txt"+str(iQ))
data_n0pt85_tp2pt8 = np.loadtxt("Gbetahalf_n0pt85_tp2pt8.txt"+str(iQ))
data_n0pt85_tp2pt3 = np.loadtxt("Gbetahalf_n0pt85_tp2pt3.txt"+str(iQ))

b = np.loadtxt("beta.txt")
b_shrt = b[:9]


prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
fig1,ax1 = plt.subplots(figsize=(8,6))

ax1.plot(1./b_shrt,data_n0pt95_tp2pt3, color=colors[0],label=r"$n=1.05,t_{\perp}=2.3t,t_{\perp}^{\prime}=0.0$",marker='p',linestyle='dashed',linewidth=2)
ax1.plot(1./b,data_n0pt9_tp2pt3, color=colors[1],label=r"$n=1.10,t_{\perp}=2.3t,t_{\perp}^{\prime}=0.0$",marker='p',linestyle='dashed',linewidth=2)
ax1.plot(1./b,data_n0pt85_tp2pt3, color=colors[2],label=r"$n=1.15,t_{\perp}=2.3t,t_{\perp}^{\prime}=0.0$",marker='p',linestyle='dashed',linewidth=2)
ax1.plot(1./b,data_n0pt85_tp2pt8, color=colors[3],label=r"$n=1.15,t_{\perp}=2.8t,t_{\perp}^{\prime}=0.0$",marker='p',linestyle='dashed',linewidth=2)
ax1.set_xlabel(r'$T/t$',fontsize=18)
ax1.set_ylabel(r"$\bar{G}({\bf K}=(0,0,\pi), \tau=\beta/2)$",fontsize=18)
ax1.tick_params(labelsize=18)
ax1.set_ylim([0.0,0.50])

ax1.legend(frameon=True,fontsize=14)

plt.show()


