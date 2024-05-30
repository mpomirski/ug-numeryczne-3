from typing import Callable
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from metody_calkowania.Integral import Integral
import numpy as np

def area_of_unit_circle(steps: np.int32) -> tuple[np.float64, np.float64, np.float64, np.float64]:
    f: Callable = lambda x: np.float64(np.sqrt(1 - x**2))
    integral: Integral = Integral(f, np.float64(-1), np.float64(1))
    rect: np.float64 = 2 * integral.rectangleMethod(steps)
    trapezoid: np.float64 = 2 * integral.trapezoidMethod(steps)
    simpson: np.float64 = 2 * integral.simpsonMethod(steps)
    CSI: np.float64 = 2 * integral.CSIMethod(steps)
    return rect, trapezoid, simpson, CSI

def perimeter_of_ellipse(a: np.float64, b: np.float64, steps: np.int32) -> tuple[np.float64, np.float64, np.float64, np.float64]:
    def f(theta: np.float64) -> np.float64:
        return np.sqrt(a**2 * np.sin(theta)**2 + b**2 * np.cos(theta)**2)

    integral: Integral = Integral(f, np.float64(0), np.float64(np.pi/2))

    rect: np.float64 = 4 * integral.rectangleMethod(steps)
    trapezoid: np.float64 = 4 * integral.trapezoidMethod(steps)
    simpson: np.float64 = 4 * integral.simpsonMethod(steps)
    CSI: np.float64 = 4 * integral.CSIMethod(steps)
    return rect, trapezoid, simpson, CSI

def main() -> None:
    steps: np.int32 = np.int32(10000)
    rect, trapezoid, simpson, CSI = area_of_unit_circle(steps)
    print("Area of unit circle:")
    print(f"Rectangle method delta:\t{np.abs(rect - np.pi):.10f}")
    print(f"Trapezoid method delta:\t{np.abs(trapezoid - np.pi):.10f}")
    print(f"Simpson method delta:\t{np.abs(simpson - np.pi):.10f}")
    print(f"CSI method delta:\t{np.abs(CSI - np.pi):.10f}")

    print("\nPerimeter of ellipse:")
    rect, trapezoid, simpson, CSI = perimeter_of_ellipse(np.float64(10), np.float64(10), steps)
    print(f"Rectangle method delta:\t{np.abs(rect - np.pi * 20):.15f}")
    print(f"Trapezoid method delta:\t{np.abs(trapezoid - np.pi * 20):.15f}")
    print(f"Simpson method delta:\t{np.abs(simpson - np.pi * 20):.15f}")
    print(f"CSI method delta:\t{np.abs(CSI - np.pi * 20):.15f}")

if __name__ == "__main__":
    main()