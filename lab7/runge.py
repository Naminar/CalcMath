
import matplotlib.pyplot as plt
from draw import *

class RungeKutta:
    h, x_0, y_0 = 0, 0, 0
    x_func = "{y}"
    y_func = "10 * (1 - ({x})**2)*({y}) - {x}" # e = 2 
    
    def calc_k(self, func: str=x_func, x=x_0, y=y_0):
        func = func.replace('{x}', str(x))
        func = func.replace('{y}', str(y))
        print(eval(func))
        return eval(func)

    # class kx:
    #     k1, k2, k3, k4 = 0, 0, 0, 0
    # class ky:
    #     k1, k2, k3, k4 = 0, 0, 0, 0

    def ki(self, f: str, x, y):
        h = self.h
        k1 = self.calc_k(f, x, y)
        k2 = self.calc_k(f, x+h/2, y+h*k1/2)
        k3 = self.calc_k(f, x+h/2, y+h*k2/2)
        k4 = self.calc_k(f, x+h, y+h*k3)
        return (k1, k2, k3, k4)

    def calc_xi(self, x, y, f: str):
        k1, k2, k3, k4 = self.ki(f, x, y)
        xi = x + self.h/6 * (k1 + 2*k2 + 2*k3 + k4)
        return xi

    def calc_yi(self, x, y, f: str):
        k1, k2, k3, k4 = self.ki(f, x, y)
        yi = y + self.h/6 * (k1 + 2*k2 + 2*k3 + k4)
        return yi

    def run(self, x_0, y_0, t: list, h):
        self.h = h
        n = int((t[1] - t[0])/h)
        xi = [x_0]
        yi = [y_0]
        for key in range(n):
            x, y = xi[-1], yi[-1]
            xi.append(self.calc_xi(x, y, self.x_func))
            yi.append(self.calc_yi(x, y, self.y_func))
        print(xi)

        # plt.figure(figsize=(16/2,9/2))
        # plt.plot([ind for ind in range(n+1)], xi, marker='o')
        # plt.tight_layout()
        # plt.gcf().set_dpi(100)
        # plt.show()

        draw([ind * self.h for ind in range(n+1)], xi, 10, ttl="Solution for Runge-Kutta", path="runge.jpg")



if __name__ == "__main__":
    kutta = RungeKutta()
    kutta.run(x_0=2, y_0=0, t=[0, 50], h=0.01)