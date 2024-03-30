from runge import RungeKutta
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy as np
from draw import *

class BDF:
    
    h = 0
    x_func = "{y}"
    y_func = "2 * (1 - ({x})**2)*({y}) - {x}" # e = 2 

    def bdf(self, F, x_0, t_1, t_2, N):

        t = np.linspace(t_1, t_2, num = N + 1, endpoint = True)
        dt = (t_2 - t_1) / N

        dim = len(x_0[0])
        x = np.empty(shape=(N + 1, dim))
        x[:4] = x_0
        for n in range(N - 3):
            func = lambda x_4: x_4 - (48*x[n + 3] - 36*x[n + 2] + 16*x[n + 1] - 3*x[n] + 12*dt*F(t[n + 4], x_4)) / 25
            x[n + 4] = fsolve(func, x[n + 3])

        return t, x

    
    def run(self, x_0, y_0, t: list, h):
        x_0 = [x_0, 0]
        dim = len(x_0)
        n_steps=3
        x = np.empty(shape=(n_steps + 1, dim))
        x[0] = x_0
        N = 20000
        t_1 = t[0]
        t_2 = t[1]
        self.h = h
        F = lambda t, x: np.array([x[1], 2 * (1 - x[0]**2) * x[1] - x[0]])
        
        xi = [x_0[0]]
        yi = [x_0[1]]
        kutta = RungeKutta()
        kutta.h = self.h

        for ind in range(3):
            xi.append(kutta.calc_xi(xi[-1], yi[-1], self.x_func))
            yi.append(kutta.calc_yi(xi[-1], yi[-1], self.y_func))
        
        x[1] = [xi[1], self.h]
        x[2] = [xi[2], 2*self.h]
        return self.bdf(F, [x_0, x[0], x[1], x[2]], t_1, t_2, N)

if __name__ == "__main__":
    bdf = BDF()
    t, x = bdf.run(x_0=2, y_0=0, t=[0, 50], h=0.01)
    x = np.delete(x, 1, 1)

    draw(t, x, 2, ttl="Solution for BDF", path="bdf.jpg")