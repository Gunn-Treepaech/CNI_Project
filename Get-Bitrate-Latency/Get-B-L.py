import re
import pandas as pd

def extract_bitrate_data(file_path):
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
    with open(file_path, 'r') as file:
        data = file.read()

    # Use regular expression to find avg round-trip values
    pattern = re.compile(r'round-trip min/avg/max = (\d+\.\d+)/(\d+\.\d+)/(\d+\.\d+) ms')
    matches = pattern.findall(data)

    # Create DataFrame from the extracted data
    df = pd.DataFrame(matches, columns=['min', 'avg', 'max'])

    return df

def write_to_combined_excel(bitrate_data, round_trip_data, excel_file):
    df_bitrate = pd.DataFrame(bitrate_data)
    df_combined = pd.concat([df_bitrate, round_trip_data], axis=1)
    df_combined.to_excel(excel_file, index=False)

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    excel_file = file_path.replace('.txt', '.xlsx')   # Use the same name but with .xlsx extension

    extracted_bitrate_data = extract_bitrate_data(file_path)
    extracted_round_trip_data = extract_round_trip_data(file_path)
    
    write_to_combined_excel(extracted_bitrate_data, extracted_round_trip_data, excel_file)

    print(f"Data has been extracted and written to {excel_file}.")
