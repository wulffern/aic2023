footer: Carsten Wulff 2023
slidenumbers:true
autoscale:true
theme:Plain Jane,1

<!--pan_skip: -->

## TFE4188 - Introduction to Lecture 7
# Voltage regulation

<!--pan_title: Lecture 7 - Voltage regulation -->

---

<!--pan_doc:

<iframe width="560" height="315" src="https://www.youtube.com/embed/GRzz3wxKJGQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

-->

<!--pan_skip: -->

# Goal

**Why** do we need voltage regulation

Introduction to **linear regulators**

Introduction to **switched regulators**

---

<!--pan_skip: -->

#[fit] Why

---

# Voltage source

<!--pan_doc:

Most, if not all, intregrated circuits need a supply and ground to work.

The difference in Fermi levels, chemical potential, or voltage must come from something.

Assume AC powered. Then there will be switched regulator to turn wall AC into DC. The DC might be 48 V, 24 V, 12 V, 5 V, 3 V
1.8 V, 1.0 V, 0.8 V, or who knows. The voltage depends on the type of application where the IC is used.
 
Many ICs are battery operated, whether it's your phone, watch, heart rate monitor, mouse, keyboard, game controller or car.
 
For batteries the voltage is determined by the difference in Fermi level on the two electrodes, and the Fermi level (chemical potential) 
is a function of the battery chemistry.
 
As a result, we need to know the battery chemistry in order to know the voltage. 

