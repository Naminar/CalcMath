
import runge
from addit import *
from rosenbrock import run_rosenbrock
from nordsieck import run_nordsieck
from addit import run_control, run_rng
import matplotlib.pyplot as plt

# plt.rcParams["image.cmap"] = "plasma"
# # to change default color cycle
# plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.plasma.colors)

colors = ['#250591', '#9612A0', '#F38649', '#72CF55']

def place_fig(t, data, name:str, index):
    plt.subplot(1, 4, index)
    ind = 0
    for x in data:
        plt.title(name)
        plt.plot(t, x, color=colors[ind])
        ind += 1
    # plt.legend(['x', 'y', 'a1', 'a2'], fontsize=6)
    plt.grid()

# methods = [run_control, run_rng, run_nordsleck, run_nordsleck]#run_rosenbrock]
# names = ['control', 'runge', 'nordsleck', 'rosenbrock']
# if __name__ == '__main__':
#     plt.figure(figsize=[8, 3], dpi=200)
#     plt.suptitle('Methods to solve stiff system.')
#     for method in methods:
#         t, x = method() 
#         place_fig(t, x, names[methods.index(method)], methods.index(method)+1)
#     # plt.suptitle(title)
#     plt.tight_layout()
#     plt.show()

# plt.plot(x,y, color='#00FF00')

methods = {'Control':run_control, 'Runge-Kutta':run_rng, 'Nordsieck': run_nordsieck, 'Rosenbrock':run_rosenbrock}#run_rosenbrock]
# names = ['control', 'runge', 'nordsleck', 'rosenbrock']
if __name__ == '__main__':
    plt.figure(figsize=[10, 3], dpi=200)
    plt.suptitle('Methods to solve stiff system.')
    ind = 0
    for method in methods.items():
        t, x = method[1]() 
        ind += 1
        place_fig(t, x, method[0], ind)
    plt.gcf().legend(['x', 'y', 'a1', 'a2'], ncol=4, fontsize=9, loc="upper right", borderaxespad=1)
    # plt.suptitle(title)
    plt.tight_layout()
    plt.savefig('img/resuls.jpg')
    plt.show()







