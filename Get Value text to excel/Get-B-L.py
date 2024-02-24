import re
import pandas as pd
import os

def extract_bitrate_data(file_path):
    """Extracts bitrate data from a given file.

    Args:
        file_path (str): The path to the file.

    Returns:
        list: A list of dictionaries, where each dictionary contains 'Bitrate' as the key and the extracted bitrate value as its value.
    """

    with open(file_path, 'r') as file:
        content = file.read()

    # Extract Bitrate information for sender
    matches = re.findall(r'\[ ID\] Interval\s+Transfer\s+Bitrate\s+Retr\s*\n\[\s*5\]([^[]+)', content)

    data = []
    for match in matches:
        values = re.findall(r'\d+\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)', match)
        if values:
            data.append({'Bitrate': values[0][3]})

    return data

def extract_round_trip_data(file_path):
    """Extracts round-trip data from a given file, capturing only the 'avg' value.

    Args:
        file_path (str): The path to the file.

    Returns:
        pd.Series: A pandas Series containing only the extracted 'avg' values.
    """

    with open(file_path, 'r') as file:
        data = file.read()

    # Use regular expression to find avg round-trip values
    pattern = re.compile(r'round-trip min/avg/max = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+) ms')
    matches = pattern.findall(data)

    # Extract only the 'avg' values
    avg_values = [match[1] for match in matches]

    return pd.Series(avg_values, name='avg')  # Create a Series with the name 'avg'

def write_to_combined_excel(bitrate_data, round_trip_data, excel_file):
    """Writes the extracted bitrate and round-trip data to a combined Excel file.

    Args:
        bitrate_data (list): A list of dictionaries, where each dictionary contains 'Bitrate' as the key and the extracted bitrate value as its value.
        round_trip_data (pd.Series): A pandas Series containing the extracted round-trip 'avg' values.
        excel_file (str): The path to the output Excel file.
    """

    df_bitrate = pd.DataFrame(bitrate_data)
    df_combined = pd.concat([df_bitrate, round_trip_data.to_frame()], axis=1)  # Convert Series to DataFrame
    df_combined.to_excel(excel_file, index=False)

def process_all_files(folder_path):
    """Processes all .txt files in the specified folder, extracting bitrate and round-trip data and writing it to combined Excel files.

    Args:
        folder_path (str): The path to the folder containing the .txt files.
    """

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            excel_file = filename.replace('.txt', '.xlsx')

            extracted_bitrate_data = extract_bitrate_data(file_path)
            extracted_round_trip_data = extract_round_trip_data(file_path)

            write_to_combined_excel(extracted_bitrate_data, extracted_round_trip_data, excel_file)

            # Print only the extracted 'avg' value (optional)
            print(f"Round-trip avg extracted from {filename}: {extracted_round_trip_data.iloc[0]}")

if __name__ == "__main__":
    folder_path = os.path.dirname(__file__)  # Get current file's directory
    process_all_files(folder_path)
