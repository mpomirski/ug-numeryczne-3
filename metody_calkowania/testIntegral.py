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

    def test_rectangleMethodSimple2(self) -> None:
        self.assertAlmostEqual(self.integral.rectangleMethod(self.n), self.result, self.precision)

    def test_trapezoidMethodSimple2(self) -> None:
        self.assertAlmostEqual(self.integral.trapezoidMethod(self.n), self.result, self.precision)

    def test_simpsonMethodSimple2(self) -> None:
        self.assertAlmostEqual(self.integral.simpsonMethod(self.n), self.result, self.precision)
    
    def test_CSIMethodSimple2(self) -> None:
        self.assertAlmostEqual(self.integral.CSIMethod(self.n), self.result, self.precision)

# 1000 intervals
class TestIntegralComplex(unittest.TestCase):
    def setUp(self) -> None:
        self.f: Callable[[np.float64], np.float64] = lambda x: np.float64(x**3+2*x**2+3*x+4)
        self.integral: Integral = Integral(self.f, -5, 5)
        self.n = np.int32(1000)
        self.result = np.float64(206.66666666666666)
        self.precision = 3

    def test_rectangleMethodComplex(self) -> None:
        self.assertAlmostEqual(self.integral.rectangleMethod(self.n), self.result, self.precision)

    def test_trapezoidMethodComplex(self) -> None:
        self.assertAlmostEqual(self.integral.trapezoidMethod(self.n), self.result, self.precision)

    def test_simpsonMethodComplex(self) -> None:
        self.assertAlmostEqual(self.integral.simpsonMethod(self.n), self.result, self.precision)
    
    def test_CSIMethodComplex(self) -> None:
        self.assertAlmostEqual(self.integral.CSIMethod(self.n), self.result, self.precision)

# 10000 intervals
class TestIntegralComplex2(unittest.TestCase):
    def setUp(self) -> None:
        self.f: Callable[[np.float64], np.float64] = lambda x: np.float64(x**3+2*x**2+3*x+4)
        self.integral: Integral = Integral(self.f, -5, 5)
        self.n = np.int32(10000)
        self.result = np.float64(206.66666666666666)
        self.precision = 3

    def test_rectangleMethodComplex2(self) -> None:
        self.assertAlmostEqual(self.integral.rectangleMethod(self.n), self.result, self.precision)

    def test_trapezoidMethodComplex2(self) -> None:
        self.assertAlmostEqual(self.integral.trapezoidMethod(self.n), self.result, self.precision)

    def test_simpsonMethodComplex2(self) -> None:
        self.assertAlmostEqual(self.integral.simpsonMethod(self.n), self.result, self.precision)
    
    def test_CSIMethodComplex2(self) -> None:
        self.assertAlmostEqual(self.integral.CSIMethod(self.n), self.result, self.precision)

# 1000 intervals
class TestIntegralTrig(unittest.TestCase):
    def setUp(self) -> None:
        self.f: Callable[[np.float64], np.float64] = lambda x: np.float64(np.sin(x))
        self.integral: Integral = Integral(self.f, 0, np.pi)
        self.n = np.int32(1000)
        self.result = np.float64(2)
        self.precision = 3

    def test_rectangleMethodTrig(self) -> None:
        self.assertAlmostEqual(self.integral.rectangleMethod(self.n), self.result, self.precision)

    def test_trapezoidMethodTrig(self) -> None:
        self.assertAlmostEqual(self.integral.trapezoidMethod(self.n), self.result, self.precision)

    def test_simpsonMethodTrig(self) -> None:
        self.assertAlmostEqual(self.integral.simpsonMethod(self.n), self.result, self.precision)
    
    def test_CSIMethodTrig(self) -> None:
        self.assertAlmostEqual(self.integral.CSIMethod(self.n), self.result, self.precision)

# 10000 intervals
class TestIntegralTrig2(unittest.TestCase):
    def setUp(self) -> None:
        self.f: Callable[[np.float64], np.float64] = lambda x: np.float64(np.sin(x))
        self.integral: Integral = Integral(self.f, 0, np.pi)
        self.n = np.int32(10000)
        self.result = np.float64(2)
        self.precision = 3

    def test_rectangleMethodTrig2(self) -> None:
        self.assertAlmostEqual(self.integral.rectangleMethod(self.n), self.result, self.precision)

    def test_trapezoidMethodTrig2(self) -> None:
        self.assertAlmostEqual(self.integral.trapezoidMethod(self.n), self.result, self.precision)

    def test_simpsonMethodTrig2(self) -> None:
        self.assertAlmostEqual(self.integral.simpsonMethod(self.n), self.result, self.precision)
    
    def test_CSIMethodTrig2(self) -> None:
        self.assertAlmostEqual(self.integral.CSIMethod(self.n), self.result, self.precision)

if __name__ == "__main__":
    unittest.main()