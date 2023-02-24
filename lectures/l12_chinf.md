footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme:Plain Jane,1

# TFE4188 - Lecture 11
# Chip infrastructure 

---
# Housekeeping

[Syllabus](https://github.com/wulffern/aic2022/blob/main/syllabus.md)

Exam

Project

---

#[fit] I want you to learn the necessary skills to make your own ICs

---

#[fit] Exam

---

- 19'th and 20'th of May
- Oral, approx 40 minutes
- 55% of the final grade
- A - F grade (F = Fail)
- Book a slot [https://www.ntnu.no/wiki/display/tfe4487/Oral+exam+2022](https://www.ntnu.no/wiki/display/tfe4487/Oral+exam+2022)

---

![left fit](../media/l12_ldo.pdf)

# Possible exam questions

Q1: What circuit could the picture be?

Q2: How would you make the bias current?

Q3: How could we make the output voltage process independent?

---

![fit](../media/l12_ex1.pdf)

---


# Q4: Draw a block diagram of a PLL, and explain.

---

#[fit] Project

---

45 % of final grade

Deadline: 22 of April. Upload project paper on blackboard.

Strict deadline, if you hand in 23 of April at 00:00:01, then it's a fail.

---

#[fit] Project Report $$\Rightarrow$$ Paper

#[fit] [A Compiled 9-bit 20-MS/s 3.5-fJ/conv.step SAR ADC in 28-nm FDSOI for Bluetooth Low Energy Receivers](https://ieeexplore.ieee.org/document/7906479)

[IEEE journal template](https://ctan.org/pkg/ieeetran?lang=en), [Example](https://github.com/wulffern/jssc2017)

Must use `\documentclass[journal,11pt,letterpaper]{IEEEtran}`

Strict page limit for report, max 8 pages (excluding bio and references). More than 8 pages $$\Rightarrow$$ Fail 

---

# [Grading of the project](https://www.ntnu.no/wiki/display/tfe4487/Grading+of+the+project)

---

# [Tapeout Review](https://www.ntnu.no/wiki/display/tfe4487/Tapeout+Review)

---

4'th of April, presentation of project

2 - 5 slides

Why, how, what


Affects coolness

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
| 12   | Paper                | Energy sources                                                           | Layout/LPE simulation    |          |
| 13   | Slides               | **Chip infrastructure**                                                          | Layout/LPE simulation    | x        |
| 14   |                      | Tapeout review                                                               | M4. Tapeout review       |          |
| 15   |                      | Easter                                                                       |                          |          |
| 16   |                      | Easter                                                                       |                          |          |
| 17   |                      | Exam repetition                                                              |                          |          |

---


# Goal

Few words on **I/O**

Understand **why** we need power on reset and brown out reset 

Understand **how** POR/BOR could made

Thoughts on infrastructure

---

#[fit] I/O 

---

#[fit] Input buffer

![right fit](../media/fig_methodology.pdf)

---

![fit](../media/l12_in1.pdf)

---

#[fit] Digital output

---

![fit](../media/l12_do1.pdf)

---

![fit](../media/l12_do2.pdf)

---

![fit](../media/l12_do3.pdf)

---

![fit](../media/l12_do4.pdf)

---

#[fit] Latch-up

Logic cells close to large NMOS pad drivers are prone to latch-up.

The latch-up process can start with electrons injected into the p-type substrate.

![right 200%](../media/fig_inv.pdf)

---
# Latch-up

1. Electrons injected into substrate, diffuse around, but will be accelerated by n-well to p-substrate built in voltage. Can end up in n-well
2. PMOS drain can be forward biased by reduced n-well potential. Hole injection into n-well. Holes diffuse around, but will be accelerated by n-well to p-substrate built in voltage. Can end up in p-substrate under NMOS
3. NMOS source pn-junction can be forward biased. Electrons injected into p-substrate. Diffuse around, but will be accelerated by n-well to p-substrate built in voltage.
4. Go to 2 (latch-up)
   
![right fit](../media/scr_eh.pdf)

---

# High-speed I/O

# [LVDS](https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=LVDS&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&refinements=PublicationTitle:IEEE%20Journal%20of%20Solid-State%20Circuits)

# [SERDES](https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=SERDES&highlight=true&returnType=SEARCH&matchPubs=true&sortType=newest&returnFacets=ALL&refinements=PublicationTitle:IEEE%20Journal%20of%20Solid-State%20Circuits)

---

#[fit] POR / BOR

---

![fit](../media/logic.pdf)


---

![fit](../media/nRF53.png)

---

![fit](../media/l12_reset.pdf)

---

![fit](../media/l12_reset1.pdf)

---

![fit](../media/l12_reset2.pdf)


---

![fit](../ip/l12_por0.pdf)

---

![fit](../ip/l12_por1.pdf)

---


![fit](../ip/l12_por2.pdf)

---

![fit](../ip/l12_por3.pdf)

---

![fit](../ip/l12_por4.pdf)

---

![fit](../ip/l12_por5.pdf)

---

![fit](../ip/l12_por6.pdf)

---

#[fit] Infrastructure

---


![fit](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Skyscrapercompare.svg/750px-Skyscrapercompare.svg.png)


---

![left fit](https://upload.wikimedia.org/wikipedia/en/9/93/Burj_Khalifa.jpg) 

![right fit](https://static.boredpanda.com/blog/wp-content/uploads/2020/12/sustainable-tiny-home-project-escape-vista-boho-xl-ikea-50-1.jpg)

---

![left fit](https://upload.wikimedia.org/wikipedia/en/9/93/Burj_Khalifa.jpg) 

![right 170%](https://www.xda-developers.com/files/2022/03/Appple-m1-Ultra-die-shot.jpg)

---

![left fit](https://static.boredpanda.com/blog/wp-content/uploads/2020/12/sustainable-tiny-home-project-escape-vista-boho-xl-ikea-50-1.jpg)

![right](https://s.zeptobars.com/Nordic-NRF24L01P.jpg)

---

# All modern SoCs need infrastructure IPs

Voltage Regulators : LDO, BUCK, BOOST 

Power on Reset 

Current sources

Voltage references

Clock sources : XO, RC, PLL, DLL, FLL

---

#[fit] All SoCs need infrastructure IPs

# so I can make them and sell them!!!! 

# \#getrich

---


![left fit](https://upload.wikimedia.org/wikipedia/en/9/93/Burj_Khalifa.jpg) 

![right fit](https://static.boredpanda.com/blog/wp-content/uploads/2020/12/sustainable-tiny-home-project-escape-vista-boho-xl-ikea-50-1.jpg)


---


#[fit] Thanks!






