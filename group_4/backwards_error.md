```math
\frac{1}{2\Delta t}(u^{n+1}_k - u^{n-1}_k)
+ \frac{a}{2\Delta x}(u_{k+1}^{n} - u_{k-1}^n)
= 0
```

Do Taylor expansions:

```math
\frac{1}{2\Delta t}\left(
u_k^n + \Delta t\,u_t + \frac{\Delta t^2}{2}u_{tt}
+ \frac{\Delta t^3}{3!}u_{ttt} + \mathcal{O}((\Delta t)^4)
- \left(
u_k^n - \Delta t\,u_t + \frac{\Delta t^2}{2}u_{tt}
- \frac{\Delta t^3}{3!}u_{ttt} + \mathcal{O}((\Delta t)^4)
\right)
\right)
```

```math
+ \frac{a}{2\Delta x}\left(
u_k^n + \Delta x\,u_x + \frac{\Delta x^2}{2}u_{xx}
+ \frac{\Delta x^3}{3!}u_{xxx} + \mathcal{O}((\Delta x)^4)
- \left(
u_k^n - \Delta x\,u_x + \frac{\Delta x^2}{2}u_{xx}
- \frac{\Delta x^3}{3!}u_{xxx} + \mathcal{O}((\Delta x)^4)
\right)
\right)
```

```math
= u_t + a u_x
+ \frac{\Delta t^2}{6}u_{ttt}
+ \frac{a\Delta x^2}{6}u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4)
```

Change time derivatives into space derivatives:

```math
u_t = -a u_x, \qquad
u_{tt} = a^2 u_{xx}, \qquad
u_{ttt} = -a^3 u_{xxx}
```

```math
\Rightarrow
u_t + a u_x
- \frac{a^3\Delta t^2}{6}u_{xxx}
+ \frac{a\Delta x^2}{6}u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4)
= 0
```

Collect terms:

```math
u_t + a u_x
+ \frac{a}{6}(\Delta x^2 - a^2\Delta t^2)u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4)
= 0
```

Using the CFL number \(c = a\Delta t/\Delta x\):

```math
u_t + a u_x
+ \frac{a\Delta x^2}{6}(1 - c^2)u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4)
= 0
```

Finally,

```math
u_t + a u_x =
-\left(
\frac{a\Delta x^2}{6}(1 - c^2)u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4)
\right)
```
