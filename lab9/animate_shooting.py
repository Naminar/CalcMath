import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  # for comparison
from scipy.optimize import fsolve   # for solve system of equations
from math import *
import sys
import os
import matplotlib.animation as animation
sys.path.append('..')#os.path.dirname(__file__) + '/../lab8/addit') #/home/namin/CalcMath/lab8
from lab8.addit import SolveRungekutta
colors = ['#250591', '#9612A0', '#F38649', '#72CF55']


def run_shooting(pi:int):
    file = f'img/shooting/{pi}.gif'
    if os.path.isfile(os.path.dirname(__file__)+f'/{file}'):
        return
    pi = pi
    def F(x, t):
        return np.array([x[1], -pi*t*cos(x[0])])

    edge=0 
    alpha=[2, 0.0]
    h = 0.1**6
    t = np.arange(0, 1, h)

    def run_control(F, x_0, t, solver=odeint): #odeint
        sol = solver(F, x_0, t)
        return(t, sol[:, 0], sol[:, 1])

    delt = h
    ind=0
    while(abs(alpha[-1]-alpha[-2])>0.1**8 or ind<10):
        x_0=np.array([0, alpha[-1]])
        t, y, _ = run_control(F, x_0, t)
        
        x_0=np.array([0, alpha[-1]+delt])
        _, y_d, _ = run_control(F, x_0, t)
        x_0=np.array([0, alpha[-1]-delt])
        _, y_dd, _ = run_control(F, x_0, t)

        alpha.append(alpha[-1] - 2*delt*(y[-1]-edge)/(y_d[-1]-y_dd[-1]))
        # alpha.append(alpha[-1] - delt*(y[-1]-edge)/(y_d[-1]-y[-1]))
        print(alpha[-1], alpha[-2])
        ind+=1

    x_0=np.array([0, alpha[-1]])
    t, y, derivative = run_control(F, x_0, t)
    derivative2nd = np.diff(derivative)/np.diff(t)
    ctrl2nd = -pi*t*np.cos(y)

    fig = plt.figure(figsize=[12, 5], dpi=300)
    axs = fig.subplot_mosaic("ABC;ADE", gridspec_kw={'width_ratios':[2, 1, 1]})
    fig.suptitle(f'$p$={pi}')
    plt.tight_layout()

    def update(frame):
        print(frame)
        fig.suptitle(f'$p$={pi}, alpha={alpha[frame+1]}')
        t = np.arange(0, 1, h)
        x_0=np.array([0, alpha[frame+1]])
        t, y, derivative = run_control(F, x_0, t)
        derivative2nd = np.diff(derivative)/np.diff(t)
        ctrl2nd = -pi*t*np.cos(y)
        axs['A'].clear() 
        axs['A'].plot(t, y, color=colors[0])
        axs['A'].plot(t, derivative, color=colors[1])
        axs['A'].plot(list(t)[:-1], derivative2nd, color=colors[2])
        axs['A'].plot(t, ctrl2nd, color=colors[3])
        
        axs['B'].clear() 
        axs['C'].clear() 
        axs['D'].clear() 
        axs['E'].clear() 
        axs['B'].plot(t, y, color=colors[0])
        axs['C'].plot(t, derivative, color=colors[1])
        axs['D'].plot(list(t)[:-1], derivative2nd, color=colors[2])
        axs['E'].plot(t, ctrl2nd, color=colors[3])
        axs['A'].legend(['y', '$y^{(1)}$', '$y^{(2)}$ - numerical', '$y^{(2)}$ - equation'], fontsize=9, loc="upper left", borderaxespad=1)
        return

    ani = animation.FuncAnimation(fig=fig, func=update, frames=ind, interval=1000, repeat=False)
    # plt.show()
    ani.save(filename=file, writer="pillow")


if __name__ == '__main__':
    pi=np.array([1, 2, 10, 50, 100, 200, 300, 1000])
    for each in pi:
        run_shooting(each)
