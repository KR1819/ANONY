import socket
import sys
from datetime import datetime
import pickle

def scan_ports(target, start_port, end_port):
    """
    Scans a range of TCP ports on a given target and returns the results.
    
    Args:
        target (str): The IP address or hostname to scan.
        start_port (int): The first port in the range to scan.
        end_port (int): The last port in the range to scan.
        
    Returns:
        dict: A dictionary containing the scan results.
    """
    scan_results = {
        'target': target,
        'start_time': datetime.now().isoformat(),
        'open_ports': []
    }
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: Invalid hostname. Could not resolve.")
        return None

    print("-" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Scanning started at: {scan_results['start_time']}")
    print("-" * 50)

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5) 
                
                result = sock.connect_ex((target_ip, port))
                
                if result == 0:
                    print(f"Port {port}: Open")
                    scan_results['open_ports'].append(port)
    except KeyboardInterrupt:
        print("\nScan aborted by user.")
        return None
    except Exception as e:
        print(f"An error occurred during scanning: {e}")
        return None
    
    scan_results['end_time'] = datetime.now().isoformat()
    print("-" * 50)
    print("Scanning finished.")
    
    return scan_results

def save_to_pkl(data, filename):
    """Saves data to a pickle file."""
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print(f"Scan results saved to '{filename}'.")
    except Exception as e:
        print(f"Error saving to .pkl file: {e}", file=sys.stderr)

# --- Main part of the script ---
if __name__ == "__main__":
    target_host = 'localhost' # Or an IP address like '127.0.0.1'
    start_port = 1
    end_port = 100
    
    results = scan_ports(target_host, start_port, end_port)
    
    if results:
        save_to_pkl(results, 'scan_results.pkl')

