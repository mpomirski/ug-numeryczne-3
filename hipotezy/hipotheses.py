import sys
import os
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.path.pardir)))
from metody_calkowania.Integral import Integral
import numpy as np
import matplotlib.pyplot as plt



def compare_methods(steps):
    def f(x): return x**2
    integral = Integral(f, 0, 1)
    exact_value = 1 / 3

    return {
        'rectangle': np.abs(integral.rectangleMethod(steps) - exact_value),
        'trapezoid': np.abs(integral.trapezoidMethod(steps) - exact_value),
        'simpson': np.abs(integral.simpsonMethod(steps) - exact_value),
        'CSI': np.abs(integral.CSIMethod(steps) - exact_value)
    }


    errors = {method: abs(result - exact_value)
              for method, result in results.items()}
    return errors


def main():
    steps_range = np.linspace(10, 10000, 10, dtype=int)
    res = [compare_methods(step) for step in steps_range]
    plt.plot(steps_range, [r['rectangle'] for r in res], label='Metoda prostokątów')
    plt.plot(steps_range, [r['trapezoid'] for r in res], label='Metoda trapezów')
    plt.plot(steps_range, [r['simpson'] for r in res], label='Metoda Simpsona')
    plt.plot(steps_range, [r['CSI'] for r in res], label='Metoda CSI')
    plt.legend()
    plt.xlabel('Liczba kroków')
    plt.ylabel('Błąd bezwzględny')
    plt.savefig('hipotezy.png')


    # for step, errors in errors_by_steps.items():
    #     print(f"Steps: {step}")
    #     for method, error in errors.items():
    #         print(f"  {method}: Error = {error:}")
    #     print()

    # print("Verifying hypotheses:")
    # print("H1: Trapezoid more accurate than Rectangle?")
    # for step in steps_range:
    #     if errors_by_steps[step]['rectangle'] > errors_by_steps[step]['trapezoid']:
    #         print(f"  At {step} steps: Confirmed")
    #     else:
    #         print(f"  At {step} steps: Rejected")

    # print("H2: Simpson more accurate than Trapezoid?")
    # for step in steps_range:
    #     if errors_by_steps[step]['trapezoid'] > errors_by_steps[step]['simpson']:
    #         print(f"  At {step} steps: Confirmed")
    #     else:
    #         print(f"  At {step} steps: Rejected")

    # print("H3: CSI more accurate than Simpson?")
    # for step in steps_range:
    #     if errors_by_steps[step]['simpson'] > errors_by_steps[step]['CSI']:
    #         print(f"  At {step} steps: Confirmed")
    #     else:
    #         print(f"  At {step} steps: Rejected")

    # print("H4: Errors decrease with more steps for each method?")
    # for method in ['rectangle', 'trapezoid', 'simpson', 'CSI']:
    #     print(f"  {method}:")
    #     last_error = float('inf')
    #     for step in sorted(errors_by_steps):
    #         error = errors_by_steps[step][method]
    #         if error < last_error:
    #             print(f"    At {step} steps: Decreasing (Confirmed)")
    #             last_error = error
    #         else:
    #             print(f"    At {step} steps: Not Decreasing (Rejected)")
    #             break


if __name__ == "__main__":
    main()
