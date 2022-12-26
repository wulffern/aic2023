footer: Carsten Wulff 2023
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica
    
#[fit] A new analog paradigm?

---

[.background-color:#000000]
[.text: #FFFFFF]
# There will always be analog circuits, because the real world is analog

---


### Life of an analog designer: Schematic Design

[.column]
![inline](../media/l00_schematic.pdf)

[.column]
![inline](../media/l00_simulation.pdf)

---
### Life of an analog designer: Layout Design

[.column]
![inline](../media/l00_layout.pdf)

[.column]
![inline](../media/l00_simulation.pdf)

---
[.table-separator: #000000, stroke-width(1)] 
[.table: margin(20)]
# Current thoughts on new analog paradigm 

| Status | Abstraction | Design            | Layout      | Why                                                     |
|:-------:|:-----------|:-----------------|:-----------|:-------------------------------------------------------|
| :construction:       | Chip        | SystemVerilog     | digital     | Complex connections, few analog interfaces              |
| :construction:       | Module      | SystemVerilog     | digital     | Large amount of digital signals, few analog signals     |
| :warning:       | Block       | Schematic         | programatic | Large amount of critical analog interfaces, few digital |
| :white_check_mark:      | Cell        | Schematic/JSON | compiled    | Few analog interfaces, few digital interfaces                                 |
| :white_check_mark:      | Device      | JSON              | compiled    | Polygon pushing                                         |
| :white_check_mark:      | Technology  | JSON/Rules        | compiled    | Custom for each technology                              |



---
[.background-color:#000000]
[.text: #FFFFFF]
# My journey on "How can I simplify analog design?"

---
#[fit] Trigger 

![inline fit](../media/acdncmos.png)

![right fit](../media/trigger.png)

---
#[fit] Problem

![right fit](../media/efficient_adcs.png)

---

#[fit] Architecture

![inline 90%](../media/draxelmayr.gif)

![right fit](../media/draxl1.png)

---

#[fit] Plan 

9-bit SAR ADC with 28 nm FDSOI transistors

9-bit SAR ADC with IO voltage (180 nm) FDSOI transistors

---


# How to make multiple SAR ADCs with limited time?


Spend 50% of time for 6 months to **develop** a tool to make SAR ADCs

Spend 50% of time for 6 months to **make** the SAR ADCs







---
![inline](../media/cnano.pdf)

16 k Perl lines. Ported to C++ for speed $$\Rightarrow$$ [ciccreator](https://github.com/wulffern/ciccreator)

---

![inline](../media/transistor.pdf)

---

![inline](../media/inverter.pdf)

---

![inline](../media/adcs.pdf)

---

[A Compiled 9-bit 20-MS/s 3.5-fJ/conv.step SAR ADC in 28-nm FDSOI for Bluetooth Low Energy Receivers](https://ieeexplore.ieee.org/document/7906479)

![inline](../media/wulff_fig_table.pdf)

---

![inline](../media/harald.pdf)![inline](../media/harald_layout.pdf)

---
# Since then 

Measured: 28 nm FDSOI, 55 nm 
Ported: 22 nm FDSOI, 22 nm, 28 nm, 65 nm, 130 nm

Finally, there is an open source port to skywater 130nm! 
[wulffern/sun_sar9b_sky130nm](https://github.com/wulffern/sun_sar9b_sky130nm)

![right fit](../media/l00_SAR9B_CV.png)

---
[.background-color:#000000]
[.text: #FFFFFF]

#[fit] Key learnings

---

#[fit] Device

---

# Super simple transistor was a good choice for portability
---

[.column]

```json
        { "name" : "DMOS_BULKN" ,
          "class" : "Gds::GdsPatternTransistor",
          "abstract" : 1,
          "yoffset": -0.5,
          "widthoffset" : -0.5,
           "fillCoordinatesFromStrings" : [
               [   "OD",
                  "-------------------",
                  "----xxx------------",
                  "----xxx------------",
                  "----xxx------------",
                  "-------------------"
              ],
              ...
              [   "M1",
                  "----------------xxx",
                  "----wDw---------xxx",
                  "----------wGw---xBx",
                  "----wSw---------xxx",
                  "----------------xxx"
              ],
              ...
              [   "NDIFFC",
                  "-------------------",
                  "----LTR------------",
                  "-------------------",
                  "----LTR------------",
                  "-------------------"
              ]
          ]
        }
```

[.column]

```json
{ "name" : "DMOS" ,
  "class" : "Gds::GdsPatternTransistor",
  "yoffset": -0.5,
  "type": "pch",
  "widthoffset" : -1,
  "fillCoordinatesFromStrings" : [
   [  "OD",
      "------------------xxxx",
      "----xxK-----------xCxC",
      "----xxx-----------xxxx",
      "----xxK-----------xCxC",
      "------------------xxxx"
   ],
   [  "PO",
      "-mmmmmmmmmmmmm--------",
      "----------------------",
      "-mmmmmmmmmmcxc--------",
      "----------------------",
      "-mmmmmmmmmmmmm--------"
   ],
   [  "M1",
      "------------------xxxx",
      "----wDww----------xxxx",
      "-----------wGww---xBxx",
      "----wSww----------xxxx",
      "------------------xxxx"
   ]
  ],
  "afterNew" : {
    "copyColumns" :[
      { "count" : 0, "offset" : 4,"length" : 4}
    ]
  }
}
```


---

#[fit] Cell

---


Generic netlist based placement worked for most cells
<br>
<br>
All necessary routing info was possible to add in JSON
<br>
<br>

JSON was portable between technologies with limited changes

---

[.column]

2016 (Perl compiler)

```json 
{ "name": "SARCMPHX1_CV",
  "description" : "Half a strong-arm comparator",
  "class" : "Layout::LayoutDigitalCell",
  "setYoffsetHalf" :  "" ,
  "rows" : 7,
  "beforeRoute" : {
    "addDirectedRoutes" : [ ["PO","VMR","MN6:G-MP6:G"],
                            ["M1","VMR","MP4:G||MP6:G"],
                            ["M1","CI","MN1:G||MN5:G"],
                            ["M1","N2","MN1:D,MN3:D,MN5:D-|--MP1:D"],
                            ["M1","N1","MN0:D,MN2:D|-MN4:D"],
                            ["M1","N1","MN0:D-|--MP0:S"],
                            ["M1","CO","MP3:D,MP5:D--|-MN6:D"],
                            ["PO","CK","MN0:G-MP0:G"],
                            ["M1","CK","MP0:G,MP1:G-|MP3:G"],
                            ["M4","NC","MP2$:D--|--MP2:G"]
                          ]
    },
    "afterRoute" : {
    "addPortOnRects" : [ ["AVDD","M4" ],
       ["N1","M1","MN4:D"],
       ["N2","M1","MN5:D" ]]
 }
}

```

[.column]

2022 (C++ compiler)

```json 
{ "name": "SARCMPHX1_CV",
  "description" : "Half a strong-arm comparator",
  "class" : "Layout::LayoutDigitalCell",
  "setYoffsetHalf" :  1 ,
  "rows" : 7,
  "meta" : {
       "noSchematic" : true
  },
  "decorator" : [
     {"ConnectSourceDrain" : ["M1","||",""]}
  ],
  "beforeRoute" : {
    "addDirectedRoutes" : [ ["PO","VMR","MN6:G-MP6:G"],
                            ["M1","VMR","MP4:G||MP6:G"],
                            ["M1","CI","MN1:G||MN5:G"],
                            ["M1","N2","MN1:D,MN3:D,MN5:D-|--MP1:D"],
                            ["M1","N1","MN0:D,MN2:D|-MN4:D"],
                            ["M1","N1","MN0:D-|--MP0:S"],
                            ["M1","CO","MP3:D,MP5:D--|-MN6:D"],
                            ["PO","CK","MN0:G-MP0:G"],
                            ["M1","CK","MP0:G,MP1:G-|MP3:G"],
                            ["M4","NC","MP2$:D-|--MP2:G"]
                          ]
    },
    "afterRoute" : {
              "addPortOnRects" : [["BULKP","M1"],
                  ["BULKN","M1"],
                  ["AVDD","M4" ],
                  ["N1","M1","MN4:D"],
                  ["N2","M1","MN5:D" ]]
    }
}

```

---

#[fit] Block

---

[.column]
Examples: CDAC, Capacitance cell, SAR

Required extentions of generic class to allow
for custom placement and routing specific to one block 

C++ is not the right language, too slow to write 

Since most cells are instances, and there is little polygon pushing (few rectangles) the language does not need to be fast.

A high level language like Python would be better for blocks

[.column]

```cpp
namespace cIcCells{
    void CDAC::place()
    {
        //...
        
        //Find how many nets called CP
        QStringList nodes= subckt()->nodes();
        int i=-1;
        foreach(QString s,nodes){
            if(s.contains("CP")){
                i += 1;
            }
        }
        
        int prev_width = 0;
        int x =  (xw + xs*2)*(i+2);
        int y = 0;
        bool first = true;
        
        foreach(cIcSpice::SubcktInstance * 
            ckt_inst,_subckt->instances()){
            inst= this->addInstance(ckt_inst,x,y);
            y += inst->height();
            if(first){
                firstinst = inst;
                first = false;
            }
        }
        this->adjust(-xs*2+xw,0,0,0);

        //Add the route rings
        for(auto k=i;k>=0;k--){
            QString name = QString("CP<%1>").arg(k);
            this->addRouteRing("M2",name,"l",1,2,false);
            
        }
        //...
    }
    //....
}

```


---
#[fit] Summary
---

# Usage is hard, requires a new type of analog designer/programmer

---
# If I could start again

Write high level stuff, that does not need to be fast, in Python

Write polygon pushing in CPython, so it's ultra fast

---


#[fit] [wulffern/aicex](https://github.com/wulffern/aicex)

---
#[fit] Thanks!
