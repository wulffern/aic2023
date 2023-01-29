#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt



#- Create a time vector
N = 2**13
t = np.linspace(0,N,N)

#- Create the "continuous time" signal
fbin = 10
fm1 = 1/N*213
f1 = 1/64 - 1/N
fd = fm1
x_s = np.sin(2*np.pi*f1*t) + + 1/2**15*np.random.randn(N)

#----------------------------------------------
#- Model an ADC
#----------------------------------------------

## Sample
#- Sampling frequency is 1/nfs of the time vector
nfs = 4
x_sn = x_s[0::nfs]

def adc(x,bits):
    levels = 2**bits
    y = np.round(x*levels)/levels
    return y

# To discrete value
bits = 10
y_sn = adc(x_sn,bits)

#- Oversample
OSR = 4

def oversample(x,OSR):

    N = len(x)
    y = np.zeros(N)

    for n in range(0,N):
        for k in range(0,OSR):
            m = n+k
            if(m < N):
                y[n] += x[m]
    return y

y_on = oversample(y_sn,OSR)

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
    X = X/np.max(np.abs(X))
    return X
X_s = freqDomain(x_s)
X_sn = freqDomain(x_sn)
Y_sn = freqDomain(y_sn)
Y_on = freqDomain(y_on)

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
plt.plot(20*np.log10(np.abs(Y_on)))
plt.xlabel("Oversampled")
plt.text(np.round((1-1/4)*N/nfs),-10,"OSR=" + str(OSR))
plt.ylim(-160,0)

fig = plt.gcf()
fig.set_size_inches(12, 7)
plt.tight_layout()
plt.savefig("l6_osr_" + str(OSR) + ".pdf")
plt.show()
