import matplotlib.pyplot as plt
import numpy as np
from typing import Callable, List, Dict

# Example functions (all take x, y, z as arguments)
def func1(x, y, z):
    return x + y + z

def func2(x, y, z):
    return x * y * z

def func3(x, y, z):
    return x**2 + y**2 + z**2

FUNCTIONS = {
    'Sum': func1,
    'Product': func2,
    'Sum of Squares': func3
}

INPUT_VARS = ['x', 'y', 'z']

def get_user_choice(options: List[str], prompt: str) -> str:
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i+1}: {option}")
    idx = int(input("Enter number: ")) - 1
    return options[idx]

def get_sweep_range(var_name: str) -> np.ndarray:
    start = float(input(f"Enter start value for {var_name}: "))
    stop = float(input(f"Enter stop value for {var_name}: "))
    step = float(input(f"Enter step value for {var_name}: "))
    return np.arange(start, stop + step, step)

def get_fixed_inputs(var_to_sweep: str) -> Dict[str, float]:
    fixed = {}
    for var in INPUT_VARS:
        if var != var_to_sweep:
            fixed[var] = float(input(f"Enter value for {var}: "))
    return fixed

def main():
    print("Available functions:")
    func_names = list(FUNCTIONS.keys())
    chosen_funcs = []
    while True:
        name = get_user_choice(func_names, "Select a function to plot (or press Enter to finish):")
        if name not in chosen_funcs:
            chosen_funcs.append(name)
        if input("Add another function? (y/n): ").lower() != 'y':
            break
    var_to_sweep = get_user_choice(INPUT_VARS, "Select input variable to sweep:")
    sweep_vals = get_sweep_range(var_to_sweep)
    fixed_inputs = get_fixed_inputs(var_to_sweep)

    plt.figure()
    for name in chosen_funcs:
        func = FUNCTIONS[name]
        outputs = []
        for val in sweep_vals:
            args = {**fixed_inputs, var_to_sweep: val}
            outputs.append(func(args['x'], args['y'], args['z']))
        plt.plot(sweep_vals, outputs, label=name)
    plt.xlabel(var_to_sweep)
    plt.ylabel('Function Output')
    plt.title('Function Outputs vs. ' + var_to_sweep)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
