footer: Carsten Wulff 2023
slidenumbers:true
autoscale:true
theme:Plain Jane,1

# TFE4188 - Introduction to Lecture 8
# Clocks and PLLs

<!--pan_title: Lecture 8 - Clocks and PLLs -->


---

# Goal

**Why** do we need to generate clocks 

Introduction to **PLLs**

---

#[fit] Why

---

![fit](../media/l10_dk.pdf)

---

![fit](../media/l10_clockic.pdf)

---

![fit](../media/logic.pdf)

---

#[fit] PLL

---

![fit](../media/l10_fb.pdf)

---

![fit](../media/l10_freq_fb.pdf)

---

## [SUN\_PLL\_SKY130NM](https://github.com/wulffern/sun_pll_sky130nm)

---

![fit](../media/l08_sun_pll.pdf)

---

#[fit]PLLs need calculation!

# \#noCowboyDesign

---

# $$ \phi(t) = 2 \pi \int_0^t f(t) dt$$

---


![fit](../media/l10_pll_sm.pdf)

---

$$ \frac{\phi_d}{\phi_{in}} = \frac{1}{1 + L(s)}$$ 


$$ L(s) = \frac{ K_{osc} K_{pd} K_{lp} H_{lp}(s) }{N s} $$


![left fit](../media/l10_pll_sm.pdf)

---

# $$K_{osc} = 2 \pi\frac{ df}{dV_{cntl}}$$

![right fit](../media/l10_pll_kvco.pdf)

---

[.column]

--
--
--

# $$ K_{pd} = \frac{I_{cp}}{2 \pi} $$

[.column]

--
--
--

$$ K_{pd} = \frac{100\text{ nA}}{2 \pi}$$

---

 $$ K_{lp}H_{lp}(s)= K_{lp}\left(\frac{1}{s} + \frac{1}{\omega_z}\right) $$

 $$ K_{lp}H_{lp}(s) = \frac{1}{s(C_1 + C_2)}\frac{1 + s R C_1}{1 +
sR\frac{C_1C_2}{C_1 + C_2}}$$



![right fit](../media/l10_lpf.pdf)

---
[.column]

--
--
--
--

$$ L(s) = \frac{ K_{osc} K_{pd} K_{lp} H_{lp}(s) }{N s} $$

[.column]


[sun\_pll\_sky130nm/py/pll.py](https://github.com/wulffern/sun_pll_sky130nm/blob/main/py/pll.py)

```python
#- Loop Model
f = np.logspace(-4,10)

s = 1j*2*np.pi*f

#- See sim/RCOSC
Kvco = 2*np.pi*1.6e9

#- Current divided by 2 pi
Kpd = 1e-6/(2*np.pi)

R = 32e3*5
C1 = 6.024e-12
C2 = 0.33e-12

Klp = 1/C1

N = 32

wpll = np.sqrt(Kpd*Klp*Kvco/N)
wz = 1/(R*C1)
w3db = wpll**2/wz

Q = wz/wpll

KlpHlp = 1/np.multiply((C1 + C2),s)* \
    (1 + np.multiply(s,(R*C1)))/(1 + np.multiply(s,R*(C1*C2)/(C1 + C2)))

```
---

![fit](../media/pll.pdf)

---

![fit](../media/tran_SchGtKttTtVt.pdf)

---

#[fit] JSSC PLLs

---

![fit](../ip/l10_jssc_pll1.pdf)

---

![fit](../ip/l10_jssc_pll1_1.pdf)

---

![fit](../ip/l10_jssc_pll2_0.pdf)

---

![fit](../ip/l10_jssc_pll2_1.pdf)

---

![fit](../ip/l10_jssc_pll3_0.pdf)

---

![fit](../ip/l10_jssc_pll3_1.pdf)

---



#[fit] Thanks!


