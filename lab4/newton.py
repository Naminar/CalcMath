
import matplotlib.pyplot as plt
import numpy as np

def diff_table(x_list: np.array, y_list: np.array):
    table_size = len(y_list)
    table = np.zeros([table_size, table_size])

    table[0] = y_list
    for i in range(1, table_size, 1):
        for j in range(0, table_size - i, 1):
            table[i][j] = (table[i - 1][j + 1] - table[i - 1][j]) / (x_list[j + i] - x_list[j])

    return table

def calculate_polynomial(x_list, matrix, x):
    polynomial = 0 
    for ind in range(len(x_list)):
        sum = matrix[ind][0]
        # print(sum)
        for k in range(ind):
            sum *= (x - x_list[k])
        # print(sum)
        polynomial += sum
    return polynomial