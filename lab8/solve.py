import sympy as sym
from sympy import sympify
import matplotlib.pyplot as plt
# k1,k2,k3,k4 = sym.symbols('k1,k2,k3,k4')
# 'k1-k2'.replace(k1, k2)
# eq1 = sym.Eq(k1-k2,5)
# eq2 = sym.Eq(sympify('k1+k2'),sympify('k1'))
# # eq2 = sym.Eq(x**2+y**2,17)
# result = sym.solve([eq1, eq2],(k1,k2))
# print(result)

def solve(left_s: list, names: list):
    kx1,kx2, ky1,ky2, ka1,ka2, kb1,kb2, = sym.symbols('kx1,kx2, ky1,ky2, ka1,ka2, kb1,kb2,')
    equations = []
    for name in names:
        equations.append(sym.Eq(sympify(left_s[names.index(name)], evaluate=True),sympify(name)))
    results = sym.solve(equations,(kx1,kx2, ky1,ky2, ka1,ka2, kb1,kb2,))
    print(results)
    # results = sym.solve(equations,(sympify(f'k{ind+1}') for ind in range(2)))

# solve(['k1+k2-3', 'k2+k1-8.1**2'])

def start_newton(ks: list):
    ki = ['kx1','kx2', 'ky1','ky2', 'ka1','ka2', 'kb1','kb2']
    eval_ks = ks[::]

    for key in ki:
        for equation in eval_ks:
            eval_ks[eval_ks.index(equation)] = equation.replace(key, '(0)')
    # return ks
    x = []
    for equation in eval_ks:
        # print(equation); print()
        x.append(eval(equation))

    for ind in range(10):
        for key in ki:
            for equation in eval_ks:
                eval_ks[eval_ks.index(equation)] = equation.replace(key, str(x[ki.index(key)]))
        y = []
        for equation in eval_ks:
            print(equation)
            y.append(eval(equation))
        x = y[::]
        eval_ks = ks[::]
        # print(x)
    return x
