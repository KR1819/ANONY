import platform
import socket
import getpass
import psutil
import pickle # Import the pickle module
import sys

def gather_machine_details():
    """Gathers system and user information from the machine."""
    machine_info = {}

    try:
        # Get OS information
        machine_info['System'] = platform.system()
        machine_info['Release'] = platform.release()
        machine_info['Version'] = platform.version()
        machine_info['Machine'] = platform.machine()

        # Get hostname and IP address
        hostname = socket.gethostname()
        machine_info['Hostname'] = hostname
        machine_info['IP_Address'] = socket.gethostbyname(hostname)

        # Get processor information
        machine_info['Processor'] = platform.processor()

        # Get logged-in user details
        machine_info['User'] = getpass.getuser()

        # Get CPU usage and RAM information using psutil
        if 'psutil' in sys.modules:
            cpu_usage = psutil.cpu_percent(interval=1)
            total_ram = round(psutil.virtual_memory().total / (1024**3), 2)
            available_ram = round(psutil.virtual_memory().available / (1024**3), 2)
            machine_info['CPU_Usage'] = f"{cpu_usage}%"
            machine_info['Total_RAM_GB'] = total_ram
            machine_info['Available_RAM_GB'] = available_ram
        else:
            machine_info['psutil'] = "psutil library not found. Install with 'pip install psutil' for more details."
    
    except Exception as e:
        machine_info['Error'] = f"An error occurred: {e}"

    return machine_info

def print_machine_details(details):
    """Prints the gathered machine details in a readable format."""
    print("--- Machine Details ---")
    for key, value in details.items():
        print(f"{key}: {value}")
    print("-----------------------")

if __name__ == "__main__":
    details = gather_machine_details()
    print_machine_details(details)

    # --- Saving the gathered details to a .pkl file ---
    output_filename = 'machine_details.pkl'
    try:
        with open(output_filename, 'wb') as file:
            pickle.dump(details, file)
        print(f"\nSuccessfully saved machine details to '{output_filename}'.")
    except Exception as e:
        print(f"Error saving to .pkl file: {e}", file=sys.stderr)
        sys.exit(1)
