#!/usr/bin/python3.6
# Author: Aneesh PA
# Date: 30 October 2024

# Basis: Ginsburg, page 285
# Combine all equations

# import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

import strain_rate_wusatowski
import strain_rate_sims
import strain_rate_ford_alexander
import strain_rate_orowan_pascoe


def calculate_strain_rate(N, R, h1, h2):
    '''
    Calculates strain rate with different equations
    :return:
    '''
    r = (h1 - h2) / h1
    # Calculate strain rate
    strain_rate_f = strain_rate_ford_alexander.strain_rate_ford_alexander(N, R, h1, h2)
    strain_rate_w = strain_rate_wusatowski.strain_rate_wusatowski(N, R, h1, h2)
    strain_rate_s = strain_rate_sims.strain_rate_sims(N, R, h1, h2)
    strain_rate_o = strain_rate_orowan_pascoe.strain_rate_orowan_pascoe(N, R, h1, h2)
    return strain_rate_f, strain_rate_w, strain_rate_s, strain_rate_o


# Function to handle the submit button
def submit():
    try:
        # Retrieve inputs and convert them to float
        rpm = float(entry1.get())
        radius = float(entry2.get())
        h1 = float(entry3.get())
        h2 = float(entry4.get())

        # Process the inputs
        strain_rate_f, strain_rate_w, strain_rate_s, strain_rate_o = calculate_strain_rate(rpm, radius, h1, h2)

        # Display the result
        messagebox.showinfo("Result",
                            f"strain rate as per ford alexander: {strain_rate_f:.10f} s^-1 \n"
                            f"strain rate as per sims: {strain_rate_s:.10f} s^-1 \n"
                            f"strain rate as per wusatowski: {strain_rate_w:.10f} s^-1 \n"
                            f"strain rate as per orowan and pascoe: {strain_rate_o:.10f} s^-1 \n")
        # call function to plot graphs
        plot_graph(rpm, radius, h1, h2)

    except ValueError:
        # Handle non-numeric input
        messagebox.showerror("Error", "Please enter valid numbers.")




def plot_graph(rpm, radius, h1, h2):
    r = (h1 - h2) / h1
    r_values = np.arange(0.1, 0.6, 0.1)
    # generate normalized values
    strain_rate_normalized_f = [strain_rate_ford_alexander.strain_rate_ford_alexander(rpm, radius, h1, h1 * (1 - r)) /(np.pi*rpm/30 * np.sqrt(radius/h1)) for r in
                                r_values]
    strain_rate_normalized_s = [strain_rate_sims.strain_rate_sims(rpm, radius, h1, h1 * (1 - r)) /(np.pi*rpm/30 * np.sqrt(radius/h1)) for r in r_values]
    strain_rate_normalized_w = [strain_rate_wusatowski.strain_rate_wusatowski(rpm, radius, h1, h1 * (1 - r)) /(np.pi*rpm/30 * np.sqrt(radius/h1)) for r in r_values]
    strain_rate_normalized_o = [strain_rate_orowan_pascoe.strain_rate_orowan_pascoe(rpm, radius, h1, h1 * (1 - r)) /(np.pi*rpm/30 * np.sqrt(radius/h1)) for r in
                                r_values]

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


# Function to handle the cancel button (clear all inputs)
def cancel():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

if __name__=="__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Calculate Strain Rate")
    root.geometry("600x400")

    # Labels and entry fields for each input
    tk.Label(root, text="rpm:").grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="radius:").grid(row=1, column=0, padx=10, pady=10)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="h1:").grid(row=2, column=0, padx=10, pady=10)
    entry3 = tk.Entry(root)
    entry3.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(root, text="h2:").grid(row=3, column=0, padx=10, pady=10)
    entry4 = tk.Entry(root)
    entry4.grid(row=3, column=1, padx=10, pady=10)

    # Submit and Cancel buttons
    submit_button = tk.Button(root, text="Calculate Strain Rate", command=submit)
    submit_button.grid(row=4, column=0, pady=10)

    cancel_button = tk.Button(root, text="Cancel", command=cancel)
    cancel_button.grid(row=4, column=1, pady=10)

    # Run the application
    root.mainloop()

