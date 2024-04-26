import numpy as np
import matplotlib.pyplot as plt
from typing import Callable


class Integral:
    def __init__(self, f: Callable[[np.float64], np.float64], left: float, right: float) -> None:
        self.f: Callable[[np.float64], np.float64] = f
        self.left: float = left
        self.right: float = right

    def calculate(self, x: np.float64) -> np.float64:
        return self.f(x)

    def __repr__(self) -> str:
        return f"Integral({self.f} from {self.left} to {self.right})"

    def plot(self) -> None:
        x: np.ndarray[np.float64, np.dtype] = np.linspace(
            self.left, self.right, 100)
        y: np.ndarray[np.float64, np.dtype] = self.f(x)  # type: ignore
        plt.plot(x, y)

    def rectangleMethod(self, n: np.int32) -> np.float64:
        dx: np.float64 = np.float64(self.right - self.left) / n
        result: np.float64 = np.float64(0)
        for i in range(n):
            x: np.float64 = self.left + i * dx
            result: np.float64 = result + self.f(x) * dx
        return result

    def plotRectangleMethod(self, n: np.int32) -> None:
        xarr: np.ndarray[np.float64, np.dtype] = np.linspace(
            self.left, self.right, 100)
        y: np.float64 = self.f(xarr)  # type: ignore
        plt.plot(xarr, y)
        dx: np.float64 = np.float64(self.right - self.left) / n
        for i in range(n):
            x: np.float64 = self.left + i * dx + dx / 2
            # Dots
            # plt.plot(x, self.f(x), 'o', color="red")
            plt.bar(x - 0.5 * dx, self.f(x), dx, alpha=0.5,
                    color="red", edgecolor="black", align='edge')

    def trapezoidMethod(self, n: np.int32) -> np.float64:
        dx: np.float64 = np.float64(self.right - self.left) / n
        result: np.float64 = np.float64(0)
        for i in range(n):
            x0: np.float64 = self.left + i * dx
            x1: np.float64 = self.left + (i + 1) * dx
            result: np.float64 = result + (self.f(x0) + self.f(x1)) * dx / 2
        return result

    def plotTrapezoidMethod(self, n: np.int32) -> None:
        xarr: np.ndarray[np.float64, np.dtype] = np.linspace(
            self.left, self.right, 100)
        y: np.float64 = self.f(xarr)  # type: ignore
        plt.plot(xarr, y)
        dx: np.float64 = np.float64(self.right - self.left) / n
        for i in range(n):
            x0: np.float64 = self.left + i * dx
            x1: np.float64 = self.left + (i + 1) * dx
            plt.plot([x0, x1], [self.f(x0), self.f(x1)], color="red")
            plt.fill_between([x0, x1], [self.f(x0), self.f(x1)],
                             alpha=0.5, color="red")


def main() -> None:
    steps: np.int32 = np.int32(7)

    def f(x: np.float64) -> np.float64:
        return x
    integral = Integral(f, -4, +4)

    plt.subplot(3, 1, 1)
    print(integral.rectangleMethod(steps))
    integral.plotRectangleMethod(steps)

    plt.subplot(3, 1, 2)
    print(integral.trapezoidMethod(steps))
    integral.plotTrapezoidMethod(steps)
    plt.show()


if __name__ == "__main__":
    main()
