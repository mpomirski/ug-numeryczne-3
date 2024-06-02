from typing import Callable
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from metody_calkowania.Integral import Integral

def area_of_unit_circle(steps: int) -> tuple[float, float, float, float, float]:
    f = lambda x: np.sqrt(1 - x**2)
    integral = Integral(f, -1, 1)
    rect = 2 * integral.rectangleMethod(steps)
    trapezoid = 2 * integral.trapezoidMethod(steps)
    simpson = 2 * integral.simpsonMethod(steps)
    CSI = 2 * integral.CSIMethod(steps)
    exact = np.pi
    return rect, trapezoid, simpson, CSI, exact

def area_under_parabola(steps: int) -> tuple[float, float, float, float, float]:
    f = lambda x: x**2
    integral = Integral(f, 0, 1)
    rect = integral.rectangleMethod(steps)
    trapezoid = integral.trapezoidMethod(steps)
    simpson = integral.simpsonMethod(steps)
    CSI = integral.CSIMethod(steps)
    exact = 1/3
    return rect, trapezoid, simpson, CSI, exact

def area_of_ellipse(a: float, b: float, steps: int) -> tuple[float, float, float, float, float]:
    f = lambda x: b * np.sqrt(1 - (x/a)**2)
    integral = Integral(f, -a, a)
    rect = 2 * integral.rectangleMethod(steps)
    trapezoid = 2 * integral.trapezoidMethod(steps)
    simpson = 2 * integral.simpsonMethod(steps)
    CSI = 2 * integral.CSIMethod(steps)
    exact = np.pi * a * b
    return rect, trapezoid, simpson, CSI, exact

def area_under_sine(steps: int) -> tuple[float, float, float, float, float]:
    f = lambda x: np.sin(x)
    integral = Integral(f, 0, np.pi)
    rect = integral.rectangleMethod(steps)
    trapezoid = integral.trapezoidMethod(steps)
    simpson = integral.simpsonMethod(steps)
    CSI = integral.CSIMethod(steps)
    exact = 2
    return rect, trapezoid, simpson, CSI, exact

def main():
    steps = 10000
    print("Area of unit circle:")
    results = area_of_unit_circle(steps)
    print(f"Rectangle method: {results[0]:.15f}, error: {abs(results[0]-results[4]):.15f}")
    print(f"Trapezoid method: {results[1]:.15f}, error: {abs(results[1]-results[4]):.15f}")
    print(f"Simpson method: {results[2]:.15f}, error: {abs(results[2]-results[4]):.15f}")
    print(f"CSI method: {results[3]:.15f}, error: {abs(results[3]-results[4]):.15f}")

    print("\nArea under parabola:")
    results = area_under_parabola(steps)
    print(f"Rectangle method: {results[0]:.15f}, error: {abs(results[0]-results[4]):.15f}")
    print(f"Trapezoid method: {results[1]:.15f}, error: {abs(results[1]-results[4]):.15f}")
    print(f"Simpson method: {results[2]:.15f}, error: {abs(results[2]-results[4]):.15f}")
    print(f"CSI method: {results[3]:.15f}, error: {abs(results[3]-results[4]):.15f}")

    print("\nArea of ellipse with a = 5, b = 3:")
    results = area_of_ellipse(5, 3, steps)
    print(f"Rectangle method: {results[0]:.15f}, error: {abs(results[0]-results[4]):.15f}")
    print(f"Trapezoid method: {results[1]:.15f}, error: {abs(results[1]-results[4]):.15f}")
    print(f"Simpson method: {results[2]:.15f}, error: {abs(results[2]-results[4]):.15f}")
    print(f"CSI method: {results[3]:.15f}, error: {abs(results[3]-results[4]):.15f}")

    print("\nArea under sine from 0 to pi:")
    results = area_under_sine(steps)
    print(f"Rectangle method: {results[0]:.15f}, error: {abs(results[0]-results[4]):.15f}")
    print(f"Trapezoid method: {results[1]:.15f}, error: {abs(results[1]-results[4]):.15f}")
    print(f"Simpson method: {results[2]:.15f}, error: {abs(results[2]-results[4]):.15f}")
    print(f"CSI method: {results[3]:.15f}, error: {abs(results[3]-results[4]):.15f}")

if __name__ == "__main__":
    main()
