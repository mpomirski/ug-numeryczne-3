# type: ignore
import unittest
from Integral import Integral
import numpy as np
from typing import Callable

# 1000 intervals
class TestIntegralSimple(unittest.TestCase):
    def setUp(self) -> None:
        self.f: Callable[[np.float64], np.float64] = lambda x: np.float64(x**3)
        self.integral: Integral = Integral(self.f, -1, 1)
        self.n = np.int32(1000)
        self.result = np.float64(0)
        self.precision = 3

    def test_rectangleMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.rectangleMethod(self.n), self.result, self.precision)

    def test_trapezoidMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.trapezoidMethod(self.n), self.result, self.precision)

    def test_simpsonMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.simpsonMethod(self.n), self.result, self.precision)
    
    def test_CSIMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.CSIMethod(self.n), self.result, self.precision)

# 10000 intervals
class TestIntegralSimple2(unittest.TestCase):
    def setUp(self) -> None:
        self.f: Callable[[np.float64], np.float64] = lambda x: np.float64(x**3)
        self.integral: Integral = Integral(self.f, -1, 1)
        self.n = np.int32(10000)
        self.result = np.float64(0)
        self.precision = 3

    def test_rectangleMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.rectangleMethod(self.n), self.result, self.precision)

    def test_trapezoidMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.trapezoidMethod(self.n), self.result, self.precision)

    def test_simpsonMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.simpsonMethod(self.n), self.result, self.precision)
    
    def test_CSIMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.CSIMethod(self.n), self.result, self.precision)

# 1000 intervals
class TestIntegralComplex(unittest.TestCase):
    def setUp(self) -> None:
        self.f: Callable[[np.float64], np.float64] = lambda x: np.float64(x**3+2*x**2+3*x+4)
        self.integral: Integral = Integral(self.f, -5, 5)
        self.n = np.int32(1000)
        self.result = np.float64(206.66666666666666)
        self.precision = 3

    def test_rectangleMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.rectangleMethod(self.n), self.result, self.precision)

    def test_trapezoidMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.trapezoidMethod(self.n), self.result, self.precision)

    def test_simpsonMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.simpsonMethod(self.n), self.result, self.precision)
    
    def test_CSIMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.CSIMethod(self.n), self.result, self.precision)

# 10000 intervals
class TestIntegralComplex2(unittest.TestCase):
    def setUp(self) -> None:
        self.f: Callable[[np.float64], np.float64] = lambda x: np.float64(x**3+2*x**2+3*x+4)
        self.integral: Integral = Integral(self.f, -5, 5)
        self.n = np.int32(10000)
        self.result = np.float64(206.66666666666666)
        self.precision = 3

    def test_rectangleMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.rectangleMethod(self.n), self.result, self.precision)

    def test_trapezoidMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.trapezoidMethod(self.n), self.result, self.precision)

    def test_simpsonMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.simpsonMethod(self.n), self.result, self.precision)
    
    def test_CSIMethodSimple(self) -> None:
        self.assertAlmostEqual(self.integral.CSIMethod(self.n), self.result, self.precision)

if __name__ == "__main__":
    unittest.main()