import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  # for comparison
from scipy.optimize import fsolve   # for solve system of equations
from math import sqrt

epsilon = 0.0001

def F(y, t):
    return np.array([y[0]*(2*y[2] - 0.5*y[0] - (y[2]**2)*(y[3]**(-2))*y[1]),
                     y[1]*(2*y[3] - 0.5*y[1] - (y[2]**(-2))*(y[3]**2)*y[0]),
                     epsilon*(2 - 2*y[2]*(y[3]**(-2))*y[1]),
                     epsilon*(2 - 2*(y[2]**(-2))*y[3]*y[0])
                     ])

y0 = np.array([10, 10, 0.4, 10])

alpha = 1/2 + sqrt(3)/6
betta = 1/2 - sqrt(3)/6

h = 0.01
t = np.arange(0, 50, h)
c = np.array([ alpha, betta])
b = np.array([1/2, 1/2])
A = np.array([[ alpha, 0],
              [-1/sqrt(3), alpha]])

assert A.shape == (len(c), len(b)) 
assert len(c) == len(b)

# Method Runge-Kutta
def SolveSystemK(F, t, y):
    s = len(c)
    m = len(y)

    def SystemEq(K):        
        K = np.reshape(K, (s, m))
        f = np.zeros(K.shape)
        for i in range(s):
            f[i] = F(y + h * np.dot(A[i], K), t + c[i] * h) - K[i]
        return np.array(f.flat)
    
    K0 = np.zeros(s * m)
    return fsolve(SystemEq, K0).reshape(s, m)
        
def SolveRungekutta(f, y0, t):
    n = len(t)
    m = len(y0)

    y = np.zeros((n, m))    
    y[0] = y0
    for i in range(n - 1):
        K = SolveSystemK(f, t[i], y[i])
        y[i + 1] = y[i] + h * np.dot(b, K)
    return y

if __name__ == '__main__':
    sol = odeint(F, y0, t)
    plt.plot(t, sol[:, 0], 'r', label=r'$y_1(t)$')
    plt.plot(t, sol[:, 1], 'g', label=r'$y_2(t)$')
    plt.plot(t, sol[:, 2], 'b', label=r'$y_3(t)$')
    plt.plot(t, sol[:, 3], 'b', label=r'$y_4(t)$')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    
    sol = SolveRungekutta(F, y0, t)
    plt.plot(t, sol[:, 0], 'r', label=r'$y_1(t)$')
    plt.plot(t, sol[:, 1], 'g', label=r'$y_2(t)$')
    plt.plot(t, sol[:, 2], 'b', label=r'$y_3(t)$')
    plt.plot(t, sol[:, 3], 'y', label=r'$y_4(t)$')

    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()


def run_control():
    sol = odeint(F, y0, t)
    return(t, [sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]])

def run_rng():
    sol = SolveRungekutta(F, y0, t)
    return(t, [sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]])

