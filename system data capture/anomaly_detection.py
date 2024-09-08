# Import necessary libraries
# pip install pandas tqdm

import argparse
import pandas as pd
from tqdm import tqdm

# Define a function to load data from a file
def load_data(file_path):
    try:
        # Attempt to read the file into a pandas DataFrame
        return pd.read_csv(file_path)
    except Exception as e:
        # If an error occurs, print the error message
        print(f"Error loading data: {e}")

# Define a function to detect anomalies in the data
def detect_anomalies(data, thresholds):
    # Use pandas to filter the data for values exceeding the thresholds
    anomalies = data[
        (data['cpu'] > thresholds['cpu']) |  # CPU usage above threshold
        (data['mem'] > thresholds['mem']) |  # Memory usage above threshold
        (data['net'] > thresholds['net'])  # Network usage above threshold
    ]
    return anomalies

# Define the main function
def main():
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description='Anomaly Detection Script')
    
    # Add arguments for the baseline and new data files
    parser.add_argument('--baseline', help='Baseline data file', required=True)
    parser.add_argument('--new_data', help='New data file', required=True)
    
    # Add arguments for the CPU, memory, and network thresholds
    parser.add_argument('--cpu_threshold', type=float, help='CPU threshold', default=0.9)
    parser.add_argument('--mem_threshold', type=float, help='Memory threshold', default=0.8)
    parser.add_argument('--net_threshold', type=float, help='Network threshold', default=100)
    
    # Add an argument to show the progress bar
    parser.add_argument('--progress', action='store_true', help='Show progress bar')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Load the baseline and new data files
    baseline = load_data(args.baseline)
    new_data = load_data(args.new_data)
    
    # Define the thresholds dictionary
    thresholds = {
        'cpu': args.cpu_threshold,
        'mem': args.mem_threshold,
        'net': args.net_threshold
    }
    
    # If the --progress flag is set, show the progress bar
    if args.progress:
        # Iterate over the new data with a progress bar
        for i in tqdm(range(len(new_data)), desc='Processing data'):
            # Detect anomalies for each row
            detect_anomalies(new_data.iloc[i:i+1], thresholds)
    else:
        # Detect anomalies for the entire new data DataFrame
        anomalies = detect_anomalies(new_data, thresholds)
        # Print the anomalies
        print(anomalies)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
import argparse
import pandas as pd
from tqdm import tqdm

# Define a function to load data from a file
def load_data(file_path):
    try:
        # Attempt to read the file into a pandas DataFrame
        return pd.read_csv(file_path)
    except Exception as e:
        # If an error occurs, print the error message
        print(f"Error loading data: {e}")

# Define a function to detect anomalies in the data
def detect_anomalies(data, thresholds):
    # Use pandas to filter the data for values exceeding the thresholds
    anomalies = data[
        (data['cpu'] > thresholds['cpu']) |  # CPU usage above threshold
        (data['mem'] > thresholds['mem']) |  # Memory usage above threshold
        (data['net'] > thresholds['net'])  # Network usage above threshold
    ]
    return anomalies

# Define the main function
def main():
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description='Anomaly Detection Script')
    
    # Add arguments for the baseline and new data files
    parser.add_argument('--baseline', help='Baseline data file', required=True)
    parser.add_argument('--new_data', help='New data file', required=True)
    
    # Add arguments for the CPU, memory, and network thresholds
    parser.add_argument('--cpu_threshold', type=float, help='CPU threshold', default=0.9)
    parser.add_argument('--mem_threshold', type=float, help='Memory threshold', default=0.8)
    parser.add_argument('--net_threshold', type=float, help='Network threshold', default=100)
    
    # Add an argument to show the progress bar
    parser.add_argument('--progress', action='store_true', help='Show progress bar')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Load the baseline and new data files
    baseline = load_data(args.baseline)
    new_data = load_data(args.new_data)
    
    # Define the thresholds dictionary
    thresholds = {
        'cpu': args.cpu_threshold,
        'mem': args.mem_threshold,
        'net': args.net_threshold
    }
    
    # If the --progress flag is set, show the progress bar
    if args.progress:
        # Iterate over the new data with a progress bar
        for i in tqdm(range(len(new_data)), desc='Processing data'):
            # Detect anomalies for each row
            detect_anomalies(new_data.iloc[i:i+1], thresholds)
    else:
        # Detect anomalies for the entire new data DataFrame
        anomalies = detect_anomalies(new_data, thresholds)
        # Print the anomalies
        print(anomalies)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()