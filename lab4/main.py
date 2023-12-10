
import matplotlib.pyplot as plt
import numpy as np
from newton import *
from spline import *

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
    # print(response)
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

def create_plot(country: str, x, y):
    plt.figure(figsize=(16/2,9/2))
    
    plt.title('Population of ' + country)
    plt.xlabel('years')
    plt.ylabel('people')
    
    plt.plot(x[0], y[0], marker='o')
    plt.plot(x[1], y[1])
    plt.plot(x[2], y[2])
    
    plt.legend(['Real', 'Approximation (least squares)', "Newton's"])
    plt.grid()
    plt.tight_layout()
    
    plt.show()

def spline_plot(country, years_ranges: list, stats_ranges: list, years, stats):
    plt.figure(figsize=(16/2,9/2))
    
    plt.title('Population of ' + country)
    plt.xlabel('years')
    plt.ylabel('people')

    plt.plot(years, stats, marker='o')
    for ind in range(len(years_ranges)):
        plt.plot(years_ranges[ind], stats_ranges[ind], linewidth=2, color='limegreen')
    
    plt.legend(['Real', 'Splines'])
    plt.grid()
    plt.tight_layout()
    
    plt.show()


if __name__ == '__main__':
    years_usa = np.array([ 1910 + ind*10 for ind in range(0, 10)])
    stat_usa  = np.array([ 92228496, 106021537, 123202624, 
                 132164569, 151325798, 179323175,
                 203211926, 226545805, 248709873,
                 281421906 ])


    def main(years, stat, country):
        param = create_system(years, stat)
        response = solve_equation(param)
        response = list(response)
        scaled_years = list(years) + [2001, 2002, 2003, 2004, 2005, 2010]
        approximation = [response[0]*year**2 + response[1]*year + response[2] for year in scaled_years]
        spline_scaling = range(years_usa[-1], 2010, 1) 

        print('By least squares in 2010: {}'.format(int(response[0]*2010**2 + response[1]*2010 + response[2])))
        print("By Newton's in 2010: {}".format(int(calculate_polynomial(years, diff_table(years, stat), 2010))))

        x = []; x.append(years); x.append(scaled_years); x.append(scaled_years)
        y = []; y.append(stat); y.append(approximation); y.append([calculate_polynomial(years, diff_table(years, stat), y) for y in scaled_years])
        
        create_plot(country, x, y)
        # create_plot(country, years, stat, scaled_years, approximation, scaled_years, [calculate_polynomial(years, diff_table(years, stat), y) for y in scaled_years])


    def spline(years, stat, country):
        b, c, d = cubic_spline(years, stat)
        b = list(b)
        c = list(c)
        d = list(d)
        years_ranges = []
        stats_ranges = []

        for ind in range(len(years) - 1):
                ls = []
                for y in range(years[ind], years[ind+1] + 1, 1):
                    ls.append(stat[ind] + b[ind]*(y - years[ind]) + c[ind]*(y - years[ind])**2 + d[ind]*(y - years[ind])**3)
                    years_ranges.append(range(years[ind], years[ind+1] + 1, 1))
                    stats_ranges.append(ls)

        scaling_point = years[-1]
        years_ranges.append(list(range(scaling_point, 2011, 1)))

        stats_ranges.append(
            [stat[-1] + b[-1]*(y - scaling_point) + c[-1]*(y - scaling_point)**2 + d[-1]*(y - scaling_point)**3 
            for y in range(scaling_point, 2011, 1)]
        )

        print('By spline in 2010: {}'.format(int(stats_ranges[-1][-1])))
        spline_plot(country, years_ranges, stats_ranges, years, stat)


    def start(years, stat, country):
        main(years, stat, country)
        spline(years, stat, country)
    
    start(years_usa, stat_usa, 'the USA')


    

    



