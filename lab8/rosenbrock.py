
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fsolve
import scipy.linalg

def partial_derivative (f, t, x, h, j):

    H = np.zeros_like(x)
    H[j] = h
    return 3 * (f(t, x + H) - f(t, x - H)) / (4 * h) \
         - 3 * (f(t, x + 2*H) - f(t, x - 2*H)) / (20 * h) \
             + (f(t, x + 3*H) - f(t, x - 3*H)) / (60 * h)

# here we assume that f is an array of f_0, ..., f_n: R^{n + 1} -> R
def jacoby_matrix(f, t, x, h):

    m = len(f)
    n = len(x)
    J = np.empty(shape=(m, n))
    for i in range(m):
        for j in range(n):
            J[i, j] = partial_derivative(f[i], t, x, h, j)

    return J

def CROS_method(F, x_0, t_1, t_2, N):

    t = np.linspace(t_1, t_2, num = N + 1, endpoint = True)
    dt = (t_2 - t_1) / N

    dim = len(x_0)
    x = np.empty(shape=(N + 1, dim))
    x[0] = x_0

    for n in range(N):
        J = jacoby_matrix(F, t[n], x[n], dt)
        M = np.eye(dim) - (0.5 + 0.5 * 1j) * dt * J
        f = np.empty(dim)
        for i in range(dim):
            f[i] = F[i](t[n] + dt * 0.5, x[n])

        w = np.linalg.solve(M, f)
        x[n + 1] = x[n] + dt * w.real

    return t, x

#------------------------------------------------------------------
N = 250000
x_0 = [10, 10, 0.4, 10]
eps = 0.0001
t_1 = 0
t_2 = 50
f_1 = lambda t, x: x[0]*(2*x[2]-0.5*x[0]-x[1]*(x[2]/x[3])**2) 
f_2 = lambda t, x: x[1]*(2*x[3]-0.5*x[1]-x[0]*(x[3]/x[2])**2) 
f_3 = lambda t, x: eps*(2-2*x[1]*x[2]*x[3]**(-2))
f_4 = lambda t, x: eps*(2-2*x[0]*x[3]*x[2]**(-2))
#------------------------------------------------------------------

def run_rosenbrock():
    t, x = CROS_method([f_1, f_2, f_3, f_4], x_0, t_1, t_2, N)
    x = x.transpose()
    return (t, x)


if __name__ == '__main__':
    t, x = CROS_method([f_1, f_2, f_3, f_4], x_0, t_1, t_2, N)
    x = x.transpose()
    
    # for i in x: plt.plot(t, i)
    # plt.show()
