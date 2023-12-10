
import matplotlib.pyplot as plt
import numpy as np

years = np.array([ 1910 + ind*10 for ind in range(0, 10)])
stat = np.array([ 92228496, 106021537, 123202624, 
         132164569, 151325798, 179323175,
         203211926, 226545805, 248709873,
         281421906 ])


def summarize_degree(x, degree):
    sum = np.sum(x**degree)
    return sum


def solve_equation(coeff: dict):
    f1 = np.array([
                  [coeff['y_4'], coeff['y_3'], coeff['y_2']], 
                  [coeff['y_3'], coeff['y_2'], coeff['y_1']],
                  [coeff['y_2'], coeff['y_1'], coeff['y_0']]])
    f2 = np.array([coeff['yx_2'], coeff['yx'], coeff['y']])
    response = np.linalg.solve(f1, f2)
    print(response)
    return response

def create_system(years, stat):
    y_4 = summarize_degree(years, 4)
    y_3 = summarize_degree(years, 3)
    y_2 = summarize_degree(years, 2)
    y_1 = summarize_degree(years, 1)
    y_0 = summarize_degree(years, 0)
    yx_2 = np.sum(stat*years**2)
    yx = np.sum(stat*years)
    y = np.sum(stat)
    return {'y_4':y_4, 'y_3':y_3, 'y_2':y_2, 'y_1':y_1, 'y_0':y_0, 'yx_2':yx_2, 'yx':yx, 'y':y}

def create_plot(x, y, y1):
    plt.figure(figsize=(16/2,9/2))
    
    plt.title('Population of the USA')
    plt.xlabel('years')
    plt.ylabel('people')
    plt.plot(x, y, marker='o')
    plt.plot(x, y1)
    plt.legend(['Real', 'Approximation'])
    plt.grid()
    plt.tight_layout()
    
    plt.show()

if __name__ == '__main__':
    param = create_system(years, stat)
    response = solve_equation(param)
    response = list(response)
    approximation = [response[0]*year**2 + response[1]*year + response[2] for year in years]
    create_plot(years, stat, approximation)
    print('in 2010:{}'.format(response[0]*2010**2 + response[1]*2010 + response[2]))

    

    



