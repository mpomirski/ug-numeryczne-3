import numpy as np
import matplotlib.pyplot as plt
from typing import Callable
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from metody_calkowania.Integral import Integral


LEFT_BOUND: np.float64 = np.float64(-50)
RIGHT_BOUND: np.float64 = np.float64(50)

def integral_with_equal_precision(n: np.int32 = np.int32(200)) -> np.float64:
    def f(x: np.float64) -> np.float64:
        return np.float64(1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)
    integral: Integral = Integral(f, LEFT_BOUND, RIGHT_BOUND)
    result: np.float64 = integral.rectangleMethod(n)
    return result

def integral_with_varied_precision(n: np.int32 = np.int32(200), c : np.float64 = np.float64(5)) -> np.float64:
    def f(x: np.float64) -> np.float64:
        return np.float64(1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)
    integral1: Integral = Integral(f, LEFT_BOUND, -c)
    integral2: Integral = Integral(f, -c, c)
    integral3: Integral = Integral(f, c, RIGHT_BOUND)
    result: np.float64 = integral1.rectangleMethod(n//3) + integral2.rectangleMethod(n//3) + integral3.rectangleMethod(n//3)
    return result

def main() -> None:
    def c_equal_5() -> None:
        print("c = 5")
        print("5 intervals:")
        intervals: np.int32 = np.int32(5)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals):.15f}, Δ={np.abs(integral_with_varied_precision(intervals) - np.float64(1)):.15f}")
        print("10 intervals:")
        intervals: np.int32 = np.int32(10)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals):.15f}, Δ={np.abs(integral_with_varied_precision(intervals) - np.float64(1)):.15f}")
        print("20 intervals:")
        intervals: np.int32 = np.int32(20)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals):.15f}, Δ={np.abs(integral_with_varied_precision(intervals) - np.float64(1)):.15f}")
        print("50 intervals:")
        intervals: np.int32 = np.int32(50)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals):.15f}, Δ={np.abs(integral_with_varied_precision(intervals) - np.float64(1)):.15f}")
        print("100 intervals:")
        intervals: np.int32 = np.int32(100)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals):.15f}, Δ={np.abs(integral_with_varied_precision(intervals) - np.float64(1)):.15f}")
        print("200 intervals:")
        intervals: np.int32 = np.int32(200)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals):.15f}, Δ={np.abs(integral_with_varied_precision(intervals) - np.float64(1)):.15f}")
    def c_equal_3() -> None:
        print("c = 3")
        print("3 intervals:")
        intervals: np.int32 = np.int32(3)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals, np.float64(3)):.15f}, Δ={np.abs(integral_with_varied_precision(intervals, np.float64(3)) - np.float64(1)):.15f}")
        print("6 intervals:")
        intervals: np.int32 = np.int32(6)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals, np.float64(3)):.15f}, Δ={np.abs(integral_with_varied_precision(intervals, np.float64(3)) - np.float64(1)):.15f}")
        print("12 intervals:")
        intervals: np.int32 = np.int32(12)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals, np.float64(3)):.15f}, Δ={np.abs(integral_with_varied_precision(intervals, np.float64(3)) - np.float64(1)):.15f}")
        print("25 intervals:")
        intervals: np.int32 = np.int32(25)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals, np.float64(3)):.15f}, Δ={np.abs(integral_with_varied_precision(intervals, np.float64(3)) - np.float64(1)):.15f}")
        print("50 intervals:")
        intervals: np.int32 = np.int32(50)
        print(f"Equal precision:\t{integral_with_equal_precision(intervals):.15f}, Δ={np.abs(integral_with_equal_precision(intervals) - np.float64(1)):.15f}")
        print(f"Varied precision:\t{integral_with_varied_precision(intervals, np.float64(3)):.15f}, Δ={np.abs(integral_with_varied_precision(intervals, np.float64(3)) - np.float64(1)):.15f}")
    def plot_precision() -> None:
        print("Plotting precision")
        x: np.ndarray[np.int32, np.dtype] = np.linspace(1, 100, 1000, dtype=np.int32)
        y_equal: np.ndarray[np.float64, np.dtype] = np.array([np.abs(integral_with_equal_precision(np.int32(i)) - np.float64(1)) for i in x])
        y_varied: np.ndarray[np.float64, np.dtype] = np.array([np.abs(integral_with_varied_precision(np.int32(i), np.float64(3)) - np.float64(1)) for i in x])
        plt.figure(figsize=(14, 4))
        plt.yscale("log")
        plt.plot(x, y_equal, label="Equal precision")
        plt.plot(x, y_varied, label="Varied precision")
        plt.xlabel("Number of intervals")
        plt.ylabel("Difference from 1")
        plt.xticks(np.arange(0, 101, 4))
        plt.legend()
        plt.show()
    c_equal_3()
    c_equal_5()
    plot_precision()


#Punkt C
# + Hipoteza H6
if __name__ == "__main__":
    main()
