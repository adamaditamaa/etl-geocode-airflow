import json
import os

def read_json(folder_path):
    """
    Reads all JSON files from a specified directory and returns a record iterator.
    
    Args:
        folder_path (str): The path to the directory containing input JSON files.
        
    Yields:
        dict: A single data record as a dictionary.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                records = data if isinstance(data, list) else [data]
                for record in records:
                    yield record
