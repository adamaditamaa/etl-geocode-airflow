import sys
import pathlib

root_path = pathlib.Path(__file__).parents[1] 
sys.path.append(str(root_path))

from integrations.geocode_util import get_structured_address

def transform(address_iter, api_key):
    """
    Processes records from an iterator by enriching them with geocoding coordinates via API.
    
    Args:
        address_iter (iterator): An iterator of raw data records from the reader.
        api_key (str): The API key for the geocoding service.
        
    Yields:
        dict: The updated record containing geocoding information if found.
    """
    for record in address_iter:
        partial_address = record.get('project_address')
        
        if partial_address:
            enriched_info = get_structured_address(partial_address, api_key)
            
            if enriched_info:
                record.update(enriched_info)
        
        yield record
