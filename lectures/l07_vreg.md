footer: Carsten Wulff 2023
slidenumbers:true
autoscale:true
theme:Plain Jane,1

<!--pan_skip: -->

## TFE4188 - Introduction to Lecture 7
# Voltage regulation

<!--pan_title: Lecture 7 - Voltage regulation -->

<!--pan_doc:

<iframe width="560" height="315" src="https://www.youtube.com/embed/GRzz3wxKJGQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

-->

---

# Goal

**Why** do we need voltage regulation

Introduction to **linear regulators**

Introduction to **switched regulators**

---

#[fit] Why

---

# Voltage source

![left 70%](../media/lindens_handbook_of_batteries.png)

|  |Chemistry|  Voltage [V] |
|----|:----|----:|
| Primary Cell| LiFeS2 + Zn/Alk/MnO2 + LiMnO2  | 0.8 - 3.6 |
| Secondary Cell| Li-Ion | 2.5 - 4.3 |
| USB | - | 4.0 - 6.5 (20)|

---

[.column]

## Core 

| Node [nm] | Voltage [V] |
|:---------:|:-----------:|
| 180       | 1.8         |
| 130       | 1.5         |
| 55        | 1.2         |
| 22        | 0.8         |

[.column]

## IO 

| Voltage [V]|
| ----:|
|5.0|
|**3.0**|  
|*1.8*|
|1.2|

---

![original fit](../media/l9_sarc.pdf)

---


| Name      | Voltage | Min [nA] | Max [mA] | PWR DR [dB] |
|:---------:|:--: |:--------:|:--------:|:-----------:|
| VDD\_VBUS |5 |10       | 500      | 77          |
| VDD\_VBAT |4 |10       | 400      | 76          |
| VDD\_IO   |1.8 |10       | 50       | 67          |
| VDD\_CORE |0.8 |10       | 350      | 75          |

---

![original fit](../media/l9_nrf53.pdf)

---

#[fit] Linear Regulators

---

## PMOS pass fet


![left fit](../media/l9_ldo_pmos.pdf)

---

## NMOS pass fet

![right fit](../media/l9_ldo_nmos.pdf)

---

#[fit]LDO's in JSSC

---

[A Scalable High-Current High-Accuracy Dual-Loop Four-Phase Switching LDO for Microprocessors](https://ieeexplore.ieee.org/document/9639005)

![inline fit](../ip/l9_jssc_ldo2.pdf)

---

![original fit](../ip/l9_jssc_ldo2_arch0.pdf)

---

![original fit](../ip/l9_jssc_ldo2_arch.pdf)

---

#[fit] Switched Regulators

---

![left fit](../media/l9_mouser.png)


[Reference Guide to Switched DC/DC Conversion](https://emea.info.mouser.com/dc-dc-converter-guide?cid=homepage&pid=mouser)

---

# Inductive DC/DC converters

---


![left fit](../media/l7_buck.pdf)

$$I_x(t) = \frac{1}{L} \int{V_x(t) dt}$$

$$V_o(t) = \frac{1}{C} \int{(I_x(t) - I_o(t))}dt$$


---

# Pulse width modulation (PWM)


[Jupyter PWM BUCK model](https://github.com/wulffern/aic2023/blob/main/jupyter/buck.ipynb)

![right fit](../media/l07_buck_pwm_fig.svg)

---

![original fit](../media/l9_sw_nRF53.png)

---

## Pulsed Frequency Mode (PFM)

![right fit](../media/l9_sw_arch.pdf)

---


![fit](../media/l9_sw_state.pdf)

---

[Jupyter PFM BUCK model](https://github.com/wulffern/aic2023/blob/main/jupyter/buck_pfm.ipynb)

![right fit](../media/l07_buck_pfm_fig.svg)

---

#[fit] BUCKs in JSSC

---

[A 10-MHz 2–800-mA 0.5–1.5-V 90% Peak Efficiency Time-Based Buck Converter With Seamless Transition Between PWM/PFM Modes](https://ieeexplore.ieee.org/document/8187654)

![inline fit](../ip/l9_jssc_sw3.pdf)

---

![original fit](../ip/l9_jssc_sw3_why.pdf)

---

![original fit](../ip/l9_jssc_sw3_arch.pdf)

---


## Boost

![right fit](../media/l9_sw_boost.pdf)

---

#[fit] Thanks!
