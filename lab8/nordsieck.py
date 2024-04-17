import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fsolve
import scipy.linalg

a = np.array([[0.25, 0.25 - np.sqrt(3.0) / 6.0],
              [0.25 + np.sqrt(3.0) / 6.0, 0.25]])
b = np.array([0.5 - np.sqrt(3.0) / 6, 0.5 + np.sqrt(3) / 6])
c = np.array([0.5, 0.5])

def Nordseik(F, x_0, t_1, t_2, N, l):

    t = np.linspace(t_1, t_2, num = N + 1, endpoint = True)
    dt = (t_2 - t_1) / N

    dim = len(x_0); k = len(l)

    x = np.empty(shape=(N + 1, dim)); x[0] = x_0
    z = np.zeros(shape=(k, dim)); z[0] = x_0
    e = np.zeros(k); e[1] = 1
    P = scipy.linalg.pascal(k, kind='upper')
    
    for n in range(N):
        Q = P @ z
        z = Q + np.outer(l, (dt * F(t[n], x[n]) - e @ Q))
        x[n + 1] = z[0]
    return t, x

#------------------------------------------------------------------
N = 250000
x_0 = [10, 10, 0.4, 10]
eps = 0.0001
t_1 = 0
t_2 = 50
l = np.array([251.0/720.0, 1.0, 11.0/12.0, 1.0/3.0, 1.0/24.0])
#------------------------------------------------------------------

def run_nordsieck():
    F = lambda t, x: np.array([ x[0]*(2*x[2]-0.5*x[0]-x[1]*(x[2]/x[3])**2),\
                                x[1]*(2*x[3]-0.5*x[1]-x[0]*(x[3]/x[2])**2),\
                                eps*(2-2*x[1]*x[2]*x[3]**(-2)),\
                                eps*(2-2*x[0]*x[3]*x[2]**(-2))])
    t, x = Nordseik(F, x_0, t_1, t_2, N, l)
    x = x.transpose()
    return (t, x)

if __name__ == '__main__':
    F = lambda t, x: np.array([ x[0]*(2*x[2]-0.5*x[0]-x[1]*(x[2]/x[3])**2),\
                                x[1]*(2*x[3]-0.5*x[1]-x[0]*(x[3]/x[2])**2),\
                                eps*(2-2*x[1]*x[2]*x[3]**(-2)),\
                                eps*(2-2*x[0]*x[3]*x[2]**(-2))])
    t, x = Nordseik(F, x_0, t_1, t_2, N, l)
    x = x.transpose()