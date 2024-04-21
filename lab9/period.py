
from interval_gen import tridiag 
import matplotlib.pyplot as plt
import numpy as np 
import math 
import sys
import os
import matplotlib.animation as animation
from interval_gen import fast_frames as ff
colors = ['#250591', '#9612A0', '#F38649', '#72CF55']

h = 0.01
t_max = 2
tn = np.arange(0, t_max, h)

def P(x):
    return 10+np.sin(2*math.pi*x)

def f(x):
    return np.cos(2*math.pi*x)

def run_period():
    file = 'img/period/fig'
    A = np.zeros([len(tn), len(tn)])
    d = np.zeros(len(tn))
    A[0][0] = -2-P(0)*h**2
    A[0][1] = 1
    A[0][-1] = 1

    A[-1][0] = 1
    A[-1][-1] = -2-P(1-h)*h**2
    A[-1][-2] = 1

    b = -2-P(tn)*h**2
    a_i = 1
    c_i = 1
    for i in range(len(A[0])-2):
        A[i+1][i] = a_i
        A[i+1][i+1] = b[i+1]
        A[i+1][i+2] = c_i

    d = f(tn)*h**2
    y = tridiag(A, d)

    # plt.plot(tn, y)
    derivative = np.diff(y)/np.diff(tn)
    derivative = np.append(derivative, 2*derivative[-1]-derivative[-2])
    derivative2nd = np.diff(derivative)/np.diff(tn)
    derivative2nd = np.append(derivative2nd, derivative2nd[-1])
    # plt.plot(tn, derivative)
    # plt.plot(tn, derivative2nd)
    ctrl2nd = f(tn)+P(tn)*y
    # plt.plot(tn, ctrl2nd)
    # plt.show()
    # plt.savefig(file+'.jpg')

    fig = plt.figure(figsize=[12, 5], dpi=100)
    axs = fig.subplot_mosaic("ABC;ADE", gridspec_kw={'width_ratios':[2, 1, 1]})

    fig.suptitle(f'Periodic equation solving')
    axs['A'].plot(tn, y, color=colors[0])
    axs['A'].plot(tn, derivative, color=colors[1])
    axs['A'].plot(tn, derivative2nd, color=colors[2])
    axs['A'].plot(tn, ctrl2nd, color=colors[3])

    axs['B'].plot(tn, y, color=colors[0])
    axs['C'].plot(tn, derivative, color=colors[1])
    axs['D'].plot(tn, derivative2nd, color=colors[2])
    axs['E'].plot(tn, ctrl2nd, color=colors[3])
    axs['A'].legend(['y', '$y^{(1)}$', '$y^{(2)}$ - numerical', '$y^{(2)}$ - equation'], fontsize=9, loc="upper left", borderaxespad=1)

    plt.tight_layout()
    
    if not os.path.isfile(os.path.dirname(__file__)+f'/{file}'+'.jpg'):
        plt.savefig(file+'.jpg')
    plt.close('all') 

    fig = plt.figure(figsize=[12, 5], dpi=150)
    axs = fig.subplot_mosaic("ABC;ADE", gridspec_kw={'width_ratios':[2, 1, 1]})
    fig.suptitle(f'Periodic equation solving')
    plt.tight_layout()
    main_min = min(np.min(y), np.min(derivative), np.min(derivative2nd), np.min(ctrl2nd))
    main_max = max(np.max(y), np.max(derivative), np.max(derivative2nd), np.max(ctrl2nd))
    
    def update(frame):
        print(f'frame is {frame}')
        # axs['A'].clear() 

        for each in axs:
            axs[each].clear()
            axs[each].set_xlim(left=0, right=t_max)
        

        axs['A'].set_ylim(bottom=main_min, top=main_max)    
        axs['A'].plot(tn[:frame], y[:frame], color=colors[0])
        axs['A'].plot(tn[:frame], derivative[:frame], color=colors[1])
        axs['A'].plot(tn[:frame], derivative2nd[:frame], color=colors[2])
        axs['A'].plot(tn[:frame], ctrl2nd[:frame], color=colors[3])
        
        # axs['B'].clear() 
        # axs['C'].clear() 
        # axs['D'].clear() 
        # axs['E'].clear() 
        axs['B'].plot(tn[:frame], y[:frame], color=colors[0])
        axs['C'].plot(tn[:frame], derivative[:frame], color=colors[1])
        axs['D'].plot(tn[:frame], derivative2nd[:frame], color=colors[2])
        axs['E'].plot(tn[:frame], ctrl2nd[:frame], color=colors[3])
        axs['A'].legend(['y', '$y^{(1)}$', '$y^{(2)}$ - numerical', '$y^{(2)}$ - equation'], fontsize=9, loc="upper left", borderaxespad=1)
        return

    if not os.path.isfile(os.path.dirname(__file__)+f'/{file}'+'.gif'):
        ani = animation.FuncAnimation(fig=fig, func=update, frames=len(y), interval=ff(len(y)), repeat=False)
        ani.save(filename=file+'.gif', writer="pillow")

if __name__ == '__main__':
    run_period()