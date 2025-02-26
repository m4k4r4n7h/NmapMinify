import os


def generate_nmap_command():
    print("Welcome to the Interactive Nmap Scanner Generator!")
    target = input("Enter the target IP address or hostname: ")
    
    print("\nSelect the type of scan")
    print("1. Basic Scan (default)")
    print("2. TCP SYN Scan")
    print("3. UDP Scan")
    print("4. OS Detection")
    print("5. Version Detection")
    print("6. Aggressive Scan")
    print("7. Adding More Flags By User")
    
    scan_type = input("\nEnter the number corresponding to the scan type (1-7): ")
    
    nmap_command = f"nmap {target}"
    
    if scan_type == "1":
        nmap_command = f"nmap {target}"
    elif scan_type == "2":
        nmap_command = f"nmap -sS {target}"
    elif scan_type == "3":
        nmap_command = f"nmap -sU {target}"
    elif scan_type == "4":
        nmap_command = f"nmap -O {target}"
    elif scan_type == "5":
        nmap_command = f"nmap -sV {target}"
    elif scan_type == "6":
        nmap_command = f"nmap -A {target}"
    elif scan_type == "7":
        print("\nLet's add some custom options!")
        nmap_command = f"nmap {target}"
        custom_options = input("Enter any custom Nmap options (e.g., '-p 80,443 -sC -T4'): ")
        nmap_command += f" {custom_options}"
    else:
        print("Invalid choice. Defaulting to Basic Scan.")
        nmap_command = f"nmap {target}"

    scan_ports = input("\nDo you want to specify ports to scan? (y/n): ")
    if scan_ports.lower() == 'y':
        ports = input("Enter the ports to scan (e.g., 80,443 or 1-1000): ")
        nmap_command += f" -p {ports}"

    scan_scripts = input("\nDo you want to use Nmap scripts for more detailed results? (y/n): ")
    if scan_scripts.lower() == 'y':
        script = input("Enter the script(s) you want to run (e.g., http-enum, smb-os-discovery): ")
        nmap_command += f" --script={script}"

    output_file = input("\nDo you want to save the results to a file? (y/n): ")
    if output_file.lower() == 'y':
        file_name = input("Enter the file name (without extension): ")
        nmap_command += f" -oN {file_name}.txt"

    aggressive_scan = input("\nDo you want to use an aggressive scan? (y/n): ")
    if aggressive_scan.lower() == 'y':
        nmap_command += " -A"

    print("\nHere is your Nmap command:")
    print(nmap_command)

    execute_scan = input("\nDo you want to run the scan now? (y/n): ")
    if execute_scan.lower() == 'y':
        print("\nRunning the Nmap scan...\n")
        os.system(nmap_command)
    else:
        print("\nScan not executed. You can run the command manually later.")


generate_nmap_command()
