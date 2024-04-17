from math import sqrt
from solve import *
import matplotlib.pyplot as plt
alpha = 1/2 + sqrt(3)/6
betta = 1/2 + sqrt(3)/6
# 3rd order for runge-kutta method.
runge_coeff = [[alpha, alpha, 0], [betta, -1/sqrt(3), alpha], [0, 1/2, 1/2]] 
eps = 0.0001

functions = [ "({x})*(2*({a}) - 0.5*({x}) - ({a})**(2)*({b})**(-2)*({y}))", # x*
              "({y})*(2*({b}) - ({a})**(-2)*({b})**(2)*({x})) - 0.5*({y})", # y*]
              f"{eps}"+"*(2 - 2*({a})*({b})**(-2)*({y}))", # a* 
              f"{eps}"+"*(2 - 2*({b})*({a})**(-2)*({x}))", # a*
]

def sum(coeff: list, lit):
    summary = ''
    ind = 1
    for co in coeff:
        summary += '+' + co + '*k' + lit + str(ind) if co != '0' else ''
        ind += 1
    return summary[1:]

# xn=0.1; yn=0.1;
t=50
h=1
x=[10]; y=[10]; a=[0.04]; b=[10]

# x_0 = [10, 10, 0.4, 10]
# eps = 0.0001

coeff1 = [ str(runge_coeff[0][ind]) for ind in range(1,3)]
coeff2 = [ str(runge_coeff[1][ind]) for ind in range(1,3)]

# print(sum(coeff, 'x'))
param = ('y','a','b')

def run_k(function, coeff):
    global param
    xn = x[-1]
    k = function.replace("{x}", f"{xn} + {h}*(" + sum(coeff, 'x') + ")")
    for key in param:
        yn = eval(key+"[-1]")
        k = k.replace('{'+ key +'}', f"{yn} + {h}*(" + sum(coeff, key) + ")") 
    return k

if __name__ == '__main__':

    for ind in range(int(t/h)):
        kx1 = run_k(functions[0], coeff1)
        kx2 = run_k(functions[0], coeff2)

        ky1 = run_k(functions[1], coeff1)
        ky2 = run_k(functions[1], coeff2)

        ka1 = run_k(functions[2], coeff1)
        ka2 = run_k(functions[2], coeff2)

        kb1 = run_k(functions[3], coeff1)
        kb2 = run_k(functions[3], coeff1)

        # solve([kx1,kx2, ky1,ky2, ka1,ka2, kb1,kb2], ['kx1','kx2', 'ky1','ky2', 'ka1','ka2', 'kb1','kb2'])
        ks = start_newton([kx1,kx2, ky1,ky2, ka1,ka2, kb1,kb2])

        x.append(x[-1] + h*(runge_coeff[2][1]*ks[0] + runge_coeff[2][2]*ks[1]))
        y.append(y[-1] + h*(runge_coeff[2][1]*ks[2] + runge_coeff[2][2]*ks[3]))
        a.append(a[-1] + h*(runge_coeff[2][1]*ks[4] + runge_coeff[2][2]*ks[5]))
        b.append(b[-1] + h*(runge_coeff[2][1]*ks[6] + runge_coeff[2][2]*ks[7]))

    print(x)

    plt.plot(range(int(t/h)),x[1::])
    plt.plot(range(int(t/h)), y[1::])
    plt.plot(range(int(t/h)), a[1::])
    plt.plot(range(int(t/h)), b[1::])

    plt.legend()
    plt.show()

# k1 = functions[0].replace("{x}", f"{xn} + {h}*(" + sum(coeff1, 'x') + ")")
# for key in param:
#     k1 = k1.replace('{'+ key +'}', f"{yn} + {h}*(" + sum(coeff1, key) + ")")
# k2 = functions[0].replace("{x}", f"{xn} + {h}*(" + sum(coeff2, 'x') + ")")
# for key in param:
#     k2 = k2.replace('{'+ key +'}', f"{yn} + {h}*(" + sum(coeff2, key) + ")")

# print(kx1, kx2)
