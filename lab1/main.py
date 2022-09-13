from enum import Enum

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import axisartist


class Param(Enum):
    LEFT = -100
    RIGHT = 100
    STEP = 0.01


def x(a, t):
    return a * np.sin(t)


def y(b, t):
    return b * np.cos(t)


def main():
    a, b = map(int, input().split())
    if a <= 0 or b <= 0:
        raise ValueError("a и b должны быть строго больше нуля")
    t = np.arange(
        Param.LEFT.value, Param.RIGHT.value + Param.STEP.value, Param.STEP.value
    )

    fig = plt.figure()
    ax = axisartist.Subplot(fig, 111)
    fig.add_axes(ax)

    ax.axis["bottom"].set_axisline_style("->", size=1.5)
    ax.axis["left"].set_axisline_style("->", size=1.5)
    ax.axis["top"].set_visible(False)
    ax.axis["right"].set_visible(False)
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")

    plt.plot(x(a, t), y(b, t))

    plt.show()


if __name__ == "__main__":
    main()
