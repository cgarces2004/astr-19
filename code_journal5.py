import math
import numpy as np

def sin_x(x):
    #Define function sin_x, which will take x and return x * sin
    return math.sin(x)

def main():
    # Generates 1000 values evenly spaced between 0 and 2pi
    x_values = np.linspace(0, 2 *math.pi, 1000)

    # Prints the table for respective x and sin(x) values
    print("x\t\t\tsin(x)")

    # For every x value, print x, calculate sin(x), and print sin(x)
    for x in x_values:
        print(f"{x:.4f}\t\t{sin_x(x):.4f}")

if __name__ == "__main__":
    main()
