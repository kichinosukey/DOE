from pyDOE import lhs
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    strs = ["c", "m", "cm", "corr"]
    nvars = 2
    sample_size = 1000

    fig, ax = plt.subplots(nrows=2, ncols=2)

    for i, s in enumerate(strs):
        if i+1 <= 2:
            row = 0
            col = i
        elif i+1 > 2:
            row = 1
            col = i - 2
        print(row, col)
        lhd = lhs(nvars, samples=sample_size, criterion=s)
        ax[row, col].scatter(lhd[:, 0], lhd[:, 1], color="k")
        ax[row, col].set_title("criterion: "+s)

        print("*"*5 + s + "*"*5)
        print(np.corrcoef(lhd.T))

    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    plt.show()