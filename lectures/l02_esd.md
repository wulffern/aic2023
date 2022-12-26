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
<!--pan_skip: -->

## **Q:** What blocks must our IC include?


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

# **Q:** Why does this work?

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



