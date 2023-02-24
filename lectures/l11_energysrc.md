footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme:Plain Jane,1

# TFE4188 - Lecture 11
# Energy Sources

---
# Housekeeping


[Syllabus](https://github.com/wulffern/aic2022/blob/main/syllabus.md)


---


| Week | Book                 | Monday                                                                       | Project plan             | Exercise |
|------|----------------------|------------------------------------------------------------------------------|--------------------------|----------|
| 2    | CJM 1-6              | Course intro, what I expect you to know, project, analog design fundamentals | Specification            |          |
| 3    | Slides               | ESD and IC Input/Output                                                      | Specification            | x        |
| 4    | CJM 7,8              | Reference and bias                                                           | Specification            |          |
| 5    | CJM 12               | Analog Front-end                                                             | M1. Specification review | x        |
| 6    | CJM 11-14            | Switched capacitor circuits                                                  | Design                   |          |
| 7    | JSSC, CJM 18         | State-of-the-art ADCs                                                        | Design                   | x        |
| 8    | Slides               | Low power radio recievers                                                    | Design                   |          |
| 9    | Slides               | Communication standards from circuit perspective                             | M2. Design review        | x        |
| 10   | CJM 7.4, CFAS,+DC/DC | Voltage regulation                                                           | Layout                   |          |
| 11   | CJM 19, CFAS         | Clock generation                                                             | Layout                   | x        |
| 12   | Paper                | **Energy sources**                                                           | Layout/LPE simulation    |          |
| 13   | Slides               | Chip infrastructure                                                          | Layout/LPE simulation    | x        |
| 14   |                      | Tapeout review                                                               | M4. Tapeout review       |          |
| 15   |                      | Easter                                                                       |                          |          |
| 16   |                      | Easter                                                                       |                          |          |
| 17   |                      | Exam repetition                                                              |                          |          |

---

# Goal

**Why** do we need energy sources? 

Introduction to **Energy Harvesting**

---

#[fit] Why

---

[.column]

--
--
--
--

#[fit] Lithium Battery

[.column]

--
--
--
--

1 year $$ \Rightarrow$$ 45 $$\mu$$W/cm$$^3$$ 

10 year $$ \Rightarrow$$ 3.5 $$\mu$$W/cm$$^3$$ 

---

![fit](../ip/l11_teg2_0.pdf)

---

 ![fit](../ip/l11_teg2_1.pdf)

---

 ![fit](../ip/l11_teg2_2.pdf)

---

 ![fit](../ip/l11_eh_src.pdf)

---

## Thermoelectric
 
## Photovoltaic

## Piezoelectric

## Ambient RF

## Triboelectric 



---

#[fit] Thermoelectric

---

[Thermoelectric_effect](https://en.wikipedia.org/wiki/Thermoelectric_effect)

- Seebeck effect

- Peltier effect

- Thomson effect

![left fit](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Thermoelectric_Generator_Diagram.svg/981px-Thermoelectric_Generator_Diagram.svg.png)

---

# [Radioisotope Thermoelectric generator](https://en.wikipedia.org/wiki/Radioisotope_thermoelectric_generator)

--

![inline 120 %](https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/MHW-RTGs.gif/190px-MHW-RTGs.gif)

![left fit](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Voyager_spacecraft_model.png/1280px-Voyager_spacecraft_model.png)



---

![left fit](../media/l11_teg_mdl.pdf)

# [Thermoelectric generators](https://en.wikipedia.org/wiki/Thermoelectric_generator)

---

![fit](../ip/l11_teg1_0.pdf)

---

![fit](../ip/l11_teg1_1.pdf)

---

![fit](../ip/l11_teg1_2.pdf)

---

![fit](../ip/l11_teg1_3.pdf)

---

![fit](../ip/l11_teg1_4.pdf)

---

![fit](../ip/l11_teg1_5.pdf)

---

#[fit] Photovoltaic

---

# [Photovoltaic effect](https://en.wikipedia.org/wiki/Photovoltaic_effect)

![left fit](../media/l11_pv_pn.pdf)

---

![original fit](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Silicon_Solar_cell_structure_and_mechanism.svg/1280px-Silicon_Solar_cell_structure_and_mechanism.svg.png)

---

![left fit](../media/l11_pv_mdl.pdf)


$$ I_D = I_S\left(e^\frac{V_D}{V_T} - 1\right)$$

$$ I_D = I_{Photo} - I_{Load}$$

$$ V_D = V_T ln{\left(\frac{I_{Photo} - I_{Load}}{I_S} + 1 \right)} $$

$$ P_{Load} = V_D I_{Load}$$



---

```python
#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

m = 1e-3
i_load = np.linspace(1e-5,1e-3,200)

i_s = 1e-12

i_ph = 1e-3

V_T = 1.38e-23*300/1.6e-19

V_D = V_T*np.log((i_ph - i_load)/(i_s) + 1)

P_load = V_D*i_load

plt.subplot(2,1,1)
plt.plot(i_load/m,V_D)
plt.ylabel("Diode voltage [mA]")
plt.grid()
plt.subplot(2,1,2)
plt.plot(i_load/m,P_load/m)
plt.xlabel("Current load [mA]")
plt.ylabel("Power Load [mW]")
plt.grid()
plt.savefig("pv.pdf")
plt.show()

```

![right fit](../py/pv.pdf)

---

![left original fit](../py/pv.pdf)

[ANYSOLAR](https://www.digikey.no/en/products/detail/anysolar-ltd/KXOB25-03X4F-TB/13999196)

![right original fit](../ip/l11_pv_dtsh.pdf)

---

![fit](../ip/l11_pv1_0.pdf)

---

![fit](../ip/l11_pv1_1.pdf)

---

![fit](../ip/l11_pv1_2.pdf)

---

#[fit] Piezoelectric

---

![left 130%](https://upload.wikimedia.org/wikipedia/commons/c/c4/SchemaPiezo.gif)

#[Piezoelectric effect](https://en.wikipedia.org/wiki/Piezoelectricity)

---



![fit](../ip/l11_pc2_0.pdf)

---

![fit](../ip/l11_pc2_1.pdf)

---

#[fit] Ambient RF

---

# Ambient RF Harvesting

[.column]

Extremely inefficient idea, but may find special use-cases at short-distance

Will get better with beamforming and directive antennas

[AirFuel](https://airfuel.org/airfuel-rf/)



[.column]

| dBm | W |
| :---: | :---: |
| 30 | 1 |
| 0  | 1 m|
| -30 | 1 u|
| -60 | 1 n |
| -90 | 1 p|

---

Assume $$P_{TX}$$ = 1 W (30 dBm) and $$P_{RX}$$ = 10 uW (-20 dBm)

$$ D = 10^\frac{P_{TX} - P_{RX} + 20 log_{10}\left(\frac{c}{4 \pi f}\right)}{20} $$

| Freq | **$$20 log_{10}\left(c/4 \pi f\right)$$** [dB]| D [m]|
| ----|:----:| ---: |
| 915M | -31.7 | 8.2 | 
| 2.45G | -40.2 | 3.1 |
| 5.80G | -47.7 | 1.3 |

---

#[fit] Triboelectric generator

---

![fit](../ip/l11_teng0_0.pdf)

---

![fit](../ip/l11_teng0_1.pdf)

---

![fit](../ip/l11_teng2_0.pdf)

---

![fit](../ip/l11_teng2_4.pdf)


---

![fit](../ip/l11_teng2_1.pdf)

---

![fit](../ip/l11_teng2_2.pdf)

---

#[fit] Comparison

---

![400% ](../ip/l11_teng2_3.pdf)

---

# References



[Towards a Green and Self-Powered Internet of Things Using Piezoelectric Energy Harvesting](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8762143)

[A 3.5-mV Input Single-Inductor Self-Starting Boost Converter With Loss-Aware MPPT for Efficient Autonomous Body-Heat Energy Harvesting](https://ieeexplore.ieee.org/document/9302641)

[A Reconfigurable Capacitive Power Converter With Capacitance Redistribution for Indoor Light-Powered Batteryless Internet- of-Things Devices](https://ieeexplore.ieee.org/abstract/document/9423810)

[A Fully Integrated Split-Electrode SSHC Rectifier for Piezoelectric Energy Harvesting](https://ieeexplore.ieee.org/document/8642406)

[Current progress on power management systems for triboelectric nanogenerators](https://ieeexplore.ieee.org/document/9729411)

[A Fully Energy-Autonomous Temperature-to-Time Converter Powered by a Triboelectric Energy Harvester for Biomedical Applications](https://ieeexplore.ieee.org/document/9441315)




---


#[fit] Thanks!




