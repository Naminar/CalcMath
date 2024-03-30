import matplotlib.pyplot as plt
import matplotlib 

def draw(t, x, e, ttl, path=None):

    plt.figure(figsize = (16/2,9/2), dpi = 150)
    plt.title(ttl, fontsize = 15)

    plt.xlabel("t", fontsize = 12)
    plt.xticks(fontsize =  10, ha = "center", va = "top")

    plt.ylabel("x(t)", fontsize = 12)
    plt.yticks(fontsize = 10, rotation = 30, ha = "right", va = "top")

    plt.scatter(t, x, s = 5, color = "navy")
    plt.plot(t, x, linewidth = 1, color = "black", label = f"$\\epsilon = {e}$")

    plt.legend(loc = "upper right", fontsize = 10)

    plt.grid (color = "black", linewidth = 0.45, linestyle = "dotted")
    plt.minorticks_on()
    plt.grid (which = "minor", color = "grey", linewidth = 0.25, linestyle = "dashed")

    plt.tight_layout()
    
    if path is not None:
        plt.savefig("img/"+path)
    plt.show()