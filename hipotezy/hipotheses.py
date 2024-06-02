import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from metody_calkowania.Integral import Integral

def compare_methods(steps):
    f = lambda x: x**2  # Definicja funkcji
    integral = Integral(f, 0, 1)
    exact_value = 1 / 3

    results = {
        'rectangle': integral.rectangleMethod(steps),
        'trapezoid': integral.trapezoidMethod(steps),
        'simpson': integral.simpsonMethod(steps),
        'CSI': integral.CSIMethod(steps)
    }
    
    errors = {method: abs(result - exact_value) for method, result in results.items()}
    return errors

def main():
    steps_range = [10, 50, 100, 500, 1000, 10000]
    errors_by_steps = {step: compare_methods(step) for step in steps_range}

    # Print errors for each method and number of steps
    for step, errors in errors_by_steps.items():
        print(f"Steps: {step}")
        for method, error in errors.items():
            print(f"  {method}: Error = {error:}")
        print()

    # Verify hypotheses
    print("Verifying hypotheses:")
    print("H1: Trapezoid more accurate than Rectangle?")
    for step in steps_range:
        if errors_by_steps[step]['rectangle'] > errors_by_steps[step]['trapezoid']:
            print(f"  At {step} steps: Confirmed")
        else:
            print(f"  At {step} steps: Rejected")

    print("H2: Simpson more accurate than Trapezoid?")
    for step in steps_range:
        if errors_by_steps[step]['trapezoid'] > errors_by_steps[step]['simpson']:
            print(f"  At {step} steps: Confirmed")
        else:
            print(f"  At {step} steps: Rejected")

    print("H3: CSI more accurate than Simpson?")
    for step in steps_range:
        if errors_by_steps[step]['simpson'] > errors_by_steps[step]['CSI']:
            print(f"  At {step} steps: Confirmed")
        else:
            print(f"  At {step} steps: Rejected")

    print("H4: Errors decrease with more steps for each method?")
    for method in ['rectangle', 'trapezoid', 'simpson', 'CSI']:
        print(f"  {method}:")
        last_error = float('inf')
        for step in sorted(errors_by_steps):
            error = errors_by_steps[step][method]
            if error < last_error:
                print(f"    At {step} steps: Decreasing (Confirmed)")
                last_error = error
            else:
                print(f"    At {step} steps: Not Decreasing (Rejected)")
                break

if __name__ == "__main__":
    main()
