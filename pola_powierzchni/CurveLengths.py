from typing import Callable
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from metody_calkowania.Integral import Integral
import numpy as np

def circumference_of_unit_circle(steps: np.int32) -> tuple[float, float, float, float]:
    f = lambda t: 1  
    integral = Integral(f, 0, 2 * np.pi)

    rect = integral.rectangleMethod(steps)
    trapezoid = integral.trapezoidMethod(steps)
    simpson = integral.simpsonMethod(steps)

    try:
        CSI = integral.CSIMethod(steps)
    except ZeroDivisionError:
        CSI = simpson

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

def sin_length(steps: np.int32) -> tuple[np.float64, np.float64, np.float64, np.float64]:
    def f(x: np.float64) -> np.float64:
        return np.sqrt(1 + np.cos(x)**2)
    
    integral: Integral = Integral(f, np.float64(0), np.float64(np.pi) * 2)
    rect: np.float64 = integral.rectangleMethod(steps)
    trapezoid: np.float64 = integral.trapezoidMethod(steps)
    simpson: np.float64 = integral.simpsonMethod(steps)
    CSI: np.float64 = integral.CSIMethod(steps)
    return rect, trapezoid, simpson, CSI

def main() -> None:
    steps: np.int32 = np.int32(10000)
    print("Circumference of unit circle using numerical integration:")
    results = circumference_of_unit_circle(steps)
    print(f"Rectangle method: {results[0]:.15f}, pi: {results[0] / 2:.15f}")
    print(f"Trapezoid method: {results[1]:.15f}, pi: {results[1] / 2:.15f}")
    print(f"Simpson method: {results[2]:.15f}, pi: {results[2] / 2:.15f}")
    print(f"CSI method: {results[3]:.15f}, pi: {results[3] / 2:.15f}")

    print("\nPerimeter of ellipse:")
    rect, trapezoid, simpson, CSI = perimeter_of_ellipse(np.float64(10), np.float64(10), steps)
    print(f"Rectangle method delta:\t{np.abs(rect - np.pi * 20):.15f}")
    print(f"Trapezoid method delta:\t{np.abs(trapezoid - np.pi * 20):.15f}")
    print(f"Simpson method delta:\t{np.abs(simpson - np.pi * 20):.15f}")
    print(f"CSI method delta:\t{np.abs(CSI - np.pi * 20):.15f}")

    print("\nLength of sin from 0 to 2pi:")
    rect, trapezoid, simpson, CSI = sin_length(steps)
    sin_length_wolfram: np.float64 = np.float64(7.6403955780554240358095241643428865838199352292945494421609933134) # From wolfram alpha
    print(f"Rectangle method delta:\t{np.abs(rect - sin_length_wolfram):.15f}")
    print(f"Trapezoid method delta:\t{np.abs(trapezoid - sin_length_wolfram):.15f}")
    print(f"Simpson method delta:\t{np.abs(simpson - sin_length_wolfram):.15f}")
    print(f"CSI method delta:\t{np.abs(CSI - sin_length_wolfram):.15f}")

if __name__ == "__main__":
    main()
