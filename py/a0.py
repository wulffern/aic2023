#!/usr/bin/env python3

from scipy import constants
pi = constants.pi
h = constants.physical_constants["Planck constant"][0]
alpha = constants.physical_constants["fine-structure constant"][0]
c = constants.physical_constants["speed of light in vacuum"][0]
me = constants.physical_constants["electron mass"][0]

a0f = 0.528e-10
a0 = (2*pi*1/alpha * h/c/me)
a1 = (1/alpha * h/c/me)
print("a0f = %g"%a0f)
print("a0 = %g"%a0)
print("a1 = %g"%a1)
print("a1/a0f = %g"%(a1/a0f))


a0m = (1/alpha * h/c/me/(2*pi))
print(a0m)
