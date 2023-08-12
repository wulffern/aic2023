#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

#- Create a time vector
N = 2**13
t = np.linspace(0,N,N)

#- Create the "continuous time" signal
fbin = 10
fm1 = 1/N*213
f1 = 1/128 - 1/N
fd = fm1
x_s = np.sin(2*np.pi*f1*t) + + 1/2**15*np.random.randn(N)

#----------------------------------------------
#- Model an ADC
#----------------------------------------------

## Sample
#- Sampling frequency is 1/nfs of the time vector
nfs = 4
x_sn = x_s[0::nfs]

bits = 1
y_sn = np.round(x_sn*2**bits)/2**bits

dither = 1
M = len(x_sn)
y_sd = np.zeros(M)
x = np.zeros(M)
for n in range(1,M):
    x[n] = x[n-1] + (x_sn[n]-y_sd[n-1])
    y_sd[n] = np.round(x[n]*2**bits  + dither*np.random.randn()/4)/2**bits

#- Remove the first samples to get rid of the initial
# settling
y_sd = y_sd[2:]

#----------------------------------------------
# Plot spectrum
#----------------------------------------------
def freqDomain(x):
    N = len(x)
    # Use hanning window to prevent FFT bin energy spread
    w = np.hanning(N+1)

    # Convert to frequency domain
    X= np.fft.fftshift(np.fft.fft(np.multiply(w[0:N],x)))

    # Normalize to max output power
    X = X/np.max(np.abs(X[int(N/4):N-int(N/4)]))
    return X
X_s = freqDomain(x_s)
X_sn = freqDomain(x_sn)
Y_sn = freqDomain(y_sn)
Y_sdn = freqDomain(y_sd )

plt.subplot(1,4,1)
plt.plot(20*np.log10(np.abs(X_s)))
plt.xlabel("Continuous time, continuous value")
plt.ylabel("Frequency Domain")
plt.ylim(-160,0)
plt.subplot(1,4,2)
plt.plot(20*np.log10(np.abs(X_sn)))
plt.xlabel("Discrete time, continuous value")
plt.ylim(-160,0)
plt.subplot(1,4,3)
plt.plot(20*np.log10(np.abs(Y_sn)))
plt.xlabel("Discrete time, Discrete value")
plt.text(np.round((1-1/4)*N/nfs),-10,str(bits) + "-bit")

plt.ylim(-160,0)
plt.subplot(1,4,4)
plt.plot(20*np.log10(np.abs(Y_sdn)))
#plt.plot(y_sd)
plt.xlabel("Noise-shaped")
plt.text(np.round((1-1/2)*N/nfs),-150,"dither=" + str(dither))
plt.ylim(-160,0)

fig = plt.gcf()
fig.set_size_inches(12, 7)
plt.tight_layout()
plt.savefig(f"l6_sd_d{dither}_b{bits}.pdf")
plt.show()
