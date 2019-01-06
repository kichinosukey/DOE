import numpy as np
import matplotlib.pyplot as plt

from LHS import LHS

if __name__=="__main__":
    """
    - visualize process of lhs
    - what I want to visualize
        - u, u[:, j]) * (b-a), u[:, j]) * (b-a) + a
    """
    n = 2
    samples = 10

    lhs = LHS(n=n, samples=samples)
    H = lhs.sample()

    fig, ax = plt.subplots(1, 3)
    for i in range(n):
        ax[0].scatter(np.ones(samples)*(i+1), lhs.path1[i], color="k")
        ax[0].set_yticks(lhs.cut)
        ax[0].grid(color="gray", linestyle="-", linewidth=0.5)
    for i in range(n):
        ax[1].scatter(np.ones(samples)*(i+1), lhs.path2[i], color="k")
        ax[1].set_yticks(lhs.cut)
        ax[1].grid(color="gray", linestyle="-", linewidth=0.5)
    for i in range(n):
        ax[2].scatter(np.ones(samples)*(i+1), lhs.rd[:, i], color="k")
        ax[2].set_yticks(lhs.cut)
        ax[2].grid(color="gray", linestyle="-", linewidth=0.5)

    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    plt.show()

  
    ax1 = plt.subplot(1, 2, 1)
    ax1.scatter(range(samples), lhs.rd[:, 0], color="gray", label="rd")
    ax1.scatter(range(samples), H[:, 0], color="k", label="lhs")

    ax2 = plt.subplot(1, 2, 2)
    ax2.scatter(range(samples), lhs.rd[:, 1], color="gray", label="rd")
    ax2.scatter(range(samples), H[:, 1], color="k", label="lhs")
   
    plt.legend()
    plt.show()

