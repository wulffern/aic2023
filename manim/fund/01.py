#!/usr/bin/env python3

from manim import *
from manim_physics import *
import skimage


class Atoms(Scene):
    def construct(self):
        """
        # Atoms
        The world is made of atoms.

        The simplest atom consist of 1 positive charge,
        and 1 negative charge.

        The positive and negative charge balance eachother perfectly,
        so seen from far away, the atom is neutral.

        The paths that electrons take around the positron
        is complex, and obeys the maths of quantum physics.


        """

        t1 = Text("The world is made of atoms")
        self.play(FadeIn(t1))
        self.wait(5)
        self.clear()

        pos = Charge(1)

        e1 = Charge(-1,LEFT)

        self.play(FadeIn(pos))
        self.wait(1)
        self.play(FadeIn(e1))
        self.play(
            Rotate(e1, angle=2*PI,run_time=10,about_point=ORIGIN,rate_func=linear),
            )
        self.wait()
        t = Text("Hydrogen",font_size=96)
        t.to_edge(UP+LEFT)
        self.play(FadeIn(t))
        self.wait(2)


        self.clear()
        image_numpy = skimage.io.imread("https://upload.wikimedia.org/wikipedia/commons/e/e7/Hydrogen_Density_Plots.png")
        img = ImageMobject(image_numpy)
        img.height = 8
        self.play(FadeIn(img))
        self.wait(10)
        self.clear()
        self.wait(1)


class Electron(Scene):
    def construct(self):
        """
        # Electron

        The electron is a fundamental particle,
        as far as we know, it is not composed of smaller parts.

        The negative charge of the electron is small

        All electrons are exaclty the same, and two electrons
        cannot occupy the same quantum state
        """

        e = Charge(-10,LEFT)
        e.to_edge(LEFT)

        self.play(FadeIn(e))
        self.wait(2)

        t = MathTex(r"q = -1.602176634\times10^{-19}\text{ C}")
        t.to_edge(RIGHT)

        self.play(FadeIn(t))
        self.wait(4)
        self.clear()
        self.wait()

class Quantum(Scene):
    def construct(self):

        variables = VGroup(MathTex("{\psi(\vec{r},t)}")).arrange_submobjects().shift(UP)

        s = MathTex(r"\hat{H} {\psi(\vec{r},t)} = i \hbar \frac{d}{dt}{\psi(\vec{r},t)}",font_size=100)
        s1 = MathTex(r"\hat{H} {\psi(\vec{r},t)} - i \hbar \frac{d}{dt}{\psi(\vec{r},t)} = 0",font_size=100)
        s2 = MathTex(r"\left[\hat{H} - i \hbar \frac{d}{dt}\right]{\psi(\vec{r},t)} = 0",font_size=100)


        self.add(s)
        self.wait(1)
        self.play(TransformMatchingTex(s, s1))
        self.wait(1)
        self.play(TransformMatchingTex(s1, s2))
        self.wait(1)
