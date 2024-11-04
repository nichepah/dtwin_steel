#!/usr/bin/python3.6
# Author: Aneesh PA
# Date: 30 October 2024

# Basis: Orowan Pascoe equation from Gisnburg, page 285

import numpy as np
import numpy as np
import matplotlib.pyplot as plt

def strain_rate_orowan_pascoe(N, R, h1, h2):
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
    
    # Calculate strain rate 
    strain_rate = (np.pi * N / 30) * np.sqrt(R * r / h1) * ((1 - 0.75) / (1 - r))
    return strain_rate

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
    strain_rate = strain_rate_orowan_pascoe(N, R, h1, h2)
    print(f"Calculated strain rate as per Orowan and Pascoe: {strain_rate:.4e} s^-1")

    # generate plot
    r_values = np.arange(0.1, 0.6, 0.1)
    strain_rate_normalized_list = [strain_rate_orowan_pascoe(N, R, h1, h1*(1-r)) /(np.pi*N/30 * np.sqrt(R/h1)) for r in r_values]


    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(r_values, strain_rate_normalized_list, label=r'Orowan Pascoe', color='red')
    plt.xlabel("r")
    plt.ylabel(r"Strain rate normalized")
    plt.title("Normalized Strain Rate vs. r")
    plt.legend()
    plt.grid(True)
    plt.show()


