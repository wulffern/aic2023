footer: Carsten Wulff 2023
slidenumbers:true
autoscale:true
theme:Plain Jane,1

<!--pan_skip: -->

# TFE4188 - Lecture 11
# Analog SystemVerilog

<!--pan_title: Lecture 11 - Analog SystemVerilog -->

---

<!--pan_skip: -->

# Goal

Explain why we need **Analog SystemVerilog** models

Introduction to Analog SystemVerilog 

---



<!--pan_skip: -->


#[fit] Why 



---

<!--pan_doc: 

<iframe width="560" height="315" src="https://www.youtube.com/embed/56oK9FAE858" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


-->


<!--pan_doc:



Design of integrated circuits is split in two, analog design, and digital design. 

Digital design is highly automated. The digital functions are coded in SystemVerilog (yes, I know 
there are others, but don't use those), translated into a gate level netlist, and automatically generated
layout. Not everything is push-button automation, but most is.

Analog design, however, is manual work. We draw schematic, simulation with a mathematical 
model of the real world, draw the analog layout needed for the foundries to make the circuit,
verify that we drew the schematic and layout the same, extract parasitics, simulate again, and in the end
get a GDSII file. 

When we mix analog and digital designs, we have two choices, analog on top, or digital on top. 

In analog on top we take the digital IP, and do the top level layout by hand in analog tools.

In digital on top we include the analog IPs in the SystemVerilog, 
and allow the digital tools to do the layout. 
The digital layout is still orchestrated by people. 

Which strategy is chosen depends on the complexity of the integrated circuit. For medium to low level 
of complexity, analog on top is fine. For high complexity ICs, then digital on top is the way to go.


Below is a description of the open source digital-on-top flow. The analog is included into GDSII 
at the OpenRoad stage of the flow. 

The GDSII is not sufficient to integrate the analog IP. The digital needs to know how the analog works, 
what capacitance is on every digital input, the propagation delay for digital input to digital outputs
, the relation between digital outputs and clock inputs, and the possible load on digital outputs.

The details on timing and capacitance is covered in a Liberty file. The behavior, or function 
of the analog circuit must be described in a SystemVerilog file. 

But how do we describe an analog function in SystemVerilog? SystemVerilog is simulated 
in an digital simulator. 
-->

![](../media/dig_des.svg)

---

# Digital simulation

<!--pan_doc: 

Conceptually, the digital simulator is easy. 

-->

- The order of execution of events at the same time-step do not matter

- The system is causal. Changes in the future do not affect signals in the past or the now


<!--pan_doc:

In a digital simulator there will be an event queue, see below. From start, set the current time step equals 
to the next time step. Check if there are any events scheduled for the time step.
Assume that execution of events will add new time steps. Check if there is another time step, and repeat. 

Since the digital simulator only acts when something is supposed to be done, they are inherently fast, 
and can handle complex systems.

-->

![left fit](../media/eventqueue.png)


<!--pan_doc:

It's a fun exercise to make a digital simulator. On my Ph.D I wanted to model ADCs, and first
I had a look at SystemC, however, I disliked C++, so I made [SystemDotNet](https://sourceforge.net/projects/systemdotnet/)

In SystemDotNet I implemented the event queue as a hash table, so it ran a bit faster. See below.

-->

---

![left fit](../media/systemdotnet.png)

### Digital Simulators

<!--pan_doc:

There are both commercial an open source tools for digital simulation. If you've never 
used a digital simulator, then I'd recommend you start with iverilog. I've made some examples 
at [dicex](https://github.com/wulffern/dicex/tree/main/project/verilog).

-->

**Commercial**

- [Cadence Excelium](https://www.cadence.com/ko_KR/home/tools/system-design-and-verification/simulation-and-testbench-verification/xcelium-simulator.html)
- [Siemens Questa](https://eda.sw.siemens.com/en-US/ic/questa/simulation/advanced-simulator/)
- [Synopsys VCS](https://www.synopsys.com/verification/simulation/vcs.html)

**Open Source**
- [iverilog/vpp](https://github.com/steveicarus/iverilog)
- [Verilator](https://www.veripool.org/verilator/)
- [SystemDotNet](https://sourceforge.net/projects/systemdotnet/)



---



### Counter

<!--pan_doc:

Below is an example of a counter in  SystemVerilog. The code can be found at [counter_sv](https://github.com/wulffern/dicex/tree/main/sim/verilog/counter_sv).

In the always\_comb section we code what will become the combinatorial logic. 
In the always\_ff section we code what will become our registers. 

-->

[.column]

```verilog
module counter(
               output logic [WIDTH-1:0] out,
               input logic              clk,
               input logic              reset
               );

   parameter WIDTH = 8;

   logic [WIDTH-1:0]                    count;
   always_comb begin
      count = out + 1;
   end

   always_ff @(posedge clk or posedge reset) begin
      if (reset)
        out <= 0;
      else
        out <= count;
   end

endmodule // counter
```

[.column]



<!--pan_doc:

In the context of a digital simulator, we can think through how the event queue will look. 

When the clk or reset changes from zero to 1, then schedule an event where if the reset is 1, then 
out will be zero in the next time step. If reset is 0, then out will be count in the next time step. 

In a time-step where out changes, then schedule an event to set count to out plus one. As such, each 
positive edge of the clock at least 2 events must be scheduled in the register transfer level (RTL) simulation. 

For example: 
-->

```bash 
Assume `clk, reset, out = 0`

Assume event with `clk = 1`

0: Set `out = count` in next event (1)

1: Set `count = out + 1` using 
   logic (may consume multiple events) 

X: no further events
```
---

<!--pan_doc:

When we synthesis the code below into a [netlist](https://github.com/wulffern/dicex/blob/main/sim/verilog/counter_sv/counter_netlist.v)
it's a bit harder to see how the events will be scheduled, but we can notice that clk and reset
are still inputs, and for example the clock is connected to d-flip-flops. The image below is 
the synthesized netlist

It should feel intuitive that a gate-level netlist will take longer to simulate than an RTL, there
are more events.

-->


![](../media/sv_counter.png)


---

# Transient analog simulation 


[.column]

<!--pan_doc:

Analog simulation are different. There is no quantized time step. How fast "things" 
happen in the circuit is entirely determined by the time constants, change in voltage, 
and change in current in the system. 

It is possible to have a fixed time-step in analog simulation, for example, we say that nothing
is faster than 1 fs, so we pick that as our time step. If we wanted to simulate 
1 s, however, that's at least 1e15 events, and with 1 event per microsecond on a computer it's still a 
simulation time of 31 years. Not a viable solution for all analog circuits. 

Analog circuits are also non-linear, properties of resistors, capacitors, inductors, diodes may 
depend on the voltage or current across, or in, the device. Solving for all the
non-linear differential equations is tricky.

An analog simulation engine must 
-->
parse spice netlist, and setup partial/ordinary differential equations for node matrix

<!--pan_doc: 

The nodal matrix could look like the matrix below, $i$ are the currents, $v$ the voltages, 
and $G$ the conductances between nodes.

-->

$$
\begin{pmatrix}
G_{11} &G_{12}  &\cdots  &G_{1N} \\ 
G_{21} &G_{22}  &\cdots  &G_{2N} \\ 
\vdots &\vdots  &\ddots  & \vdots\\ 
G_{N1} &G_{N2}  &\cdots  &G_{NN} 
\end{pmatrix}
\begin{pmatrix}
v_1\\ 
v_2\\ 
\vdots\\ 
v_N
\end{pmatrix}=
\begin{pmatrix}
i_1\\ 
i_2\\ 
\vdots\\ 
i_N
\end{pmatrix}
$$


[.column]

<!--pan_doc:

The simulator, and devices 
-->
model the non-linear current/voltage behavior between all nodes

<!--pan_doc:

as such, the $G$'s may be non-linear functions, and include the $v$'s and $i$'s.

Transient analysis use 
-->
numerical methods to compute time evolution 

<!--pan_doc:

The time step is adjusted automatically, often by proprietary algorithms, to trade 
accuracy and simulation speed. 

The numerical methods can be forward/backward Euler, or the others listed below.

-->

- [Euler](https://aquaulb.github.io/book_solving_pde_mooc/solving_pde_mooc/notebooks/02_TimeIntegration/02_01_EulerMethod.html)
- [Runge-Kutta](https://aquaulb.github.io/book_solving_pde_mooc/solving_pde_mooc/notebooks/02_TimeIntegration/02_02_RungeKutta.html)
- [Crank-Nicolson](https://en.wikipedia.org/wiki/Crank%E2%80%93Nicolson_method)
- [Gear](https://ieeexplore.ieee.org/document/1083221)


<!--pan_doc:


If you wish to learn more, I would recommend starting with the original paper on analog transient analysis. 

-->

---

[.column]

[SPICE (Simulation Program with Integrated Circuit Emphasis)](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1973/ERL-m-382.pdf)
published in 1973 by Nagel and Pederson

[.column]

<!--pan_doc:

The original paper has spawned a multitude of commercial, free and open source simulators, some are listed below. 

If you have money, then buy Cadence Spectre. If you have no money, then start with ngspice. 

-->


**Commercial**
- [Cadence Spectre](https://www.cadence.com/ko_KR/home/tools/custom-ic-analog-rf-design/circuit-simulation/spectre-simulation-platform.html)
- [Siemens Eldo](https://eda.sw.siemens.com/en-US/ic/eldo/)
- [Synopsys HSPICE](https://www.synopsys.com/implementation-and-signoff/ams-simulation/primesim-hspice.html)


**Free**
- [Aimspice](http://aimspice.com)
- [Analog Devices LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)
- [xyce](https://xyce.sandia.gov)

**Open Source**
- [ngspice](http://ngspice.sourceforge.net)


---


<!--pan_doc:

# Mixed signal simulation

It is possible to co-simulate both analog and digital functions. An illustration is shown below.

The system will have two simulators, one analog, with transient simulation and differential equation solver,
and a digital, with event queue.

Between the two simulators there would be analog-to-digital, and digital-to-analog converters. 

To orchestrate the time between simulators there must be a global event and time-step control. 
Most often, the digital simulator will end up waiting for the analog simulator.

The challenge with mixed-mode simulation is that if the digital circuit becomes to large,
and the digital simulation must wait for analog solver, then it does not work. 

Most of the time, it's stupid to try and simulate complex system-on-chip with mixed-signal
, full detail, simulation. 

For IPs, like an ADC, co-simulation works well, and is the best way to verify the digital and analog.

But if we can't run mixed simulation, how do we verify analog with digital?

-->

![fit](../media/mixed_simulator.pdf)

---



#[fit] Analog SystemVerilog Example

---

[.column]

<!--pan_skip: -->

# TFE4152 2021 - Project


Be inspired by the ISSCC paper, and design a similar system. 

Design analog circuits in SPICE 

Design digital circuits in SystemVerilog


[A 10 000 Frames/s CMOS Digital Pixel Sensor](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=972156)

[.column]

![inline fit](../ip/block_diagram_modified.pdf)


---

<!--pan_skip: -->

![left fit](../ip/pixelSensor.png)

![right fit](../ip/timing_diagram.png)

---

<!--pan_doc:

The key idea is to model the analog behavior to sufficient detail such that we can
verify the digital code. I think it's best to have a look at a concrete example.

Take a high-speed camera IC, as illustrated below. Each pixel consists of a sensor, comparator and a memory,
which are analog functions.

The control of each pixel, and the readout of each pixel is digital. 

The image below is a model of the system in [A 10 000 Frames/s CMOS Digital Pixel Sensor](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=972156).

The principle of the paper is as follows:
- in each pixel, sample the output of the light sensor
- from top level, feed a digital ramp, and an analog ramp to all pixels at the same time 
- in each pixel, use comparator to lock the memory when the analog ramp matches the sampled 
output from the sensor 

As such, the complete image is converted from analog to digital in parallel. 

-->

![original fit](../media/pixelSensorModel.pdf)

---

<!--pan_skip: -->

# What you got



[github.com/wulffern/dicex](https://github.com/wulffern/dicex)

```
project/
├── spice/
│   ├── Makefile                # See https://www.gnu.org/software/make/manual/html_node/Introduction.html
│   ├── pixelSensor.cir         # Almost empty circuit for pixelSensor
│   └── pixelSensor_tb.cir      # SPICE testbench for pixelSensor, emulates verilog
└── verilog/
    ├── Makefile                
    ├── pixelSensor.fl          # Verilog file list
    ├── pixelSensor_tb.gtkw     # Save file for GTKWave
    ├── pixelSensor_tb.v        # Verilog testbench for pixelSensor
    └── pixelSensor.v           # Verilog model of analog pixelSensor circuit
```


---

<!--pan_doc: 

The verilog below shows how the "Analog SystemVerilog" can be written.

In SystemVerilog there are "real" values for signals and values, or floating point. 

The output of the sensor is modeled as the `tmp`` variable. First tmp is reset to 
`v_erase` on the `ERASE` signal.
-->

[.column]

```verilog 

module PIXEL_SENSOR
  (
   input logic      VBN1,
   input logic      RAMP,
   input logic      RESET,
   input logic      ERASE,
   input logic      EXPOSE,
   input logic      READ,
   inout [7:0] DATA

   );

   real             v_erase = 1.2;
   real             lsb = v_erase/255;
   parameter real   dv_pixel = 0.5;

   real             tmp;
   logic            cmp;
   real             adc;

   logic [7:0]      p_data;

   //----------------------------------------------------------------
   // ERASE
   //----------------------------------------------------------------
   // Reset the pixel value on pixRst
   always @(ERASE) begin
      tmp = v_erase;
      p_data = 0;
      cmp  = 0;
      adc = 0;
   end

```

<!--pan_doc:

When `EXPOSE` is enabled to collect light, we reduce the `tmp` value proportional to an lsb and 
a derivative `dv_pixel`. The `dv_pixel` is a parameter we can set on each pixel to model the 
light. 

The RAMP input signal is the analog ramp on the top level fed to each pixel. However, 
since I did not have real wires in `iverilog` I had to be creative. Instead of a continuous 
increasing value the `RAMP` is a clock that toggles 255 times. The actual "input" to the 
ADC is the `adc` variable, but that is generated locally in each pixel. When the `adc` exceeds 
the `tmp` we set `cmp` high.

The previous paragraph demonstrates an important point on analog systemVerilog models. 
They don't need to be exact, and they don't need to reflect exactly what happens in the "real world"
of the analog circuit. What's important is that the behavior from the outside resembles 
the real analog circuit, and that the digital designer makes the correct design choices. 

The comparator locks the `p_data`, and, as we can see, the `DATA` is a tri-state bus that 
is used both for reading and writing. 

-->

[.column]

```verilog 
   //----------------------------------------------------------------
   // SENSOR
   //----------------------------------------------------------------
   // Use bias to provide a clock for integration when exposing
   always @(posedge VBN1) begin
      if(EXPOSE)
        tmp = tmp - dv_pixel*lsb;
   end

   //----------------------------------------------------------------
   // Comparator
   //----------------------------------------------------------------
   // Use ramp to provide a clock for ADC conversion, assume that ramp
   // and DATA are synchronous
   always @(posedge RAMP) begin
      adc = adc + lsb;
      if(adc > tmp)
        cmp <= 1;
   end

   //----------------------------------------------------------------
   // Memory latch
   //----------------------------------------------------------------
   always_comb  begin
      if(!cmp) begin
         p_data = DATA;
      end

   end

   //----------------------------------------------------------------
   // Readout
   //----------------------------------------------------------------
   // Assign data to bus when pixRead = 0
   assign DATA = READ ? p_data : 8'bZ;

endmodule // re_control

```


<!--pan_doc:

For more information on real-number modeling I would recommend [The Evolution of Real Number Modeling](https://youtu.be/gNpPslQZT-Y)

<iframe width="560" height="315" src="https://www.youtube.com/embed/gNpPslQZT-Y"
title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
allowfullscreen></iframe>

-->

---

<!--pan_skip: -->

![](https://youtu.be/gNpPslQZT-Y)

---

#[fit] Thanks!
