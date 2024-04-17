import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

betta = 10
alpha = 100
    
def deriv(t, y):
    """ODEs for Robertson's chemical reaction system."""
    x, y = y
    xdot = 1 - x * y
    ydot = alpha * y * (x - (1+betta)/(y+betta))
    # zdot = 3.e7 * y**2
    return xdot, ydot#, zdot

# Initial and final times.
t0, tf = 0, 20
# Initial conditions: [X] = 1; [Y] = [Z] = 0.
y0 = 1, 0.001
# Solve, using a method resilient to stiff ODEs.
soln = solve_ivp(deriv, (t0, tf), y0, method='Radau')
# print(soln.nfev, 'evaluations required.')

# Plot the concentrations as a function of time. Scale [Y] by 10**YFAC
# so its variation is visible on the same axis used for [X] and [Z].
YFAC = 4
plt.plot(soln.t, soln.y[0], label='[X]')
plt.plot(soln.t, soln.y[1], label=r'$10^{}\times$[Y]'.format(YFAC))
# plt.plot(soln.t, soln.y[2], label='[Z]')
plt.xlabel('time /s')
plt.ylabel('concentration /arb. units')
plt.legend()
plt.show()
