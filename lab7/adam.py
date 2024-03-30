from runge import RungeKutta
import matplotlib.pyplot as plt
from draw import *


class Adam:
    
    h, x_0, y_0 = 0, 0, 0
    x_func = "{y}"
    y_func = "10 * (1 - ({x})**2)*({y}) - {x}" # e = 2 
    coeff = [55, -59, 37, -9]
    coeff.reverse()

    def calc_f(self, f, x, y):
        f = f.replace("{x}", str(x))
        f = f.replace("{y}", str(y))  
        return(eval(f))
    

    def fi(self, f: list, x: list, y: list):
        print(x, self.coeff)
        return sum([self.calc_f(f, x[ind], y[ind]) * self.coeff[ind] for ind in range(len(self.coeff))])


    def calc_xi(self, x: list, y: list, f: str):
        xi = x[-1] + self.h*self.fi(f, x, y)/24
        return xi


    def calc_yi(self, x: list, y: list, f: str):
        yi = y[-1] + self.h*self.fi(f, x, y)/24
        return yi


    def run(self, x_0, y_0, t: list, h):
        self.h = h
        n = int((t[1] - t[0])/h)
        xi = [x_0]
        yi = [y_0]

        kutta = RungeKutta()
        kutta.h = self.h
        # kutta.x_0 = x_0
        # kutta.y_0 = y_0
        # kutta.x_func = self.x_func
        # kutta.y_func = self.y_func

        for ind in range(3):
            xi.append(kutta.calc_xi(xi[-1], yi[-1], self.x_func))
            yi.append(kutta.calc_yi(xi[-1], yi[-1], self.y_func))

        # print(xi, yi)
        for key in range(n-3):
            x, y = xi[-4:], yi[-4:]
            print(x, y)
            xi.append(self.calc_xi(x, y, self.x_func))
            yi.append(self.calc_yi(x, y, self.y_func))

        # plt.plot([ind for ind in range(n+1)], xi, marker='o')
        # plt.tight_layout()
        # plt.gcf().set_dpi(100)
        # plt.show()

        draw([ind * self.h for ind in range(n+1)], xi, 10, ttl="Solution for Adams", path="adams.jpg")

if __name__ == "__main__":
    adam = Adam()
    adam.run(x_0=2, y_0=0, t=[0, 50], h=0.01)