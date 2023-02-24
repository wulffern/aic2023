#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def dofft_mag(x):

    N  = len(x)
    #x = x*np.hanning(N+3)[0:N]
    yfft = np.fft.fft(x)

    M = len(yfft)
    M2 = int(M/2)
    mag = 20*np.log10(abs(yfft[1:M2]))
    return mag



nb = 13
N = 2**nb

fbin = 11
fin = 2*np.pi*fbin/N

t = np.arange(0,N,1)
amp = 1
u = amp*np.sin(fin*t)
y = np.sign(u)
e = u-y


#for i in range(0,N):





plt.subplot(3,2,1)
plt.plot(u)
plt.subplot(3,2,3)
plt.plot(y)
plt.subplot(3,2,5)
plt.plot(e)

plt.subplot(3,2,2)
plt.semilogx(dofft_mag(u))
plt.subplot(3,2,4)
plt.semilogx(dofft_mag(y))
plt.subplot(3,2,6)
plt.semilogx(dofft_mag(e))

plt.show()
