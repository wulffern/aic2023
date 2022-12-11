#!/usr/bin/env python3

from manim import *
from manim_physics import *


class Particles(Scene):
    def construct(self):

        pos = Charge(2)

        e1 = Charge(-1,LEFT)
        e2 = Charge(-1,RIGHT)

        self.play(FadeIn(pos))
        self.wait(1)
        self.play(FadeIn(e1,e2))
        self.play(
            Rotate(e1, angle=2*PI,run_time=10,about_point=ORIGIN,rate_func=linear),
            Rotate(e2, angle=2*PI,run_time=10,about_point=ORIGIN,rate_func=linear)
            )
        self.wait()
        t = Text("Helium",font_size=96)
        t.to_edge(UP+LEFT)
        self.play(FadeIn(t))
        self.wait(2)
