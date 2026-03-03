We again consider the 1D Advection equation with periodic boundary conditions on $[0, 1]$:
$$\frac{\partial u}{\partial t} = -c \frac{\partial u}{\partial x}$$

Consider the time derivative of the squared $L^2$ norm $H(x) = \int^1_0 u(x)^2 dx$:

$$
\frac{d}{dt}H(x) =  \int^1_0 {2u \frac{\partial u}{\partial t}}dx =  \int^1_0 {2u \frac{\partial u}{\partial t}}dx = - 2c \int^1_0 {u \frac{\partial u}{\partial x}}dx = - c [u^2]^1_0 = 0
$$

i.e. $H$ is a conserved quantity.


Now consider the semi-discretised equation in space; i.e. a (finite dimensional) ODE in continuous time:

$$\dot{u}=-\frac{c}{2\Delta x} (u_{n+1}-u_{n-1})=Au$$

where $A$ is the circulant matrix:

```math
A=\begin{pmatrix}
0 & -\frac{c}{2} & 0 & \dots & 0& \frac{c}{2} \\
\frac{c}{2} & \ddots & \ddots & \ddots && 0 \\
0 & \ddots & \ddots & \ddots& \ddots& \vdots \\
\vdots  &\ddots &\ddots&\ddots&\ddots&0\\\
0&&\ddots&\ddots&\ddots& -\frac{c}{2} \\
-\frac{c}{2} & 0 & \dots & 0 & \frac{c}{2} & 0
\end{pmatrix}
```

Note that $A$ is skew-symmetric, i.e.  it satisfies $A^T=-A$.
We can analogously consider the square of the discrete $L^2$ norm:

$$\lVert u \rVert^2_{2}=\Delta x u^Tu$$

$$\frac{d}{dt}\lVert u \rVert^2_{2}=2u^T \dot{u}=2u^TAu=0$$

i.e. it is also a conserved quantity. In fact, the above systems are both Hamiltonian, with the conserved quantities being interpreted as energy, and the centered discretisation in space preserves this structure.

Now consider the fully discretised system in time using the leapfrog integrator. Because $A$ is skew-symmetric, this is a symplectic integrator. Symplectic integrators "approximately" conserve energy; that is, the energy oscillates about its true value without drift.

Concretely, Leapfrog integration conserves the energy of a perturbed Hamiltonian system as per backwards error analysis:

```math
\begin{aligned}
u^{n \pm 1} &= u^n \pm \Delta t \dot{u^n} + \frac{{(\Delta t)}^2}{2} \ddot{u^n} \pm \frac{{(\Delta t)}^3}{6} \dddot{u^n} + \dots \\
\frac{u^{n+1} - u^{n-1}}{2 \Delta t}  &= \dot{u^n} + \frac{{(\Delta t)}^2}{6} \dddot{u^n} + O(\Delta t^4)\\
\implies \dot{u} &= Au + \frac{{(\Delta t)}^2}{6} A^3{u} + O(\Delta t^4)
\end{aligned}
```

We now consider the steps of the Leapfrog integration explicitly; let $\mu=\frac{c\Delta t}{\Delta x}$.

```math
\begin{aligned}
u^{n+1} - u^{n-1} &= -\mu Au^n \\
(u^{n+1} + u^{n-1})^T(u^{n+1} - u^{n-1})&= -\mu(u^{n+1} + u^{n-1})^TAu^n \\
\lVert u^{n+1} \rVert ^2_{2} - \lVert u^{n-1} \rVert ^2_{2} &= - \mu(u^{n+1} + u^{n-1})^TAu^n
\end{aligned}
```

One can show that when $\mu = 1$, we have the exact preservation of the discrete 2-norm of our solution in time increments of $2 \Delta t$.
$$\lVert u^{n+1} \rVert ^2_{2} = \lVert u^{n-1} \rVert ^2_{2}$$
If the numerical scheme to determine our first step also respects this, then we have preservation of energy for all time. 

However when $\mu < 1$ we have oscillatory but bounded fluctuations in energy, and for $\mu > 1$, the CFL condition is violated and energy grows unboundedly.

The above also hints at an issue with Leapfrog integration in that it splits the grid into two independent alternating solutions that may drift apart in time. Schemes like the Asselin filter can couple them together using added artificial diffusion at the cost of violating energy conservation.
