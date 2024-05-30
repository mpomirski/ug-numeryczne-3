import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.interpolate import lagrange, CubicSpline
from numpy.polynomial.polynomial import Polynomial
from typing import Callable


class Integral:
    def __init__(self, f: Callable[[np.float64], np.float64], left: np.float64, right: np.float64) -> None:
        self.f: Callable[[np.float64], np.float64] = f
        self.left: np.float64 = left
        self.right: np.float64 = right

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
        y: np.float64 = self.f(xarr) # type: ignore
        plt.plot(xarr, y)
        dx: np.float64 = np.float64(self.right - self.left) / n
        plt.plot(xarr, y, color="red")
        for i in range(n):
            x0: np.float64 = self.left + i * dx
            x1: np.float64 = self.left + (i + 0.5) * dx
            x2: np.float64 = self.left + (i + 1) * dx

            x_all: np.ndarray[np.float64, np.dtype] = np.array([x0, x1, x2])
            y_all: np.ndarray[np.float64, np.dtype] = self.f(x_all) # type: ignore

            poly: np.poly1d = lagrange(x_all, y_all)
            x_new: np.ndarray[np.float64, np.dtype] = np.linspace(x0, x2, 100)
            plt.plot(x_new, poly(x_new), color="black")

    def CSIMethod(self, n: np.int32) -> np.float64:
        # Krok 1: Podziel przedział na n równych części
        # Krok 2: Z każdej części wybierz 3 punkty (poczatek, środek, koniec) = (k0, k1, k2)
        # Krok 3: Znajdź wielomian interpolacyjny dla tych punktów
        # Krok 4: Oblicz całkę z tego wielomianu
        # Krok 5: Zsumuj wyniki

        # Krok 1
        dx: np.float64 = np.float64(self.right - self.left) / n
        result: np.float64 = np.float64(0)
        for i in range(n):
            # Krok 2
            x0: np.float64 = self.left + i * dx
            x1: np.float64 = self.left + (i + 0.5) * dx
            x2: np.float64 = self.left + (i + 1) * dx

            x_all: np.ndarray[np.float64, np.dtype] = np.array([x0, x1, x2])
            y_all: np.ndarray[np.float64, np.dtype] = self.f(x_all) # type: ignore
            # Krok 3 - interpolacja algorytmem Cubic Spline
            cs: CubicSpline = CubicSpline(x_all, y_all)
            # Krok 4
            result: np.float64 = result + cs.integrate(x0, x2) # type: ignore
        return result
    
    def plotCSIMethod(self, n: np.int32) -> None:
        xarr: np.ndarray[np.float64, np.dtype] = np.linspace(
            self.left, self.right, 100)
        y: np.float64 = self.f(xarr) # type: ignore
        dx: np.float64 = np.float64(self.right - self.left) / n
        plt.plot(xarr, y, color="red")
        for i in range(n):
            x0: np.float64 = self.left + i * dx
            x1: np.float64 = self.left + (i + 0.5) * dx
            x2: np.float64 = self.left + (i + 1) * dx

            x_all: np.ndarray[np.float64, np.dtype] = np.array([x0, x1, x2])
            y_all: np.ndarray[np.float64, np.dtype] = self.f(x_all) # type: ignore

            cs: CubicSpline = CubicSpline(x_all, y_all)
            x_new: np.ndarray[np.float64, np.dtype] = np.linspace(x0, x2, 100)
            plt.plot(x_new, cs(x_new), color="black")




        
def main() -> None:
    steps: np.int32 = np.int32(10)
    function: str = "x**2+2*x-1"

    def f(x: np.float64) -> np.float64:
        return eval(function)
    integral = Integral(f, np.float64(-4), np.float64(+4))

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    print("Rectangle method:")
    print(integral.rectangleMethod(steps))
    integral.plotRectangleMethod(steps)

    plt.subplot(2, 2, 2)
    print("Trapzoid method:")
    print(integral.trapezoidMethod(steps))
    integral.plotTrapezoidMethod(steps)

    plt.subplot(2, 2, 3)
    print("Simpson method:")
    print(integral.simpsonMethod(steps))
    integral.plotSimpsonMethod(steps)

    plt.subplot(2, 2, 4)
    print("CSI method:")
    print(integral.CSIMethod(steps))
    integral.plotCSIMethod(steps)


    plt.suptitle(f"Integral of ${function}$ from -4 to 4\nwith {steps} steps")
    legend_lines = [Line2D([0], [0], color='blue', lw=2),
                    Line2D([0], [0], color='red', lw=2),
                    Line2D([0], [0], color='orange', lw=2),
                    Line2D([0], [0], color='black', lw=2),
                    Line2D([0], [0], color='green', lw=2),]
    plt.figlegend(legend_lines ,["Function", "Rectangle", "Trapezoid", "Simpson", "CSI"])
    plt.show()




if __name__ == "__main__":
    main()
