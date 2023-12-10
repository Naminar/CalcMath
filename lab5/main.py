
import matplotlib.pyplot as plt
import numpy as np

x = np.array([ind * 0.25 for ind in range(0, 9)])
f = np.array([ 1.0, 0.989616, 0.958851, 0.908852,
      0.841471, 0.759188, 0.664997, 0.562278, 0.454649 ])

def calc_integral_trapezoid(x, f, scaling_factor: int = 1, points: list = []):
    sum = 0
    for ind in range((len(x) - 1)//scaling_factor):
        cur_heap = scaling_factor*ind  
        next_hep = scaling_factor*(ind +1)
        points.append((f[cur_heap] + f[next_hep])*(x[next_hep] - x[cur_heap])/2)
        sum += points[-1]
        # print(cur_heap, next_hep)
    return sum


def calc_integral_simpson(x, f):
    sum = 0
    h = x[1] - x[0]
    for ind in range(1, (len(x) + 1)//2):
        sum += f[2*ind - 1]
    sum *= 4

    for ind in range(1, (len(x) + 1)//2 - 1):
        sum += f[2*ind]*2
    sum += f[0] + f[len(f) - 1]
    return sum*h/3

def richardson_correction(I_h, I_2h, p: int = 2):
    corr_int = I_h + (I_h - I_2h)/(2**p - 1)
    return corr_int 

_F_ = '{:.7}'

if __name__ == '__main__':
    # print(len(x))
    print(('Trapezoid method: h - '+_F_+', 2h - '+_F_+'').format(calc_integral_trapezoid(x, f), calc_integral_trapezoid(x, f, 2)))
    print('Trapezoid method with correction: '+_F_.format(richardson_correction(calc_integral_trapezoid(x, f), calc_integral_trapezoid(x, f, 2))))
    print(('Simpson\'s method = '+_F_).format(calc_integral_simpson(x, f)))

    int_step = []
    calc_integral_trapezoid(x, f, 1, int_step)
    plt.figure(figsize=(16/2,9/2))

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x, f, marker='o')
    plt.stem(x[:len(int_step)], int_step, 'g')
    plt.legend(['f(x)', '$\\frac{[f(x_{i+1}) + f(x_{i})] \cdot h}{2}$'], fontsize="17")
    plt.grid()
    plt.tight_layout()
    
    plt.gcf().set_dpi(100)
    plt.show()
