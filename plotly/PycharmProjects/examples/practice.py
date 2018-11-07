# https://plot.ly/python/network-graphs/#create-network-graph
# https://networkx.github.io/documentation/latest/tutorial.html
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def plot_a_line():
    plt.plot([2, 4, 6, 8],
             [4, 8, 12, 16])
    plt.show()


def plot_a_sine_curve():
    x = np.linspace(start=0, stop=10, num=70)
    plt.plot(x, np.sin(x), label='sine', color='green', linestyle=':', marker='d', markersize=3)
    plt.scatter(x, np.cos(x), label='cosine', color='m', linestyle='--')
    plt.legend()
    plt.xlabel('x', fontsize=15, color='green')
    plt.ylabel('sin(x)', fontsize=15, color='green')
    plt.title("Learning plots")
    plt.show()


def plot_a_figure():
    fig = plt.figure()
    ax1 = fig.add_axes([0, 0.6, 1, 0.4])
    ax2 = fig.add_axes([0, 0, 0.8, 0.4])
    x = np.linspace(start=0, stop=10, num=50)
    ax1.plot(x, np.sin(x))
    ax2.plot(x, np.cos(x))
    plt.show()


def plot_using_subplot():
    fig = plt.figure(figsize=(8, 8))  # 8 inch by 8 inch

    ax1 = fig.add_subplot(221)
    ax1.plot([2, 4, 6, 8],
             [4, 8, 12, 16])

    ax2 = fig.add_subplot(222)
    x = np.linspace(start=0, stop=10, num=50)
    ax2.plot(x, np.sin(x), color='green')

    ax3 = fig.add_subplot(223)
    ax3.plot(x, np.cos(x), linestyle=':')

    ax4 = fig.add_subplot(224)
    ax4.plot(x, np.tan(x), color='m')

    plt.show()


plot_using_subplot()
