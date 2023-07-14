#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

#- Create a time vector
N = 2**13
t = np.linspace(0,N,N)

#- Create the "continuous time" signal with multiple sinusoidal signals and some noise
f1 = 3023/N
fd = 1/N*119
x_s = np.sin(2*np.pi*f1*t) + 1/1024*np.random.randn(N) #+   0.5*np.sin(2*np.pi*(f1-fd)*t) + 0.5*np.sin(2*np.pi*(f1+fd)*t)

#- Create the sampling vector, and the sampled signal
t_s_unit = [1,1,0,0,0,0,0,0]
t_s = np.tile(t_s_unit,int(N/len(t_s_unit)))
x_sn = x_s*t_s

#- IIR filter
b = 0.3
a = 0.25
z = a + 1j*b
z_abs = np.abs(z)
print("|z| = " + str(z_abs))
y = np.zeros(N)
y[0] = a
for i in range(1,N):
    y[i] = b*x_sn[i-1] + y[i-1]


#- Convert to frequency domain with a hanning window to avoid FFT bin
#- energy spread
Hann = True
if(Hann):
    w = np.hanning(N+1)
else:
    w = np.ones(N+1)

#X_s = np.fft.fftshift(np.fft.fft(np.multiply(w[0:N],x_s)))
X_sn = np.fft.fftshift(np.fft.fft(np.multiply(w[0:N],x_sn)))
Y = np.fft.fftshift(np.fft.fft(np.multiply(w[0:N],y)))


plt.subplot(2,2,1)
plt.plot(x_sn)
plt.axis([1000,1400,-1,1])
plt.ylabel("Time Domain")
plt.subplot(2,2,2)
plt.plot(y)
plt.axis([1000,1400,-1,1])
plt.subplot(2,2,3)
plt.plot(20*np.log10(np.abs(X_sn)))
plt.xlabel("Sampled")
plt.ylabel("Frequency Domain")
plt.subplot(2,2,4)
plt.plot(20*np.log10(np.abs(Y)))
plt.xlabel("IIR Filter")

fig = plt.gcf()
fig.set_size_inches(10, 7)
plt.tight_layout()
plt.savefig("l5_iir.svg")
plt.show()
