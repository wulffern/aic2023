---
title: A refresher of the first 4 years of electronics
layout: post
permalink: refresh
---



<!--pan_title: A refresher-->

* TOC
{:toc }

# There is a standard unit of measurement

All known physical quantities are derived from 7 base units ([SI
units](https://en.wikipedia.org/wiki/International_System_of_Units))
, second (s), meter (m), kg (kilogram), ampere (A), kelvin (K), candela (cd).

All other units (for example volts), are derived from the base units.

I don't go around remembering all of them, they are easily available online. When you forget the equation for charge (Q), voltage (V) and capacitance (C), look at the units below, and you can see it's $Q = C V$[^1]

![](https://www.nist.gov/sites/default/files/images/2021/08/23/NIST.SP_.1247.png)



#  Electrons

Electrons are fundamental, they cannot (as far as we know), be divided
into smaller parts. Explained further in the [standard model of particle physics](https://en.wikipedia.org/wiki/Standard_Model)

Electrons have a negative charge of $q \approx 1.602 \times 10^{-19}$. The proton a positive charge. The two charges balance exactly! If you have a trillion electrons and a trillion protons inside a volume, the net external charge will be $0$ (assuming we measure from some distance away)

All electrons are the same, although the quantum state can be different.

An electron cannot occupy the same quantum state as another. This rule that applies to all Fermions (particles with spin of 1/2)

The quantum state of an electron is fully described by it's spin, momentum (p) and position in space (r).

#  Probability

The probability of finding an electron in a state as a function of space and time is 

$$ P = |\psi(r,t)|^2 $$

, where $\psi$ is named the probability amplitude, and is a complex function of space and time. In some special cases, it's

$$ \psi(r,t) = A e^{i( kr - \omega t)}$$

, where A is complex number, k is the wave number, r is the position vector from
some origin, $\omega$ is the frequency and $t$ is time.


The energy is $E = \hbar \omega$ , where $\hbar = h/2\pi$ and $h$ is 
[Planck Constant](https://en.wikipedia.org/wiki/Planck_constant) and the momentum is $p = \hbar k$

#  Uncertainty principle

We cannot, with ultimate precision, determine both the position and the momentum of a particle, the precision is 

$$\sigma_x \sigma_p \ge \frac{\hbar}{2}$$

From the [uncertainty principle](https://en.wikipedia.org/wiki/Uncertainty_principle) we can actually [estimate the size of the atom](https://wulffern.github.io/aic2023/atom)

#  States as a function of time and space

The time-evolution of the probability ampltiude is 

$$ i\hbar \frac{d}{dt} \psi(r,t) = H \psi(r,t)$$

, where H is named the Hamiltonian matrix, or the energy matrix or (if understand correctly) the ampltiude matrix of the probability amplitude to change from one state to another. 

For example, if we have a system with two states, a simplfied version of two electrons shared between two atoms, as in $H_2$, or hydrogen gas, or co-valent bonds, then the Hamiltonian is a 2 x 2 matrix. And the $\psi$ is a vector of $[\psi_1,\psi_2]$

Computing the solution to the [Schrodinger Equation](https://en.wikipedia.org/wiki/Schrödinger_equation) can be tricky, because you must know the number of relevant states to know the vector size of $\psi$ and the matrix size of $H$. In addition, the $H$ can be a function of time and space (I think).

Compared to the equations of electric fields, however, Schrodinger is easy, it's a set of linear differential equations.

#  Allowed energy levels in atoms

Solutions to Schrodinger result in quantized energy levels for a electron bound
to an atom.

Take hydrogen, the electron bound to the proton can only exists in quantized
energy levels. The lowest energy state can have two electrons, one with spin up,
and one with spin down.


From Schrodinger you can compute the energy levels, which most of us did at
somepoint, although now, I can't remember how it was done. That's not important.
The important is to internalize that the energy levels in bound electrons are
discrete.


Electrons can transition from one energy level to another by external influence,
i.e temperature, light, or other.


The probability of a state transition (change in energy) can be determined from
the probability amplitude and Schrodinger.


#  Allowed energy levels in solids

If I have two silicon atoms spaced far apart, then the electrons can have the
same spin and same momentum around their respective nuclei. As I bring the atoms
closer, however, the probability amplitudes start to interact (or the dimensions
of the Hamiltonian matrix grow), and there can be state transitions between the
two electrons.


The allowed energy levels will split. If I only had two states interacting, the Hamiltonian could be

$$ H = 
\begin{bmatrix}
A & 0 \\
0 & -A
\end{bmatrix}
$$

and the new energy levels could be 

$$ E_1 = E_0 + A$$

and 

$$ E_2 = E_0 - A$$

In a silicon crystal we can have trilions of atoms, and those that are close, have states that interact. **That's why crystals stay solids**. All chemical bonds are states of electrons interacting! Some are strong (co-valent bonds), some are weaker (ionic bonds), but it's all quantum states interacting.

The discrete energy levels of the electron transition into bands of allowed energy states. 

![](https://upload.wikimedia.org/wikipedia/commons/e/ef/Solid_state_electronic_band_structure.svg)

For a crystal, the allowed energy bands is captured in the [band structure](https://en.wikipedia.org/wiki/Electronic_band_structure)

# Silicon Unit Cell

A [silicon](https://en.wikipedia.org/wiki/Silicon) crystal unit cell is a diamond faced cubic with 8 atoms in the corners spaced at 0.543 nm, 6 at the center of the
faces, and 4 atoms inside the unit cell at a nearest neighbor distance of 0.235
nm. 

![](https://upload.wikimedia.org/wikipedia/commons/f/f1/Silicon-unit-cell-3D-balls.png)


# Valence band and Conduction band

The full band structure of a silicon unit cell is complicated. For bulk silicon
we simplify, and we think of two bands. In the  conduction band ($E_C$) is the
lowest energy where electrons are free (not bound to atoms). The valence band
($E_V$) is the highest band where electrons are bound to silicon atoms.  

The difference between  $E_C$ and $E_V$ is a property of the material we've named the band gap. 

$$ E_G = E_C - E_V$$


# Metals

In metals, the band splitting of the energy levels causes the valence band and conduction band to overlap. As such, electrons can easily transition between bound state and free state. As such, electrons in metals are shared over large distances, and there are many electrons readily available to move under an applied field, or difference in electron density. That's why metals conduct well.

# Isolators

In insulating materials the difference between the conduction band and the valence band is large. As a result, it takes a large energy to exite electrons to a state where they can freely move. 

That's why glass is transparent to optical frequencies. Visible light does not have sufficient energy to exite electrons from a bound state.

That's also why glass is opaque to ultra-violet, which has enough energy to exite electrons out of a bound state.

Based on these two pieces you could estimate the bandgap of glass.

# Semiconductors

In a silicon the bandgap is lower than an insulator, approximately $E_G = 1.12 eV$ for silicon.

At room temperature, that allows a small number of electrons to be excited into the conduction band, leaving behind a "hole" in the valence band.

# Fermi level

From Wikipedia's [Fermi level](https://en.wikipedia.org/wiki/Fermi_level)

> In band structure theory, used in solid state physics to analyze the energy
> levels in a solid, the Fermi level can be considered to be a hypothetical
> energy level of an electron, such that at thermodynamic equilibrium this
> energy level would have a 50% probability of being occupied at any given time

The fermi level is closely linked to the [Fermi-Dirac
distribution](https://en.wikipedia.org/wiki/Fermi%E2%80%93Dirac_statistics)

$$
f(E) = \frac{1}{e^{(E - E_F)/kT} + 1}
$$

If the energy of the state is more than a few kT away from the fermi-level, then

$$
f(E) \approx e^{(E_F - E)/kT}
$$


# Band diagrams

A [band diagram](https://en.wikipedia.org/wiki/Band_diagram) or energy level
diagrams shows the conduction band energy and valence band energy as a function
of distance in the material.

![](https://upload.wikimedia.org/wikipedia/commons/4/43/Pn-junction_zero_bias.png)

The horizontal axis is the distance, the vertical axis is the energy.

The figure shows a PN-junction 

# Density of electrons/holes 

There are two components needed to determine how many electrons are in the
conduction band. The density of available states, and the probability of an
electron to be in that quantum state. 

The probability is the Fermi-Dirac distribution. The density of available states
is a complicated calculation from the band-structure of silicon. See [Diodes](https://wulffern.github.io/aic2023/2021/07/08/Diodes.html)
for details.

$$ n_e = \int_{E_C}^{\infty} N(E)f(E) dE$$

The Fermi level is assumed to be independent of energy level, so we can write 

$$ n_e = e^{E_F/kT}  \int_{E_C}^{\infty} N(E) e^{-E/kT}dE$$

for the density of electrons in the conduction band.


# Fields 

There are equations that relate electric field, magnetic field, charge density
and current density to eachother. 

The equations

$$ \oint_{\partial \Omega} \mathbf{E} \cdot d\mathbf{S} = \frac{1}{\epsilon_0} \iiint_{V} \rho
\cdot dV$$  

,relates net electric flux to net enclosed electric charge

$$ \oint_{\partial \Omega} \mathbf{B} \cdot d\mathbf{S} = 0$$

,relates net magnetic flux to net enclosed magnetic charge

$$ \oint_{\partial \Sigma} \mathbf{E} \cdot d\mathbf{\ell} = - \frac{d}{dt}\iint_\Sigma \mathbf{B}
\cdot d\mathbf{S}$$

,relates induced electric field to changing magnetic flux

$$ \oint_{\partial \Sigma} \mathbf{B} \cdot d\mathbf{\ell} = \mu_0\left(
\iint_\Sigma \mathbf{J} \cdot d\mathbf{S} + \epsilon_0 \frac{d}{dt}\iint_\Sigma
\mathbf{E} \cdot d\mathbf{S} \right)$$

,relates induced magnetic field to changing electric flux and to current

These are the [Maxwell
Equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations), and are
non-linear time dependent differential equations. 

Under the best of circumstances they are fantastically hard to solve! But it's
how the real world works.

The permittivity of free space is defined as 

$$\epsilon_0 = \frac{1}{\mu_0 c^2}$$

, where $c$ is the [speed of light](https://en.wikipedia.org/wiki/Speed_of_light), and $\mu_0$ is the [vacuum permeability](https://en.wikipedia.org/wiki/Vacuum_permeability), which, in [SI units](https://en.wikipedia.org/wiki/International_System_of_Units), is now

$$\mu_0 = \frac{2 \alpha}{q^2}\frac{h}{c}$$ 

, where $\alpha$ is the [fine structure constant](https://en.wikipedia.org/wiki/Fine-structure_constant).


# Voltage 

The electric field has units voltage per meter, so the electric field is the
derivative of the voltage as a function of space.

$$ E = \frac{dV}{dx}$$


# Current 

Current has unit $A$ and charge $C$ has unit $As$, so the current is the number
of charges passing through a volume per second. 

The current density $J$ has units $A/m^2$ and is often used, since we can multiply
by the surface area of a conductor, if the current density is uniform. 

$$ I  = A \times J $$

# Drift current

Charges in an electric field will give rise to a drift current. 

We know from Newtons laws that force equals mass times acceleration 

$$ \vec{F} = m \vec{a}$$

If we assume a zero, or constant magnetic field, the force on a particle is
$\vec{F} = q\vec{E}$

The current density is then 

$$ \vec{J} = q\vec{E} \times n \times \mu $$

where $n$ is the charge density, and $\mu$ is the mobility (how easily the
charges move) and has units [$m^2/Vs$]

Assuming $E = V/m$, we could write 

$$ J = \frac{C}{m^3}\frac{V}{m}\frac{m^2}{Vs} = \frac{C}{s}m^{-2}$$

So multiplying by an area $A = B m^2$

$$ I = q n \mu B V$$

and we can see that the conductance $G = q n \mu B$, and since $G = 1/R$, where
R is the resistance, we have

$$ I = G V \Rightarrow V = RI$$

Or [Ohms law](https://en.wikipedia.org/wiki/Ohm%27s_law)


# Diffusion current

A difference in charge density will give rise to a diffusion current, and the
current density is

$$ J = -q D_n \frac{d \rho}{dx}$$

,where $D_n$ is a diffusion constant, and $\rho$ is the charge density.

# Currents in a semiconductor

Both electrons, and holes will contribute to current.

Electrons move in the conduction band, and holes move in the valence band. 

Both holes and electrons can only move if there are available quantum states. 

For example, if the valence band is completely filled (all states filled), then
there can be no current. 

To compute the total current in a semiconductor one must compute 

$$ I  = I_{n_{drift}} +I_{n_{diffusion}} + I_{p_{drift}}  + I_{p_{diffusion}}$$

where $n$ denotes electrons, and $p$ denote holes.

# Resistors 

We can make resistors with metal and silicon (a semiconductor)

In metal the dominate carrier depends on the metal, but it's usually electrons.
As such, one can often ignore the hole current.

In a semiconductor the dominant carrier depends on the Fermi level in relation
to the conduction band and valence band. If the Fermi level is close to the
valence band the dominant carrier will be holes.
If the Fermi level is close to the conduction band, the dominant carrier will be
electrons.

That's why we often talk about "majority carriers" and "minority carriers", both
are important in semiconductors.

# Capacitors 

A capacitor resists a change in voltage. 

$$ I = C \frac{dV}{dt}$$

and store energy in an electric field between two conductors with an insulator
between.

# Inductors

An inductor resist a change in current.

$$ V = L \frac{dV}{dt}$$

and store energy in the magnetic fields in a loop of a conductor. 

# Diodes 

See [Diodes](https://wulffern.github.io/aic2023/2021/07/08/Diodes.html) for a
long explanation. 

Assume we in the silicon lattice introduce a dopant, for example phosphorus with one
more electron than silicon. Four of the electrons will be in co-valent bonds
with the silicon lattice, while the last electron is loosely bound to the
phosphorus atom. We call that a donor.

A donor will shift the Fermi level towards the conduction band, and as such,
there will be more free electrons, as long as there is sufficient energy to
break the loose electron bond.

A atom with one less electron, for example Boron, can be introduced in the same
way, and is called an acceptor.

Most of the charges in a p-type (acceptors) silicon will be holes, while in
n-type it will be electrons.

The interesting thing happens when p-type and n-type are in contact. Since we've
shifted the Fermi level of the two silicon types in opposite direction there
will be an energy difference. That energy difference must be equialized, as
such, over time, the Fermi level of the two types will align, and a junction
will form, with few free charges, a depletion region. 

The conduction band and valence band will bend, and we now have a barrier for
charge transport, a built-in electric field. 

















[^1]: Although you do have to keep your symbols straight. We use "C" for Capacitance, but C can also mean Columbs. Context matters.
