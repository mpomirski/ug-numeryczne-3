import numpy as np
import matplotlib.pyplot as plt


class Integral:
    def __init__(self, f: callable, left: float, right: float):
        self.f = f
        self.left = left
        self.right = right

    
    def calculate(self, x: float) -> float:
        return self.f(x)
    
    def __repr__(self) -> str:
        return f"Integral({self.f} from {self.left} to {self.right})"
    
    def plot(self) -> None:
        x = np.linspace(self.left, self.right, 100)
        y = self.f(x)
        plt.plot(x, y)
        plt.show()

    def rectangleMethod(self, n: int) -> float:
        dx = (self.right - self.left) / n
        result = 0
        for i in range(n):
            x = self.left + i * dx
            result += self.f(x) * dx
        return result
    
    def plotRectangleMethod(self, n: int) -> None:
        x = np.linspace(self.left, self.right, 100)
        y = self.f(x)
        plt.plot(x, y)
        dx = (self.right - self.left) / n
        for i in range(n):
            x = self.left + i * dx + dx / 2
            plt.plot(x, self.f(x), 'o', color="red")
            plt.bar(x - 0.5 * dx, self.f(x), dx, alpha=0.5, color="red", edgecolor="black", align='edge')
        plt.show()


def main() -> None:
    def f(x):
        return np.sin(x)
    integral = Integral(f, -np.pi, +np.pi)
    print(integral.rectangleMethod(10))
    integral.plotRectangleMethod(10)

if __name__ == "__main__":
    main()