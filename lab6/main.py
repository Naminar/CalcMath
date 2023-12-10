
import matplotlib.pyplot as plt
import numpy as np

from spline import *


def calc_integral_trapezoid(x, f, scaling_factor: int = 1, points: list = []):
    sum = 0
    for ind in range((len(x) - 1)//scaling_factor):
        cur_heap = scaling_factor*ind  
        next_hep = scaling_factor*(ind +1)
        points.append((f[cur_heap] + f[next_hep])*(x[next_hep] - x[cur_heap])/2)
        sum += points[-1]
    return sum

def create_plot(xs, s, fk):
    plt.figure(figsize=(16/2,9/2))

    plt.xlabel('x')
    plt.ylabel('f(x)')
        
    for ind in range(len(xs)): 
        plt.plot(xs[ind], s[ind], color='red')
        plt.plot(xs[ind], fk[ind], color='blue')
    
    plt.legend(['spline f(x)', 'f(x) * sin(kx)'])
    plt.grid()
    plt.tight_layout()
    
    plt.gcf().set_dpi(100)
    plt.show()

if __name__ == '__main__':
    
    f = np.array([0., 0.5, 0.86603, 1.0, 0.86603])
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    k = 50
    delta = 0.0001


    def main():
        b, c, d = cubic_spline(x, f)
        S  = []; Xs = []; F  = []

        for ind in range(len(x)-1):
            candidates = list(np.arange(x[ind], x[ind+1] + delta, delta))
            Xs.append(np.array([x_0 for x_0 in candidates]))
            S.append(np.array([f[ind] + b[ind]*(x_0 - x[ind]) + c[ind]*(x_0 - x[ind])**2 + d[ind]*(x_0 - x[ind])**3 for x_0 in Xs[-1]]))
            F.append(np.sin(Xs[-1]*k)*S[-1])

        create_plot(Xs, S, F)

        integral = 0
        for ind in range(len(Xs)):
            integral += calc_integral_trapezoid(Xs[ind], F[ind]) 
        print('Integral value is: {}'.format(integral))
    
    main()