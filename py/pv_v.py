#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

m = 1e-3
i_load = np.logspace(-5,-3)
i_load = np.linspace(1e-5,1e-3,200)

i_s = 1e-12

i_ph = 1e-3

V_T = 1.38e-23*300/1.6e-19

V_D = V_T*np.log((i_ph - i_load)/(i_s) + 1)

P_load = V_D*i_load


plt.subplot(2,1,1)
plt.plot(V_D,i_load/m)
plt.ylabel("Current load [mA]")
plt.grid()
plt.subplot(2,1,2)
plt.plot(V_D,P_load/m)
plt.xlabel("Diode voltage ")
plt.ylabel("Power Load [mW]")
plt.grid()
plt.savefig("pv.pdf")
plt.show()
