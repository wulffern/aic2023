# Introduction

The purpose of the introduction is to put the reader into the right
frame of mind. Introduce the problem statement, key references, the key
contribution of your work, and an outline of the work presented. Think
of the introduction as explaining the "Why" of the work.

Although everyone has the same assignment for the project, you have
chosen to solve the problem in different ways. Explain what you consider
the problem statement, and tailor the problem statement to what the
reader will read.

Key references, like [@klein01], is introduced. Don't copy the paper
text, write why they designed the circuit, how they chose to implement
it, and what they achieved. The reason we reference other papers in the
introduction is to show that we understand the current state-of-the-art.
As such, maybe find other, more recent, image sensors. Provide a summary
where state-of-the-art has moved since the original paper.

The outline should be included towards the end of the introduction. The
purpose of the outline is to make this document easy to read. A reader
should never be surprised by the text. All concepts should be eased
into. We don't want the reader to feel like they been thrown in at the
end of a long story. As such, if you chosen to solve the problem
statement in a way not previously solved in a key references, then you
should explain that.

A checklist for all chapters can be seen in table below.

# Theory

It is safe to assume that all readers have read the key reference
[@klein01], if they have not, then expect them to do so. The purpose of
the theory section is not to demonstrate that you have read the paper,
but rather, highlight theory that the reader probably does not know. The
theory section should give sufficient explanation to bridge the gap
between references, and what you apply in this text.

# Implementation

The purpose of the implementation is to explain what you did. How have
you chosen to architect the solution, how did you split it up in analog
and digital parts? Use one subsection per circuit.

For the analog, explain the design decisions you made, how did you pick
the transistor sizes, and the currents. Use clear figures (i.e.
circuitikz), don't use pictures from schematic editors. How does the
circuit work? Did you make other choices than in [@klein01]?

For the digital, how did you divide up the digital? What were the design
choices you made? How did you split it up into finite state machines and
pixel array control? How did you implement readout of the data? Explain
what you did, and how it works. Use state diagrams and block diagrams.

# Result

The purpose of the results is to convince the reader that what you made
actually works. To do that, explain testbenches and simulation results.
The key to good results is to be critical of your own work. Do not try
to oversell the results. Your result should speak for them self.

For analog circuits, show results from each block. Highlight key
parameters, like current and delay of comparator. Demonstrate that the
full analog system works. Show that the correct digital value is stored
in memory. Check memory value for multiple pixel voltages, either by
changing the exposure time, or changing the pixel current.

Show simulations that demonstrate that the digital works. Show how you
read out the data from the pixel array.

# Discussion

Explain what the circuit and results show. Be critical.

# Future work

Give some insight into what is missing in the work. What should be the
next steps?

# Conclusion

Summarize why, how, what and what the results show.

# Appendix

Include in appendix the necessary files to reproduce the work. One good
way to do it is to make a github repository with the files, and give a
link here.

The SPICE and SystemVerilog for the actual circuit should be included
into the abstract directly. Testbenches, makefiles etc, can be linked
via github.



| **Item**                                                               | **Description**                                                                                                                                                                                                                                                                           | **OK** |
|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------|
| Is the problem description clearly defined?                            | Describe which parts of the problem you chose to focus on. The problem description should match the results you've achieved.                                                                                                                                                              |        |
| Is there a clear explanation why the problem is worth solving?         | The reader might need help to understand why the problem is interesting                                                                                                                                                                                                                   |        |
| Is status of state-of-the-art clearly explained?                       | You should make sure that you know what others have done for the same problem. Check IEEEXplore. Provide summary and references. Explain how your problem or solution is different                                                                                                        |        |
| Is the key contribution clearly explained?                             | Highlight what you've achieved. What was your contribution?                                                                                                                                                                                                                               |        |
| Is there an outline of the report?                                     | Give a short summary of what the reader is about to read                                                                                                                                                                                                                                  |        |
| Is it possible for a reader skilled in the art to understand the work? | Have you included references to relevant papers                                                                                                                                                                                                                                           |        |
| Is the theory section too long                                         | The theory section should be less than 10 % of the work                                                                                                                                                                                                                                   |        |
| Are all circuits explained?                                            | Have you explained how every single block works?                                                                                                                                                                                                                                          |        |
| Are figures clear?                                                     | Remember to explain all colors, and all symbols. Explain what the reader should understand from the figure. All figures must be referenced in the text.                                                                                                                                   |        |
| Is it clear how you verified the circuit?                              | It's a good idea to explain what type of testbenches you used. For example, did you use dc, ac or transient to verify your circuit?                                                                                                                                                       |        |
| Are key parameters simulated?                                          | You at least need current from VDD. Think through what you would need to simulate to prove that the circuit works.                                                                                                                                                                        |        |
| Have you tried to make the circuit fail?                               | Knowing how circuits fail will increase confidence that it will work under normal conditions.                                                                                                                                                                                             |        |
| Have you been critical of your own results?                            | Try to look at the verification from different perspectives. Play devil's advocate, try to think through what could go wrong, then explain how your verification proves that the circuit does work.                                                                                       |        |
| Have you explained the next steps?                                     | Imagine that someone reads your work. Maybe they want to reproduce it, and take one step further. What should that step be?                                                                                                                                                               |        |
| No new information in conclusion.                                      | Never put new information into conclusion. It's a summary of what's been done                                                                                                                                                                                                             |        |
| Story                                                                  | Does the work tell a story, is it readable? Don't surprise the reader by introducing new topics without background information.                                                                                                                                                           |        |
| Chronology                                                             | Don't let the report follow the timeline of the work done. What I mean by that is don't write "first I did this, then I spent huge amount of time on this, then I did that". No one cares what the timeline was. The report does not need to follow the same timeline as the actual work. |        |
| Too much time                                                          | How much time you spent on something should not be correlated to how much text there is in the report. No one cares how much time you spent on something. The report is about why, how, what and does it work.                                                                            |        |
| Length                                                                 | A report should be concise. Only include what is necessary, but no more. Shorter is almost always better than longer.                                                                                                                                                                     |        |
| Template                                                               | Use <https://github.com/wulffern/dic2021/tree/main/2021-10-19_project_report> template for the report. Write in LaTeX. You will need LaTeX for your project and master thesis. Use <http://overleaf.com> if you're uncomfortable with local text editors and LaTeX.                       |        |
| Spellcheck                                                             | Always use a spellchecker. Misspelled words are annoying, and may change content and context (peaked versus piqued)                                                                                                                                                                       |        |



[@klein01]: Kleinfelder, Lim, Liu, Gamal "A 10 000 Frames/s CMOS Digital Pixel Sensor", JSSC, VOL 36, NO 12, 2001

