# type: ignore
import unittest
from CurveLengths import area_of_unit_circle, perimeter_of_ellipse
import numpy as np
from typing import Callable

class TestCurveLengths(unittest.TestCase):
    def setUp(self) -> None:
        self.n = np.int32(10000)
        self.precision = 5
    
    def testUnitCircleArea(self) -> None:
        rect, trapezoid, simpson, csi = area_of_unit_circle(self.n)
        self.assertAlmostEqual(rect, np.pi, self.precision)
        self.assertAlmostEqual(trapezoid, np.pi, self.precision)
        self.assertAlmostEqual(simpson, np.pi, self.precision)
        self.assertAlmostEqual(csi, np.pi, self.precision)

    
    def testEllipsePerimeter(self) -> None:
        a, b = np.float64(10), np.float64(10)
        rect, trapezoid, simpson, csi = perimeter_of_ellipse(a, b, self.n)
        self.assertAlmostEqual(rect, np.pi * 20)
        self.assertAlmostEqual(trapezoid, np.pi * 20)
        self.assertAlmostEqual(simpson, np.pi * 20)
        self.assertAlmostEqual(csi, np.pi * 20)

if __name__ == "__main__":
    unittest.main()