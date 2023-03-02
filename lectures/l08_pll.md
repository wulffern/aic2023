footer: Carsten Wulff 2023
slidenumbers:true
autoscale:true
theme:Plain Jane,1

<!--pan_skip: -->

## TFE4188 - Introduction to Lecture 8
# Clocks and PLLs

<!--pan_title: Lecture 8 - Clocks and PLLs -->


---

<!--pan_doc:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Vahp2tsGWIQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

-->


# Goal

**Why** do we need to generate clocks 

Introduction to **PLLs**

---

#[fit] Why

---

1. 32 MHz crystal

2. 32 KiHz crystal

3. In PCB antenna

4. DC/DC inductor 


![left](../media/l10_dk.pdf)


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

![fit](../media/l08_sun_pll.pdf)

---

#[fit]PLLs need calculation!

# \#noCowboyDesign

---

$$ \phi(t) = 2 \pi \int_0^t f(t) dt$$

---


![left fit](../media/l10_pll_sm.pdf)

# PLLs are assumed to be linear in phase


$$ \frac{\phi_d}{\phi_{in}} = \frac{1}{1 + L(s)}$$ 


$$ L(s) = \frac{ K_{osc} K_{pd} K_{lp} H_{lp}(s) }{N s} $$



---

# Voltage controlled oscillator

$$K_{osc} = 2 \pi\frac{ df}{dV_{cntl}}$$

![right fit](../media/SUN_PLL_ROSC.pdf)

---

## [SUN\_PLL\_SKY130NM/sim/ROSC/](https://github.com/wulffern/sun_pll_sky130nm/tree/main/sim/ROSC)

![right fit](../media/SUN_PLL_ROSC_KVCO.pdf)

---

# Phase detector and charge pump



$$ K_{pd} = \frac{I_{cp}}{2 \pi} $$


![right fit](../media/SUN_PLL_CP.pdf)

---

# Loop filter

 
$$ K_{lp}H_{lp}(s)= K_{lp}\left(\frac{1}{s} + \frac{1}{\omega_z}\right) $$

$$ K_{lp}H_{lp}(s) = \frac{1}{s(C_1 + C_2)}\frac{1 + s R C_1}{1 +
sR\frac{C_1C_2}{C_1 + C_2}}$$



![right fit](../media/SUN_PLL_LP.pdf)

---

# Divider 

$$ K_{div} = \frac{1}{N}$$


![right fit](../media/SUN_PLL_DIV.pdf)


---
[.column]


## Loop function

$$ L(s) = \frac{ K_{osc} K_{pd} K_{lp} H_{lp}(s) }{N s} $$

[.column]


## Python model

[sun\_pll\_sky130nm/py/pll.py](https://github.com/wulffern/sun_pll_sky130nm/blob/main/py/pll.py)

---

![fit](../media/pll.pdf)

---

![fit](../media/tran_SchGtKttTtVt.pdf)

---

## [SUN\_PLL\_SKY130NM](https://github.com/wulffern/sun_pll_sky130nm)

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


