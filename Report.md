# Differential Equations numerical assignment
Made by: Mikhail Kuskov, B18-01

## 1) Exact solution
$$hello world$$

## 2) Implementation
```python
t = self.x_list(n)
y = np.full(n, self.y0)
step = self.step(n)

for i in range(1, n):
    y[i] = y[i - 1] + step * self.derivative(t[i - 1], y[i - 1])
```
