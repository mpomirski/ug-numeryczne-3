import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
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
            plt.plot([x0, x1], [self.f(x0), self.f(x1)], color="orange")
            plt.fill_between([x0, x1], [self.f(x0), self.f(x1)],
                             alpha=0.5, color="orange")

    def simpsonMethod(self, n: np.int32) -> np.float64:
        dx: np.float64 = np.float64(self.right - self.left) / n
        result: np.float64 = np.float64(0)
        for i in range(n):
            x0: np.float64 = self.left + i * dx
            x1: np.float64 = self.left + (i + 0.5) * dx
            x2: np.float64 = self.left + (i + 1) * dx
            result: np.float64 = result + \
                (self.f(x0) + 4 * self.f(x1) + self.f(x2)) * dx / 6
        return result
    
    def plotSimpsonMethod(self, n: np.int32) -> None:
        xarr: np.ndarray[np.float64, np.dtype] = np.linspace(
            self.left, self.right, 100)
        y: np.float64 = self.f(xarr)
        plt.plot(xarr, y)
        dx: np.float64 = np.float64(self.right - self.left) / n
        plt.plot(xarr, y, color="red")
        for i in range(n):
            x0: np.float64 = self.left + i * dx
            x1: np.float64 = self.left + (i + 0.5) * dx
            x2: np.float64 = self.left + (i + 1) * dx

            x: np.ndarray[np.float64, np.dtype] = np.array([x0, x1, x2])
            y: np.ndarray[np.float64, np.dtype] = self.f(x)

            poly: np.poly1d = lagrange(x, y)
            x_new: np.ndarray[np.float64, np.dtype] = np.linspace(x0, x2, 100)
            plt.plot(x_new, poly(x_new), color="black")
        
def main() -> None:
    steps: np.int32 = np.int32(2)

    def f(x: np.float64) -> np.float64:
        return x**3+x**2+2*x-1
    integral = Integral(f, -4, +4)

    plt.figure(figsize=(10, 10))
    plt.subplot(3, 1, 1)
    print("Rectangle method:")
    print(integral.rectangleMethod(steps))
    integral.plotRectangleMethod(steps)

    plt.subplot(3, 1, 2)
    print("Trapzoid method:")
    print(integral.trapezoidMethod(steps))
    integral.plotTrapezoidMethod(steps)

    plt.subplot(3, 1, 3)
    print("Simpson method:")
    print(integral.simpsonMethod(steps))
    integral.plotSimpsonMethod(steps)
    plt.suptitle(f"Integral of $x^3+x^2+2x-1$ from -4 to 4\n{steps} steps")
    legend_lines = [Line2D([0], [0], color='blue', lw=2),
                    Line2D([0], [0], color='red', lw=2),
                    Line2D([0], [0], color='orange', lw=2),
                    Line2D([0], [0], color='black', lw=2)]
    plt.figlegend(legend_lines ,["Function", "Rectangle", "Trapezoid", "Simpson"])
    plt.show()




if __name__ == "__main__":
    main()
