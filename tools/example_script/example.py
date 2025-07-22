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
def condition(data: Dict[str, Any]) -> bool:
    """
    Optional: Return True if the script should execute for this response
    If not defined, the script will execute for all responses
    """
    # Example: Only run for responses with status code 200
    return response.get('code') == 200

def execute(data: Dict[str, Any]):
    """
    Main execution function that runs after each request
    """
    # Example: Print interesting responses
    if response.get('chars', 0) > 1000:
        print(f"Large response detected for {request_data['candidate_char']}")
    
    # Example: Save successful guesses
    if response.get('show_response', False):
        with open('successful_guesses.txt', 'a') as f:
            f.write(f"{request_data['candidate_string']}\n")