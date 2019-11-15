# Differential Equations numerical assignment
Made by: Mikhail Kuskov, B18-01

## Exact solution

Given function
$$f(x,y)=y'=xy-xy^3$$
with IVP: $y(x_0)=y_0$

Solution:
1) Let's transform equation to the first order Bernoulli ODE:
   $y'-xy=-xy^3$ and we have $p(x)=-x$, $q(x)=-x$, $n=3$.
2) Let's substitute $v=y^{1-n}=y^{-2}$ and
   obtain $-\frac{v'}{2}-xv=-x$.
3) Solving complementary we obtain $v(x)=k*e^{-x^2}$ and
   by method of variation of parameter we get the final solution
   for $v(x)=c_1e^{-x^2}+1$
4) Than, substituting back $v=y^{-2}$ we get: $y^{-2}=c_1e^{-x^2}+1$,
   which is $y=\sqrt{ \frac{1}{c_1e^{-x^2}+1} }$, 
   $y=-\sqrt{ \frac{1}{c_1e^{-x^2}+1} }$
5) With given IVP: $y(0)=\sqrt{\frac{1}{2}}$, we can derive formula     for $c_1=\frac{(1-y_0^2)e^{x_0^2}}{y_0^2}$ and compute $c_1$
   for given particular case $c_1=1$



## Source code
```python
t = self.x_list(n)
y = np.full(n, self.y0)
step = self.step(n)

for i in range(1, n):
    y[i] = y[i - 1] + step * self.derivative(t[i - 1], y[i - 1])
```


## Numerical investigations
