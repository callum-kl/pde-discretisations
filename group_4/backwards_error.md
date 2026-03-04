$$\frac{1}{2\Delta t}(u^{n+1}_k - u^{n-1}_k)
+ \frac{a}{2\Delta x}(u_{k+1}^{n} - u_{k-1}^n)
=0
$$

Do Taylor expansions: 
$$
\frac{1}{2\Delta t}\Bigl(
u^{n}_k + \Delta t\, u_{t}
+ \frac{\Delta t^2}{2} u_{tt}
+ \frac{\Delta t^3}{3!} u_{ttt}
+ \mathcal{O}((\Delta t)^4) \\
$$
$$
- (u^{n}_k - \Delta t\, u_{t}
+ \frac{\Delta t^2}{2} u_{tt}
- \frac{\Delta t^3}{3!} u_{ttt}
+ \mathcal{O}((\Delta t)^4) )\\
\Bigr)
$$

$$ + \frac{a}{2\Delta x}\Bigl(
u^{n}_k + \Delta x\, u_{x}
+ \frac{\Delta x^2}{2} u_{xx}
- \frac{\Delta x^3}{3!} u_{xxx}
+ \mathcal{O}((\Delta x)^4) )\\
$$
$$
- (u^{n}_k - \Delta x\, u_{x}
+ \frac{\Delta x^2}{2} u_{xx}
- \frac{\Delta x^3}{3!} u_{xxx}
+ \mathcal{O}((\Delta x)^4) )\\
\Bigr) $$

$$
=u_t + a u_x + \frac{\Delta t^2}{6} u_{ttt}
+ \frac{a\Delta x^2}{6} u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4)
$$

Change time derivatives into space derivatives
$$
u_t = -au_x
$$

$$
u_{tt} = a^2 u_{xx}
$$

$$
u_{ttt} = -a^3 u_{xxx}
$$

$$
\to u_t + a u_x + \frac{\Delta t^2}{6} (-a^3 u_{xxx})
 + \frac{a\Delta x^2}{6} u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4) = 0
$$

Collect terms and simplify:

$$
u_t + a u_x + \frac{a}{6} (\Delta x^2-a^2 \Delta t^2) u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4) = 0
$$
then, using the CFL number $$ c = a \Delta t/ \Delta x$$
$$
u_t + a u_x + \frac{a \Delta x ^2}{6} (1-c^2) u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4) = 0
$$

giving finally

$$
u_t + a u_x = - \Big(\frac{a \Delta x ^2}{6} (1-c^2) u_{xxx}
+ \mathcal{O}((\Delta t)^4, (\Delta x)^4)\Big)
$$