[Linden's Handbook of Batteries](https://www.amazon.com/Lindens-Handbook-Batteries-Fifth-Kirby/dp/1260115925) is a good book
if you want to dive deep into primary (non-chargable) or secondary (chargable) batteries and their voltage curves.

Some common voltage sources are listed below.

-->

![left 70%](../media/lindens_handbook_of_batteries.png)

|  |Chemistry|  Voltage [V] |
|----|:----|----:|
| Primary Cell| LiFeS2 + Zn/Alk/MnO2 + LiMnO2  | 0.8 - 3.6 |
| Secondary Cell| Li-Ion | 2.5 - 4.3 |
| USB | - | 4.0 - 6.5 (20)|

---



[.column]

## Core voltage

<!--pan_doc:

The transistors in a particular technology (from GlobalFoundries, TSMC, Samsung or others) have a maximum 
voltage that they can survive for a certain life time. 

A gate oxide will break due to Time Dependent Dielectric Breakdown (TDDB) if the voltage across the gate oxide is too large.

The threshold voltage of a transistor can shift excessively over time caused by Hot-Carrier Injection (HCI) or Negative
Bias Temperature Instability.

Hot-Carrier injection is caused by electrons, or holes, accelerated to high velocity in the channel, or drain depletion region
, causing impact ionization (breaking a co-valent bond releasing an electron/hole pair). At a high drain/source field and a 
medium gate/(source or drain) field the minority carrier can be accelerated and caught by traps in the oxide, shifting the 
threshold voltage. 

Negative Bias Temperature Instability is a shift in threshold voltage due to a physical change in the oxide. 
A strong electric field across the oxide for a long time can break co-valent, or ionic bonds, in the oxide. As such,
there might be more traps (states) than before.

For a long time, I had trouble with the "traps" in the oxide. I had a hard time visualizing how electrons wandered down 
the channel and got caught in the oxide. I was trying to imagine the electric field, and that the electron needed to find 
a positive charge in the oxide to cancel. Diving a bit deeper into quantum mechanics, my mental image improved a bit, so I'll
try to give you a more accurate mental model for how to think about traps.

Quantum mechanics tells us that bound electrons can only occupy fixed states. The probability 
of finding an electron in a state is given by Fermi-Dirac statistics, but if there is no energy state, there cannot be an electron there.
For example, there might be a 50 \% probability of finding an electron in the oxide, but if there is no state there, then there will not be any electron
, and thus no change to our threshold voltage. What happens when we make "traps", through TDDB, HCI, or NBTI is that we create new states that can be occupied by charges.
And if the Fermi-Diract statistics tells us the probability of an electron being in that state is 50 \%, then there will likely be an electron there.

The threshold voltage is defined as the voltage at which we can invert the channel, or create the same density of electrons (for NMOS) as  density of dopant
atoms (density of holes) in the bulk. If the oxide has a net negative charge (because of electrons in new states), then we have to pull harder 
(higher gate voltage) to establish the channel. Thus the threshold voltage increases with electrons stuck in the oxide. 

In quantum mechanics the time evolution, and the complex probability amplitude of an electron changing state, could, in theory, be computed with the Schrødinger equation. 
Unfortunately, for any real scenario, like the gate oxide of a transistor, using Schrødinger to compute exactly what will happen is beyond the capability of the 
largest supercomputers. 

In any case, the voltage where the transistor can survive is estimated by the foundry, by approximation, and testing, and may be like the table below. 

-->

| Node [nm] | Voltage [V] |
|:---------:|:-----------:|
| 180       | 1.8         |
| 130       | 1.5         |
| 55        | 1.2         |
| 22        | 0.8         |

[.column]



## IO voltage

<!--pan_doc:

Most ICs talk to other ICs, and they have a voltage for the general purpose input output. The voltage reduction in I/O voltage does not need to scale as fast 
as the core voltage, because foundries have thicker oxide transistors that can survive the voltage. And most the area on an IC is likely digital logic made with core transistors.

-->

| Voltage [V]|
| ----:|
|5.0|
|**3.0**|  
|*1.8*|
|1.2|

---

<!--pan_doc:

## Supply planning

For any IC, we must know the application. We must know where the voltage comes from, the IO voltage, the core voltage, and any other requirements (like charging batteries).

One example could be an IC that is powered from a Li-Ion battery, with a USB to provide charging capability. 

Between each voltage we need an analog block, a regulator, to reduce the voltage in an effective manner. What type of regulator depends again on the application, 
but the architecture of the analog design would be either a linear regulator, or a switched regulator. 


-->

![original fit](../media/l9_sarc.pdf)

---

<!--pan_doc:

The dynamic range of the power consumed by an IC can be large. From nA when it's not doing anything, to hundreds of mA when there is high computation load our transmitting
with a radio. 

As a result, it's not necessarily possible, or effective, to have only one regulator to go from for example 1.8 V to 0.8 V. We may need multiple regulators. Some that can
handle low load (nA - $\mu$A) effectively, and some that can handle high loads.

For example, if you design a regulator to deliver 500 mA to the load, and the regulator uses 5 mA, that's only 1 \% of the current, which may be OK. 
The same regulator might consume 5 mA even though the load is 1 uA, which would be bad. All the current flows in the regulator at low loads.

-->


| Name      | Voltage | Min [nA] | Max [mA] | PWR DR [dB] |
|:---------:|:--: |:--------:|:--------:|:-----------:|
| VDD\_VBUS |5 |10       | 500      | 77          |
| VDD\_VBAT |4 |10       | 400      | 76          |
| VDD\_IO   |1.8 |10       | 50       | 67          |
| VDD\_CORE |0.8 |10       | 350      | 75          |

---

<!--pan_doc:

Most [product specifications](https://infocenter.nordicsemi.com/topic/ps_nrf5340/chapters/pmu/doc/pmu.html?cp=4_0_0_3) will give you a view into what type of 
regulators there are on an IC. The picture below is from nRF5340

-->

![original fit](../media/l9_nrf53.pdf)

---

#[fit] Linear Regulators

---

## PMOS pass-fet

<!--pan_doc:

One way to make a regulator is to control the current in a PMOS with a feedback loop, as shown below. The OTA continously adjusts the gate-source voltage of
the PMOS to maintain the voltage. 

For digital laods, where $I_{load}$ is a digital current, with high current every rising edge of the clock, it's an option to place a large external decoupling capacitor 
(a reservoir of charge) in parallell with the load. Thus the feedback loop only need to supply the average current, and the peak currents needed by digital logic is supplied
by the capacitor.

The device between supply (1.5 V) and output voltage (0.8 V) is often called a pass-fet. A PMOS pass-fet regulator is often called a LDO, or low droopout regulator, since
we only need a $V_{DSSAT}$ across the PMOS, which can be a few hundred mV. 

Key parameters of regulators are

| Parameter                    | Description                                                                                               | Unit |
|:----------------------------:|:---------------------------------------------------------------------------------------------------------:|:----:|
| Load regulation              | How much does the output voltage change with load current                                                 | V/A  |
| Line regulation              | How much does the output voltage change with input voltage                                                | V/V  |
| Power supply rejection ratio | What is the transfer function from input voltage to output voltage? The PSRR at DC is the line regulation | dB   |
| Max current                  | How much current can be delivered through the pass-fet?                                                   | A    |
| Quiesent current             | What is the current used by the regulator                                                                 | A    |


A disadvantage of a PMOS is the hole mobility, which usually is lower than for NMOS. If the maximum current of an LDO is large, then the PMOS can be big. Maybe even 
50 \% of the IC area.

-->


![left fit](../media/l9_ldo_pmos.pdf)

---

## NMOS pass-fet

<!--pan_doc:

An NMOS passfet will be smaller than a PMOS for large loads. The disadvantage with a PMOS is the gate-source voltage needed. For some senarios the needed gate voltage might
exceed the input voltage (1.5 V). A gate voltage above input voltage is possible, but increases complexity, as a charge pump (switched capacitor regulator) is needed to make 
the gate voltage.

Another interesting phenomena with NMOS pass-fet is that the PSRR is usually better, but we do have a common gate amplifier, as such, high frequency voltage ripple on output voltage
will be amplified input voltage, and may cause issues for others using the input voltage.

-->

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

<!--pan_doc:

For linear regulators have the same current in the load, as in the input voltage. The power efficiency is thus naturally bad for a linear regulator.
A linear regulator with a 5 V input voltage, and 1 V output voltage will have a maximum power efficiency of 20 \% (1/5). 80 \% of the power is wasted in the pass-fet as heat.

For some applications that might be OK, but for most battery operated systems we're interested in using the electrons from the battery in the most effective manner. 

For increased power efficiency, we must use switched regulators.

-->

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
