import requests
import time

def get_structured_address(partial_address, api_key, retry_count=3, retry_delay=5):
    """
    Sends a request to the LocationIQ API to retrieve coordinates and full address details.
    
    Args:
        partial_address (str): The short address string to be searched.
        api_key (str): LocationIQ API access token.
        retry_count (int): Number of retries for network or server-side errors.
        retry_delay (int): Time to wait between retries in seconds.
        
    Returns:
        dict: A dictionary containing full_address, latitude, and longitude, 
              or None if the request fails or address is not found.
    """
    base_url = "https://us1.locationiq.com/v1/search"
    params = {
        'key': api_key,
        'q': partial_address,
        'format': 'json'
    }
    
    num_retry = 0
    while num_retry < retry_count:
        try:
            response = requests.get(base_url, params=params)
            
            if response.status_code == 404:
                print(f"Address not found: '{partial_address}'. Skipping...")
                return None
                
            response.raise_for_status()
            data = response.json()
            print(f"Geocoding result for '{partial_address}': {data}")
            if data and len(data) > 0:
                return {
                    "full_address": data[0].get("display_name"),
                    "latitude": data[0].get("lat"),
                    "longitude": data[0].get("lon")
                }
                
        except requests.exceptions.RequestException as e:
            num_retry += 1
            print(f"Error geocoding {partial_address}: {e}")
            
            if num_retry < retry_count:
                print(f"Retrying {partial_address} ({num_retry}/{retry_count}) in {retry_delay} seconds")
                time.sleep(retry_delay)
            else:
                raise Exception(f"Failed to Retry '{partial_address}' after {retry_count} trial. Error: {e}")
                
    