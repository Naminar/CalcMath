
from tridiagonal import tridiag
from copy import copy
import matplotlib.pyplot as plt
from numpy.linalg import norm
import numpy as np
import matplotlib.animation as animation
import os
def run_quasi(pi):
    file = f'img/quasi/{pi}.gif'
    if os.path.isfile(os.path.dirname(__file__)+f'/{file}'):
        return
    h = 0.1**5
    tn = np.arange(0, 1+h, h)
    u = np.ones((1,len(tn)))
    x = np.zeros(len(tn))
    u = np.vstack([u, x])
    pi=pi
    def f(x, tn):
        return -pi*tn*np.cos(x)
    def deriv(x, tn):
        return pi*tn*np.sin(x)
    i = 1
    while(norm(u[-1]-u[-2])>0.1**8 and i < 10**3):
        b = -2-h**2*deriv(u[i], tn)
        d = h**2*(f(u[i], tn)-deriv(u[i], tn)*u[i])
        a = np.array([0]+[1 for ind in range(len(tn)-1)]) 
        c = np.array([1 for ind in range(len(tn)-1)]+[0])
        x = tridiag(a,b,c,d)
        u = np.vstack([u, x])
        i+=1

    fig = plt.figure(figsize=[12, 5], dpi=300)
    axs = fig.subplot_mosaic("ABC;ADE", gridspec_kw={'width_ratios':[2, 1, 1]})
    fig.suptitle(f'$p$={pi}')
    plt.tight_layout()
    colors = ['#250591', '#9612A0', '#F38649', '#72CF55']

    def update(frame):
        fig.suptitle(f'$p$={pi}, inter={frame}')
        derivative = np.diff(u[frame+1])/np.diff(tn)
        derivative2nd = np.diff(derivative)/np.diff(list(tn)[:-1])
        ctrl2nd = -pi*tn*np.cos(u[frame+1])
        t = copy(tn)
        y = u[frame+1]
        axs['A'].clear() 
        axs['A'].plot(t, y, color=colors[0])
        axs['A'].plot(list(t)[:-1], derivative, color=colors[1])
        axs['A'].plot(list(t)[:-2], derivative2nd, color=colors[2])
        axs['A'].plot(t, ctrl2nd, color=colors[3])
        
        axs['B'].clear() 
        axs['C'].clear() 
        axs['D'].clear() 
        axs['E'].clear() 
        axs['B'].plot(t, y, color=colors[0])
        axs['C'].plot(list(t)[:-1], derivative, color=colors[1])
        axs['D'].plot(list(t)[:-2], derivative2nd, color=colors[2])
        axs['E'].plot(t, ctrl2nd, color=colors[3])
        axs['A'].legend(['y', '$y^{(1)}$', '$y^{(2)}$ - numerical', '$y^{(2)}$ - equation'], fontsize=9, loc="upper left", borderaxespad=1)
        return
    from interval_gen import generate_interval as gi
    ani = animation.FuncAnimation(fig=fig, func=update, frames=gi(i), interval=1000, repeat=False)
    ani.save(filename=file, writer="pillow")


if __name__ == '__main__':
    pi=np.array([1, 2, 10, 50, 100, 200, 300])
    for each in pi:
        run_quasi(each)
