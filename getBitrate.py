import re
import pandas as pd

def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Extract Bitrate and Retr information for sender
    matches = re.findall(r'\[ ID\] Interval\s+Transfer\s+Bitrate\s+Retr\s*\n\[\s*5\]([^[]+)', content)

    data = []
    for match in matches:
        values = re.findall(r'\d+\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)\s+([^\s]+)', match)
        if values:
            data.append({'Bitrate': values[0][3]})

    return data

def write_to_excel(data, excel_file):
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    file_path = "r1-r3-1.txt"  # Replace with your actual file path
    excel_file = "output.xlsx"   # Replace with your desired output Excel file name

    extracted_data = extract_data(file_path)
    write_to_excel(extracted_data, excel_file)

    print(f"Data has been extracted and written to {excel_file}.")
