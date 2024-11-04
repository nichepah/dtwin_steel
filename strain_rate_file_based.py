#!/usr/bin/python3.6
# Author: Aneesh PA
# Date: 04 November 2024

# Basis: Ginsburg, page 285
# Combine all equations

import strain_rate_wusatowski
import strain_rate_sims
import strain_rate_ford_alexander
import strain_rate_orowan_pascoe
import csv

def calculate_strain_rates(N, R, h1, h2):
    """
    Calculates strain rates
    :param N:
    :param R:
    :param h1:
    :param h2:
    :return:
    """
    strain_rate_fa = strain_rate_ford_alexander.strain_rate_ford_alexander(N, R, h1, h2)
    # print(f"Calculated strain rate as per ford alexander: {strain_rate:.4e} s^-1")
    strain_rate_w = strain_rate_wusatowski.strain_rate_wusatowski(N, R, h1, h2)
    # print(f"Calculated strain rate as per wusatowski: Orowan and Pascoe: {strain_rate:.4e} s^-1")
    strain_rate_s = strain_rate_sims.strain_rate_sims(N, R, h1, h2)
    # print(f"Calculated strain rate as per Sims: {strain_rate:.4e} s^-1")
    strain_rate_op = strain_rate_orowan_pascoe.strain_rate_orowan_pascoe(N, R, h1, h2)
    # print(f"Calculated strain rate as per Orowan and Pascoe: {strain_rate:.4e} s^-1")
    print(f"sr_fa, sr_s, sr_w, sr_op: {strain_rate_fa:.4e} {strain_rate_s:.4e} "
          f"{strain_rate_w:.4e} {strain_rate_op:.4e} s^-1")
    return strain_rate_fa, strain_rate_s, strain_rate_w, strain_rate_op


# Function to read data from input CSV and call strain rate calculations
def process_csv(input_file, output_file):
    results = []
    row_values = []
    N=R=h1=h2=0

    # Reading the input CSV file
    with open(input_file, mode='r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Read the first row and store its float value in N
        first_row = next(csv_reader)
        N = float(first_row[0])
        second_row = next(csv_reader)
        R = float(second_row[0])
        third_row = next(csv_reader)
        h1 = float(first_row[0])
        fourth_row = next(csv_reader)
        h2 = float(second_row[0])
        print(N, R, h1, h2)
        sr_fa, sr_s, sr_w, sr_op = calculate_strain_rates(N, R, h1, h2)
        # Store the results for each row
        results.append([sr_fa, sr_s, sr_w, sr_op])


    # Writing the results to the output CSV file
    with open(output_file, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write each result to a new row
        for result in results:
            csv_writer.writerow(result)


if __name__=="__main__":
    # Specify input and output file paths
    input_file = 'data/input.csv'
    output_file = 'data/output.csv'

    # Run the processing function
    process_csv(input_file, output_file)

    # generate plot
    # r_values = np.arange(0.1, 0.6, 0.1)
    # # generate normalized values
    # strain_rate_normalized_f = [strain_rate_ford_alexander.strain_rate_ford_alexander(N, R, h1, h1 * (1 - r)) / (
    #             np.pi * N / 30 * np.sqrt(R / h1)) for r in r_values]
    # strain_rate_normalized_s = [
    #     strain_rate_sims.strain_rate_sims(N, R, h1, h1 * (1 - r)) / (np.pi * N / 30 * np.sqrt(R / h1)) for r in
    #     r_values]
    # strain_rate_normalized_w = [
    #     strain_rate_wusatowski.strain_rate_wusatowski(N, R, h1, h1 * (1 - r)) / (np.pi * N / 30 * np.sqrt(R / h1)) for r
    #     in r_values]
    # strain_rate_normalized_o = [
    #     strain_rate_orowan_pascoe.strain_rate_orowan_pascoe(N, R, h1, h1 * (1 - r)) / (np.pi * N / 30 * np.sqrt(R / h1))
    #     for r in r_values]
    #
    # # Create the plot
    # plt.figure(figsize=(10, 6))
    # plt.plot(r_values, strain_rate_normalized_f, label=r'ford_alexander', color='violet')
    # plt.plot(r_values, strain_rate_normalized_s, label=r'sims', color='blue')
    # plt.plot(r_values, strain_rate_normalized_w, label=r'wusatowski', color='green')
    # plt.plot(r_values, strain_rate_normalized_o, label=r'orowan_pascoe', color='red')
    # plt.xlabel("r")
    # plt.ylabel(r"Strain rate normalized")
    # plt.title("Normalized Strain Rate vs. r")
    # plt.legend()
    # plt.grid(True)
    # plt.show()


