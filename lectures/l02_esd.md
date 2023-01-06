footer: Carsten Wulff 2023
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica


<!--pan_title: Lecture 2 - IC and ESD  -->

<!--pan_doc:

<iframe width="560" height="315" src="https://www.youtube.com/embed/PqGt_QmVJeo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

-->

<!--pan_skip: -->

## TFE4188 - Introduction to Lecture 2
# ICs and ESD

---

<!--pan_skip: -->

# Goal 

Understand the **real-world** constraints on our IC

Understand why you must **always handle ESD** on an IC

---

<!--pan_skip: -->

#[fit] RPLY

The project for 2023 is to design an integrated temperature sensor. The hope is that some will tapeout on the Google/Efabless Open MPW shuttle

---

<!--pan_skip: -->

# The **real world** constrains our IC

---

## **Q:** What blocks must our IC include?

<!--pan_doc:

## What blocks must our IC include?

First, we need to have an idea of what comes in and out of the temperature
sensor. Before we have made the temperature sensor, we need to think what the signal interface could be, and we need to learn.

Maybe we read [Kofi Makinwa's overview of temperature sensors](http://ei.ewi.tudelft.nl/docs/TSensor_survey.xls)
and find one of the latest papers, [A BJT-based CMOS Temperature Sensor with Duty-cycle-modulated Output and ±0.54 °C (3σ) Inaccuracy from -40 °C to 125 °C](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9383810).

At this point, you may struggle to understand the details of the paper, but at least it should be possible to see what comes in and out of the module. 
What I could find is in the table below, maybe you can find more?

| Pin      | Function       | in/out | Value    | Unit |
|:---------|:---------------|:-------|:---------|:-----|
| VDD_3V3  | analog supply  | in     | 3.0      | V    |
| VDD_1V2  | digital supply | in     | 1.2      | V    |
| VSS      | ground         | in     | 0        | V    |
| CLK_1V2  | clock          | in     | 20       | MHz  |
| RST_1V2  | digital        | out    | 0 or 1.2 | V    |
| I_C      | bias           | in     | ?        | uA?  |
| PHI1_1V2 | digital        | out    | 0 or 1.2 | V    |
| PHI2_1V2 | digital        | out    | 0 or 1.2 | V    |
| DCM_1V2  | digital        | out    | 0 or 1.2 | V    |

This list contains supplies, clocks, digital outputs, bias currents and a ground. Let me explain what they are.


### Supply 
The temperature sensor has two supplies, one analog (3.3 V) and one digital (1.2 V), which must come from somewhere. 

We're using Skywater, and to use the free tapeouts we must use the [Caravel](https://caravel-harness.readthedocs.io/en/latest/) 
test chip harness.

That luckily has two supplies. It can be powered externally by up to 5.0 V, and has an external low dropout regulator (LDO) that provides the digital supply (1.8 V).
See more at [Absolute maximum ratings](https://caravel-harness.readthedocs.io/en/latest/maximum-ratings.html)

### Ground 
Most ICs have a ground, a pin which is considered 0 V. It may have multiple grounds. Remember that a voltage is only defined between two points, so it's actually 
not true to talk about a voltage in a node (or on a wire). A voltage is always a differential to something. We've (as in global electronics engineers) have just 
agreed that it's useful to have a "node" or "wire" we consider 0 V. 

### Clocks 
Most digital need a clock, and the Caravel provide a 40 MHz clock which should suffice for most things. We could probably just use that clock for 
our temperature sensor.

### Digital 
We need to read the digital outputs.  We could either feed those off chip, or use a on chip micro-controller. The Caravel includes options to do both. We could connect digital
outputs to the logic analyzer, and program the RISC-V to store the readings. Or we could connect the digital output to the I/O and use an instrument in the lab.

### Bias 
The Caravel does not provide bias currents (that I found), so that is something you will need to make. 


### Conclusion
Even a temperature sensor needs something else on the IC. We need digital input/output, clock generation (PLL, oscillators), bias current generators, and voltage regulators
(which require a constant reference voltage).

I would claim that any System-On-Chip will always need these blocks!

I want you to pause, take a look at the [course plan](https://wulffern.github.io/aic2023/plan/), and now you might understand why I've selected the topics.

### One more thing
There is one more function we need when we have digital logic and a power supply. We need a "RESET" system. 

Digital logic has a fundamental assumption 
that we can separate between a "1" and a "0", which is usually translated to for example 1.8 V (logic 1) and 0 V (logic 0). 
But if the power supply is at 0 V, before we connect the battery, then that fundamental assumption breaks. 

When we connect the battery, how do we know the fundamental assumption is OK? It's certainly not ok at 30 mV supply. How about 500 mV? or 1.0 V? 
How would we know?

Most ICs will have a special analog block that can keep the digital logic, bias generators, clock generators, input/output and voltage regulators in a **safe**
state until the power supply is high enough (for example 1.62 V). 


-->


---
<!--pan_skip: -->

#[fit] ESD

---

# Electrostatic Discharge 

If you make an IC, you must consider Electrostatic Discharge (ESD) Protection circuits

<!--pan_doc: 

ESD events are tricky. They are short (ns), high current (Amps) and poorly modeled in the SPICE model. 
Most SPICE models will not model correctly what happens to an transistor during an ESD event.

But ESD design is a must, you have to think about ESD, otherwise your design will never work. 

Consider a certain ESD specification, for example 1 kV human body model, a requirement for an integrated circuit. 
By requirement I mean if the 1 kV is not met, then the project will be delayed until it is fixed. If it's not fixed, then the
project will be infinietly delayed, or in other words, cancelled.

Now imagine it's your responsibility to ensure it meets the 1 kV specification, what would you do? I would recommend you read one
of the few ESD books in existence, shown below, and rely on you understanding of PN-junctions.

-->

![right 110%](https://media.wiley.com/product_data/coverImage300/18/04714987/0471498718.jpg)

<!--pan_doc: 

The industry has agreed on some common test criteria for electrostatic discharge.

-->

Standards for testing at [JEDEC](https://www.jedec.org/category/technology-focus-area/esd-electrostatic-discharge-0)

---

## When do ESD events occur?

[.column]

__Before/during PCB__ 

Human body model (HBM)

Charged device model (CDM)

[.column]

__After PCB__

Human body model (HBM) 

System level ESD 

---
## Human body model (HBM)

- Models a person touching a device with a finger
- **Long** duration (around 100 ns)
- Acts like a current source into a pin
- Can usually be handled in the I/O ring
- 4 kV HBM ESD is 2.67 A peak current

![right fit](../media/esd_hbm_finger.pdf)

---
# An ESD zap example 

 Imagine a ESD zap between VSS and VDD. How can we protect the device? 

![left fit](../media/esd_hbm_model.pdf)

---

#[fit]  Permutations

![right fit](../media/l02_hbm_overview.pdf)

---


![inline fit](../media/l02_01.pdf)

---

![inline fit](../media/l02_02.pdf)

---

![inline fit](../media/l02_all.pdf)

---

![left fit](../media/l02_ggnmos.pdf)

## **Q:** Why does this work?

---

If you don't do the layout right[^3]

[.column]

![fit](../ip/esd_layout.pdf) 

[.column]

![fit ](../ip/esd_damage.pdf)


[^3]: [New Ballasting Layout Schemes to Improve ESD Robustness of I/O Buffers in Fully Silicided CMOS Process](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=5299049)

---

## **Q:** How can current in one place lead to a current somewhere else?

![left fit](../media/l02_latchup.pdf)


---

You must **always handle ESD** on an IC

- Do everything yourself
- Use libraries from foundry
- Get help [www.sofics.com](http://www.sofics.com)


---


#[fit] Thanks!



