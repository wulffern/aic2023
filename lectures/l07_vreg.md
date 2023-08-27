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

Assume a system is AC powered. Then there will be switched regulator to turn wall AC into DC. The DC might be 48 V, 24 V, 12 V, 5 V, 3 V
1.8 V, 1.0 V, 0.8 V, or who knows. The voltage depends on the type of IC and the application.
 
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

### Why transistors break

A gate oxide will break due to Time Dependent Dielectric Breakdown (TDDB) if the voltage across the gate oxide is too large. Silicon oxide can break down at approximately 5 MV/cm. The breakdown forms a conductive channel from the gate to the channel and is permanent. After breakdown there will be a resisrtor of kOhms between gate and channel. A similar breakdown phenomena is used in [Metal-Oxide RRAM](https://ieeexplore.ieee.org/document/6193402).

The threshold voltage of a transistor can shift excessively over time caused by Hot-Carrier Injection (HCI) or Negative Bias Temperature Instability.

Hot-Carrier injection is caused by electrons, or holes, accelerated to high velocity in the channel, or drain depletion region , causing impact ionization (breaking a co-valent bond releasing an electron/hole pair). At a high drain/source field, and  
medium gate/(source or drain) field, the channel minority carriers can be accelerated to high energy and transition to traps in the oxide, shifting the 
threshold voltage. 


Negative Bias Temperature Instability is a shift in threshold voltage due to a physical change in the oxide. 
A strong electric field across the oxide for a long time can break co-valent, or ionic bonds, in the oxide. The bond break will change the forces (stress) in the amorphorous silicon oxide which might not recover. As such, there might be more traps (states) than before. See [Simultaneous Extraction of Recoverable and Permanent Components Contributing to Bias-Temperature Instability](https://ieeexplore.ieee.org/document/4419069) for more details.

### What is traps?

For a long time, I had trouble with "traps in the oxide"". I had a hard time visualizing how electrons wandered down 
the channel and got caught in the oxide. I was trying to imagine the electric field, and that the electron needed to find 
a positive charge in the oxide to cancel. Diving a bit deeper into quantum mechanics, my mental image improved a bit, so I'll
try to give you a more accurate mental model for how to think about traps.

Quantum mechanics tells us that bound electrons can only occupy fixed states. The probability 
of finding an electron in a state is given by Fermi-Dirac statistics, but if there is no energy state, there cannot be an electron there.

For example, there might be a 50 \% probability of finding an electron in the oxide, but if there is no state there, then there will not be any electron
, and thus no change threshold voltage. 

What happens when we make "traps", through TDDB, HCI, or NBTI is that we create new states that can be occupied by charges.
And if the Fermi-Diract statistics tells us the probability of an electron being in that state is 50 \%, then there will likely be an electron there.

The threshold voltage is defined as the voltage at which we can invert the channel, or create the same density of electrons (for NMOS) as  density of dopant
atoms (density of holes) in the bulk. 

If the oxide has a net negative charge (because of electrons in new states), then we have to pull harder 
(higher gate voltage) to establish the channel. As a result, the threshold voltage increases with electrons stuck in the oxide. 

In quantum mechanics the time evolution, and the complex probability amplitude of an electron changing state, could, in theory, be computed with the Schrødinger equation. 
Unfortunately, for any real scenario, like the gate oxide of a transistor, using Schrødinger to compute exactly what will happen is beyond the capability of the 
largest supercomputers. 

### Breakdown voltages

The voltage where the transistor can survive is estimated by the foundry, by approximation, and testing, and may be like the table below. 

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

Most ICs talk to other ICs, and they have a voltage for the general purpose input/output. The voltage reduction in I/O voltage does not need to scale as fast 
as the core voltage, because foundries have thicker oxide transistors that can survive the voltage. 
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

The dynamic range of the power consumed by an IC can be large. From nA when it's not doing anything, to hundreds of mA when there is high computation load. 

As a result, it's not necessarily possible, or effective, to have one regulator from 1.8 V to 0.8 V. We may need multiple regulators. Some that can
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

<!--pan_skip: -->

#[fit] Linear Regulators

---

<!--pan_doc:

# Linear Regulators

-->

## PMOS pass-fet

<!--pan_doc:

One way to make a regulator is to control the current in a PMOS with a feedback loop, as shown below. The OTA continously adjusts the gate-source voltage of
the PMOS to force the input voltages of the OTA to be equal.

For digital loads, where $I_{load}$ is a digital current, with high current every rising edge of the clock, it's an option to place a large external decoupling capacitor 
(a reservoir of charge) in parallell with the load. Accordingly, the OTA would supply the average current.

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
| Settling time  | How fast does the output voltage settle at a current step | s|


A disadvantage of a PMOS is the hole mobility, which is lower than for NMOS. If the maximum current of an LDO is large, then the PMOS can be big. Maybe even 
50 \% of the IC area.

-->


![left fit](../media/l9_ldo_pmos.pdf)

---

## NMOS pass-fet

<!--pan_doc:

An NMOS passfet will be smaller than a PMOS for large loads. The disadvantage with an NMOS is the gate-source voltage needed. For some senarios the needed gate voltage might
exceed the input voltage (1.5 V). A gate voltage above input voltage is possible, but increases complexity, as a charge pump (switched capacitor regulator) is needed to make 
the gate voltage.

Another interesting phenomena with NMOS pass-fet is that the PSRR is usually better, but we do have a common gate amplifier, as such, high frequency voltage ripple on output voltage
will be amplified to the input voltage, and may cause issues for others using the input voltage.

-->

![right fit](../media/l9_ldo_nmos.pdf)

---

<!--pan_skip: -->

#[fit]LDO's in JSSC

---

<!--pan_skip: -->

[A Scalable High-Current High-Accuracy Dual-Loop Four-Phase Switching LDO for Microprocessors](https://ieeexplore.ieee.org/document/9639005)

![inline fit](../ip/l9_jssc_ldo2.pdf)

---

<!--pan_skip: -->

![original fit](../ip/l9_jssc_ldo2_arch0.pdf)

---

<!--pan_skip: -->

![original fit](../ip/l9_jssc_ldo2_arch.pdf)

---

<!--pan_skip:-->

#[fit] Switched Regulators

---

<!--pan_doc:

# Switched Regulators

Linear regulators have the same current in the load, as from the input. The power efficiency is thus bad for a linear regulator.

For some applications that might be OK, but for most battery operated systems we're interested in using the electrons from the battery in the most effective manner. 

Another challenge is temperature. A linear regulator with a 5 V input voltage, and 1 V output voltage will have a maximum power efficiency of 20 \% (1/5). 80 \% of the power is wasted in the pass-fet as heat. 

Imagine a LDO driving an 80 W CPU at 1 V from a 5 V power supply. The power drawn from the supply is 400 W, as such, 320 W would be wasted in the LDO. A quad flat no-leads (QFN) package usually have a thermal resistance of 20 $^{\circ}$C/W, so if it would be possible, the temperature of the LDO would be 6400 $^{\circ}$C. Obviously, that cannot work. 


For increased power efficiency, we must use switched regulators.

Imagine a switch regulator with 93 % power efficiency. The power from the 5 V supply would be $80\text{ W}/ 0.93 = 86\text{ W}$, as such, only 6 W is wasted as heat, or a temperature increase 120 $^{\circ}$C, still high, but not impossible with a small heat-sink.

All switched regulators are based on devices that store electric field (capacitors), or magnetic field (inductors). 

A capacitor can be charged to a voltage. Once charged, one can reconfigure a capacitor circuit, for example changing the capacitor circuit from series to parallell (convert down in voltage), or parallell to series (convert up in voltage).

An inductor, once charged with a current, will continue to push the current even if we change the voltage across the inductor terminals. As such, we can redirect current, either to charge a capacitor to a higher voltage, or a lower voltage, than the input voltage.

An overview of switched regulators can be seen in the figure below. I would encourage you to download the PDF from Mouser. 

-->

![left fit](../media/l9_mouser.png)


[Reference Guide to Switched DC/DC Conversion](https://emea.info.mouser.com/dc-dc-converter-guide?cid=homepage&pid=mouser)

---

## Inductive DC/DC converters

---

<!--pan_doc:

I've found that people struggle with inductive DC/DCs. They see a circuit inductors, capacitors, and transistors and think filters, Laplace and steady state. The path of Laplace and steady state will lead you astray and you won't understand how it works.

Hopefully I can put you on the right path to understanding. 

In the figure below we can see a typical inductive switch mode DC/DC converter. The input voltage is $V_{DDH}$, and the output is $V_O$.

Most DC/DCs are feedback systems, so the control will be adjusted to force the output to be what is wanted, however, let's ignore close loop for now. 

-->

![left fit](../media/l7_buck.pdf)

<!--pan_doc:

To see what happens I find the best path to understanding is to look at the integral equations. 

Let's ignore the resistor for now.

The current in the inductor is given by
-->


$$I_x(t) = \frac{1}{L} \int{V_x(t) dt}$$

<!--pan_doc:

and the voltage on the capacitor is given by

-->

$$V_o(t) = \frac{1}{C} \int{(I_x(t) - I_o(t))}dt$$

<!--pan_doc:

Before you dive into Matlab, Mathcad, Maple, SymPy or another of your favorite math software, it helps to think a bit.

My mathematics is not great, but I don't think there is any closed form solution to the output voltage of the DC/DC, especially since the state of the NMOS and PMOS is time-dependent.

The output voltage also affect the voltage accross the inductor, which affects the current, which affects the output voltage, etc, etc. 

The equations can be solved numerically, but a numerical solution to the above integrals needs initial conditions.

There are many versions of the control block, let's look at two.

-->


---

## Pulse width modulation (PWM)

<!--pan_doc:

Assume $I_x=0$ at $t=0$. Assume the output voltage is $V_O=0$. Imagine we set $A=1$ for a fixed time duration.  The voltage at $V_1=V_{DDH}$, and $V_x = V_{VDDH}-V_O$. As $V_x$ is positive, and roughly constant, as such the current would increase linearly. 

Since the $I_x$ is linear, then $V_o$ would be a second order function. 

Let's set $A=0$ and $B=1$ for another fixed time duration (it does not need to be the same as time as A). 
 
The voltage across the inductor would be $V_x = 0 - V_o$. The output voltage would not have increased much, so the absolute value of $V_x$ during $A=1$ would be higher than the absolute value of $V_x$ during the first $B=1$. 

The $V_x$ is now negative, so the current will decrease, however, since $V_x$ is small, it does not decrease much. 
 
I've made a
-->

[Jupyter PWM BUCK model](https://github.com/wulffern/aic2023/blob/main/jupyter/buck.ipynb)

<!--pan_doc:

that numerically solves the equations. 

In the figure below we can see how the current during A increases fast, while during B it decreases little. The output voltage increases similarly to a second order function.

![](../media/l07_buck_pwm_fig_start.svg)

If we run the simulation longer, see plot below, the DC/DC will start to settle into a steady state condition.

On the left we can see the current $I_x$ and $I_o$, on the right you can see the output voltage.  Turns out that the output voltage will be 

$$ V_o = V_{in} \times \text{ Duty-Cycle}$$

, where the duty-cycle is the ratio between the time of $A=1$ and $B=1$.

-->

![right fit](../media/l07_buck_pwm_fig.svg)


<!--pan_doc:

Once the system has fully settled, see figure below, we can see the reason for why DC/DC converters are useful.

During $A=1$ the current $I_x$ increases fast, and it's only during $A=1$ we pull current from $V_{DDH}$. At the start of $B=1$ the current is still positive, which means we pull current from ground. The average current in the inductor is the same as the load current, however, the current from $V_{DDH}$ is lower than the average inductor current. 

![](../media/l07_buck_pwm_fig_settled.svg)

DC/DC converters are used everywhere efficiency is important. Below is a screenshot of the hardware description in the [nRF5340 Product Specification](https://infocenter.nordicsemi.com/pdf/nRF5340_PS_v1.3.pdf).

We can see 3 inductor/capacitor pairs. One for the "VDDH", and two for "DECRF" and "DECD", as such, we can make a good guess there are three DC/DC converters inside the nRF5340

-->

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
