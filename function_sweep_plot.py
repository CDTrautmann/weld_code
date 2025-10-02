import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt
from typing import Callable, List, Dict

#list of input variables (alpha, q, k, T, T_o, d, Ro, U)

# Regime 1 functions
def heat_width_1(alpha, q, k, T, T_o, d, Ro, U):
    return np.sqrt((2*alpha*q)/(np.pi*np.e*k*U*(T-T_o)))
def Line_cooling_1(alpha, q, k, T, T_o, d, Ro, U):
    return -1*(2*np.pi*k*U*(T-T_o)**2)/(q)
def Max_temp_1(alpha, q, k, T, T_o, d, Ro, U):
    return T_o + 2*alpha*q/(np.e*np.pi*k*U*Y_c**2)
def T85_1(alpha, q, k, T, T_o, d, Ro, U):
    return (q)/(2*np.pi*k*U)*((1/(500-T_o))-(1/(800-T_o)))



# Regime 2 functions
def heat_width_2(alpha, q, k, T, T_o, d, Ro, U):
    return (1/(2*np.pi))*(q/(k*(T-T_o)))
def Line_cooling_2(alpha, q, k, T, T_o, d, Ro, U):
    return -1*(2*np.pi*k*U*(T-T_o)**2)/(q)
def Max_temp_2(alpha, q, k, T, T_o, d, Ro, U):
    return T_o + q/(2*np.pi*k*Y_c)
def T85_2(alpha, q, k, T, T_o, d, Ro, U):
    return (q)/(2*np.pi*k*U)*((1/(500-To))-(1/(800-T_o)))



# Regime 3 functions
def heat_width_3(alpha, q, k, T, T_o, d, Ro, U):
    return np.sqrt((1/(2*np.pi*np.e)))*(q*alpha)/(k*d*U*(T-T_o))
def Line_cooling_3(alpha, q, k, T, T_o, d, Ro, U):
    return -1*(2*np.pi*((k*d*U)**2)*(T-T_o)**3)/(alpha*q**2)
def Max_temp_3(alpha, q, k, T, T_o, d, Ro, U):
    return T_o+(np.sqrt(1/(2*np.pi*np.e)))*(q*alpha)/(k*d*U*y_c)
def T85_3(alpha, q, k, T, T_o, d, Ro, U):
    Ti = np.cbrt(2*(((800 - T_o)**2 - (500 - T_o)**2)/(800+500-2*T_o)))
    return (alpha*(q**2)*(800-500))/(((Ti-T_o)**3)*2*np.pi*(k*d*U)**2)



# Regime 4 functions
def heat_width_4(alpha, q, k, T, T_o, d, Ro, U):
    return alpha * q + k
def Line_cooling_4(alpha, q, k, T, T_o, d, Ro, U):
    return alpha + q * k
def Max_temp_4(alpha, q, k, T, T_o, d, Ro, U):
    return alpha**2 + q**2 - k**2
def T85_4(alpha, q, k, T, T_o, d, Ro, U):
    return (alpha - q) / (k + 2)



# Common functions for regime check
def Ryk(alpha, q, k, T, T_o, d, Ro, U):
    return q*U/(4*np.pi*k*alpha*(T-T_o))
def dstar(alpha, q, k, T, T_o, d, Ro, U):
    return U*d/(2*alpha)


FUNCTIONS_1 = {
    'Heat Width': heat_width_1,
    'Line Cooling': Line_cooling_1,
    'Max Temp': Max_temp_1,
    'T85': T85_1,
}

FUNCTIONS_2 = {
    'Heat Width': heat_width_2,
    'Line Cooling': Line_cooling_2,
    'Max Temp': Max_temp_2,
    'T85': T85_2,
}

FUNCTIONS_3 = {
    'Heat Width': heat_width_3,
    'Line Cooling': Line_cooling_3,
    'Max Temp': Max_temp_3,
    'T85': T85_3,
}

FUNCTIONS_4 = {
    'Heat Width': heat_width_4,
    'Line Cooling': Line_cooling_4,
    'Max Temp': Max_temp_4,
    'T85': T85_4,
}
INPUT_VARS = ['alpha', 'q', 'k', 'T', 'T_o', 'd', 'Ro', 'U']

# Preprocessing functions
def preprocess_inputs(alpha, q, k, T, T_o, d, Ro, U):
    # Run two of the defined functions and store their outputs
    out1 = Ryk(alpha, q, k, T, T_o, d, Ro, U)
    out2 = dstar(alpha, q, k, T, T_o, d, Ro, U)
    return out1, out2

def regime_check(Ry, Ds):
    # Dummy regime check based on input values
    if Ry > 1 and Ds > sqrt(3.14159/2)*sqrt(Ry):
        return 1
    elif Ry < 1 and Ds > -1*Ry*np.log(Ry) and Ds > Ry:
        return 2
    elif -1*Ry*np.log(Ry) > Ds > Ry:
        return 4
    else:
        return 3

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


# Use initial values for fixed inputs
def get_fixed_inputs(var_to_sweep: str, initial_inputs: dict) -> dict:
    return {var: val for var, val in initial_inputs.items() if var != var_to_sweep}


def main():
    # Get initial inputs for preprocessing
    print("Enter initial values for preprocessing:")
    initial_inputs = {}
    for var in INPUT_VARS:
        initial_inputs[var] = float(input(f"{var}: "))
    Ry, Ds = preprocess_inputs(
        initial_inputs['alpha'], initial_inputs['q'], initial_inputs['k'], initial_inputs['T'],
        initial_inputs['T_o'], initial_inputs['d'], initial_inputs['Ro'], initial_inputs['U']
    )
    regime = regime_check(Ry, Ds)
    print(f"Determined regime: {regime}")
    print(f"Ry: {Ry}, Ds: {Ds}")

    # Select function set based on regime
    if regime == 1:
        FUNCTIONS = FUNCTIONS_1
    elif regime == 2:
        FUNCTIONS = FUNCTIONS_2
    elif regime == 3:
        FUNCTIONS = FUNCTIONS_3
    elif regime == 4:
        FUNCTIONS = FUNCTIONS_4
    else:
        print("Unknown regime, defaulting to regime 1 functions.")
        FUNCTIONS = FUNCTIONS_1

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
    fixed_inputs = get_fixed_inputs(var_to_sweep, initial_inputs)

    plt.figure()
    for name in chosen_funcs:
        func = FUNCTIONS[name]
        print(f"Sweeping with function: {name} ({func.__name__})")
        outputs = []
        for val in sweep_vals:
            args = {**fixed_inputs, var_to_sweep: val}
            # Unpack arguments in the correct order
            arg_list = [args[var] for var in INPUT_VARS]
            outputs.append(func(*arg_list))
        plt.plot(sweep_vals, outputs, label=name)
    plt.xlabel(var_to_sweep)
    plt.ylabel('Function Output')
    plt.title('Function Outputs vs. ' + var_to_sweep)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
