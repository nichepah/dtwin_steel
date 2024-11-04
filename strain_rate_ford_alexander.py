#!/usr/bin/python3.6
# Author: Aneesh PA
# Date: 30 October 2024

# Basis: Ford and Alexander equation from Gisnburg, page 285

import numpy as np
import numpy as np
import matplotlib.pyplot as plt

def strain_rate_ford_alexander(N, R, h1, h2):
    """
    Calculate the strain rate in flat rolling based on roll speed, roll radius, 
    and initial and final thickness.
    
    Parameters:
        N (float): Roll speed in revolutions per minute (rpm).
        R (float): Radius of the roll in meters (m).
        h1 (float): Initial thickness of the strip in meters (m).
        h2 (float): Final thickness of the strip in meters (m).
        
    Returns:
        float: Calculated strain rate in s^-1.
    """
    # Calculate the reduction ratio
    r = (h1 - h2) / h1
    # Calculate strain rate using the formula from Ginzburg page 285
    strain_rate = (np.pi * N / 30) * np.sqrt(R / h1) * (1 + r / 4) * np.sqrt(r)
    return strain_rate

# Test parameters
# N = 50           # Roll speed in rpm
# R = 0.3          # Radius of the roll in meters (e.g., 30 cm)
# h1 = 0.05        # Initial thickness in meters (e.g., 5 cm)
# h2 = 0.03        # Final thickness in meters (e.g., 3 cm)


if __name__=="__main__":
    h1 = input("Enter h1: ")
    h2 = input("Enter h2: ")
    N = input("Enter rpm, N:")
    R = input("Enter Roll Radius, R: ")

    h1=float(h1)
    h2=float(h2)
    N=float(N)
    R=float(R)

    r = (h1 - h2) / h1
    # Calculate strain rate
    strain_rate = strain_rate_ford_alexander(N, R, h1, h2)
    print(f"Calculated strain rate as per Ford and Alexander: {strain_rate:.4e} s^-1")

    # generate plot
    # better use this
    r_values = np.arange(0.1, 0.6, 0.1)
    strain_rate_normalized_list = [strain_rate_ford_alexander(N, R, h1, h1*(1-r)) /(np.pi*N/30 * np.sqrt(R/h1)) for r in r_values]

    # Create the plot
    # r'Strain rate / $\left(\frac{\pi N}{30} \sqrt{\frac{R}{h1}}\right)$'

    plt.figure(figsize=(10, 6))
    plt.plot(r_values, strain_rate_normalized_list, label='alexander and ford', color='violet')
    plt.xlabel("r")
    plt.ylabel(r"Strain rate normalized")
    plt.title("Normalized Strain Rate vs. r")
    plt.legend()
    plt.grid(True)
    plt.show()


