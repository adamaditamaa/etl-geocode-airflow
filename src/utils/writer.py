
import json
import os


def write_json(data, path):
    """
    Receives an iterator of enriched records and writes them into a single JSON file.
    
    Args:
        data (iterator): An iterator containing records enriched with geocoding data.
        path (str): The destination file path for the output.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    results = list(data)
    with open(path, 'w') as f:
        json.dump(results, f, indent=4)
