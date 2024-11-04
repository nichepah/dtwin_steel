#!/usr/bin/python3.6
# Author: Aneesh PA
# Date: 30 October 2024

# Basis: Gisnburg, page 285
# Combine all equations

# import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

import strain_rate_wusatowski
import strain_rate_sims
import strain_rate_ford_alexander
import strain_rate_orowan_pascoe

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
strain_rate = strain_rate_ford_alexander.strain_rate_ford_alexander(N, R, h1, h2)
print(f"Calculated strain rate as per ford alexander: {strain_rate:.4e} s^-1")

strain_rate = strain_rate_wusatowski.strain_rate_wusatowski(N, R, h1, h2)
print(f"Calculated strain rate as per wusatowski: Orowan and Pascoe: {strain_rate:.4e} s^-1")

strain_rate = strain_rate_sims.strain_rate_sims(N, R, h1, h2)
print(f"Calculated strain rate as per Sims: {strain_rate:.4e} s^-1")

strain_rate = strain_rate_orowan_pascoe.strain_rate_orowan_pascoe(N, R, h1, h2)
print(f"Calculated strain rate as per Orowan and Pascoe: {strain_rate:.4e} s^-1")

# generate plot
r_values = np.arange(0.1, 0.6, 0.1)
# generate normalized values
strain_rate_normalized_f = [strain_rate_ford_alexander.strain_rate_ford_alexander(N, R, h1, h1*(1-r)) /(np.pi*N/30 * np.sqrt(R/h1)) for r in r_values]
strain_rate_normalized_s = [strain_rate_sims.strain_rate_sims(N, R, h1, h1*(1-r)) /(np.pi*N/30 * np.sqrt(R/h1)) for r in r_values]
strain_rate_normalized_w = [strain_rate_wusatowski.strain_rate_wusatowski(N, R, h1, h1*(1-r)) /(np.pi*N/30 * np.sqrt(R/h1)) for r in r_values]
strain_rate_normalized_o = [strain_rate_orowan_pascoe.strain_rate_orowan_pascoe(N, R, h1, h1*(1-r)) /(np.pi*N/30 * np.sqrt(R/h1)) for r in r_values]


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(r_values, strain_rate_normalized_f, label=r'ford_alexander', color='violet')
plt.plot(r_values, strain_rate_normalized_s, label=r'sims', color='blue')
plt.plot(r_values, strain_rate_normalized_w, label=r'wusatowski', color='green')
plt.plot(r_values, strain_rate_normalized_o, label=r'orowan_pascoe', color='red')
plt.xlabel("r")
plt.ylabel(r"Strain rate normalized")
plt.title("Normalized Strain Rate vs. r")
plt.legend()
plt.grid(True)
plt.show()

