import csv
from typing import List, Dict
# This script reads weather data from CSV files and processes it. It can also write data back to CSV files. The use of AI was involved in generating this code.

def read_weather_data(file_path: str) -> List[Dict[str, str]]:
    """
    Reads weather data from a CSV file and returns a list of dictionaries.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[Dict[str, str]]: List of weather data records.
    """
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def write_weather_data(file_path: str, data: List[Dict[str, str]]) -> None:
    """
    Writes weather data to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        data (List[Dict[str, str]]): List of weather data records.
    """
    if not data:
        return
    with open(file_path, mode='w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # Example usage
    test_data = read_weather_data("Weather Test Data.csv")
    training_data = read_weather_data("Weather Training Data.csv")
    print(f"Loaded {len(test_data)} test records and {len(training_data)} training records.")

    # Optionally write data back to a new file
    write_weather_data("Weather Test Data Copy.csv", test_data)
