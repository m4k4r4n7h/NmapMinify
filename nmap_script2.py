import os


def generate_nmap_command():
    print("Welcome to the Interactive Nmap Scanner Generator!")
    target_host = input("Enter the target IP address or hostname: ")
    
    print("\nSelect the type of scan")
    print("1. Basic Scan (default)")
    print("2. TCP SYN Scan")
    print("3. UDP Scan")
    print("4. OS Detection")
    print("5. Version Detection")
    print("6. Aggressive Scan")
    print("7. Adding More Flags By User")
    
    scan_type = input("\nEnter the number corresponding to the scan type (1-7): ")
    
    nmap_command = f"nmap {target_host}"
    
    if scan_type == "1":
        nmap_command = f"nmap {target_host}"
    elif scan_type == "2":
        nmap_command = f"nmap -sS {target_host}"
    elif scan_type == "3":
        nmap_command = f"nmap -sU {target_host}"
    elif scan_type == "4":
        nmap_command = f"nmap -O {target_host}"
    elif scan_type == "5":
        nmap_command = f"nmap -sV {target_host}"
    elif scan_type == "6":
        nmap_command = f"nmap -A {target_host}"
    elif scan_type == "7":
        print("\nLet's add some custom options!")
        nmap_command = f"nmap {target_host}"
        custom_options = input("Enter any custom Nmap options (e.g., '-p 80,443 -sC -T4'): ")
        nmap_command += f" {custom_options}"
    else:
        print("Invalid choice. Defaulting to Basic Scan.")
        nmap_command = f"nmap {target_host}"

    print("\nSelect any additional flags or options:")
    print("1. Scan Specific Ports")
    print("2. Use Nmap Scripts")
    print("3. Save Results to File")
    print("4. Use Aggressive Scan")
    print("5. Use Reverse DNS Resolution")
    print("6. Specify Source IP Address")
    print("7. Enable IPv6 Scanning")
    print("8. Fragment Packets")
    print("9. Set Maximum Retries")
    print("10. Specify Source Port")
    
    selected_flags = input("\nEnter the numbers corresponding to the options you'd like to include (comma separated): ").split(',')
    
    for flag in selected_flags:
        if flag.strip() == "1":
            scan_ports = input("\nDo you want to specify ports to scan? (y/n): ")
            if scan_ports.lower() == 'y':
                ports = input("Enter the ports to scan (e.g., 80,443 or 1-1000): ")
                nmap_command += f" -p {ports}"
        elif flag.strip() == "2":
            use_scripts = input("\nDo you want to use Nmap scripts for more detailed results? (y/n): ")
            if use_scripts.lower() == 'y':
                script = input("Enter the script(s) you want to run (e.g., http-enum, smb-os-discovery): ")
                nmap_command += f" --script={script}"
        elif flag.strip() == "3":
            save_to_file = input("\nDo you want to save the results to a file? (y/n): ")
            if save_to_file.lower() == 'y':
                file_name = input("Enter the file name (without extension): ")
                nmap_command += f" -oN {file_name}.txt"
        elif flag.strip() == "4":
            aggressive_scan = input("\nDo you want to use an aggressive scan? (y/n): ")
            if aggressive_scan.lower() == 'y':
                nmap_command += " -A"
        elif flag.strip() == "5":
            reverse_dns = input("\nDo you want to use reverse DNS resolution? (y/n): ")
            if reverse_dns.lower() == 'y':
                nmap_command += " -R"
        elif flag.strip() == "6":
            specify_source_ip = input("\nDo you want to specify a source IP address? (y/n): ")
            if specify_source_ip.lower() == 'y':
                ip_address = input("Enter the source IP address: ")
                nmap_command += f" -S {ip_address}"
        elif flag.strip() == "7":
            enable_ipv6 = input("\nDo you want to enable IPv6 scanning? (y/n): ")
            if enable_ipv6.lower() == 'y':
                nmap_command += " -6"
        elif flag.strip() == "8":
            fragment_packets = input("\nDo you want to fragment packets? (y/n): ")
            if fragment_packets.lower() == 'y':
                nmap_command += " -f"
        elif flag.strip() == "9":
            max_retries = input("\nDo you want to set a maximum retry count? (y/n): ")
            if max_retries.lower() == 'y':
                retries = input("Enter the number of retries: ")
                nmap_command += f" --max-retries {retries}"
        elif flag.strip() == "10":
            specify_source_port = input("\nDo you want to specify a source port for scanning? (y/n): ")
            if specify_source_port.lower() == 'y':
                port = input("Enter the source port: ")
                nmap_command += f" --source-port {port}"

    print("\nHere is your Nmap command:")
    print(nmap_command)

    execute_scan = input("\nDo you want to run the scan now? (y/n): ")
    if execute_scan.lower() == 'y':
        print("\nRunning the Nmap scan...\n")
        os.system(nmap_command)
    else:
        print("\nScan not executed. You can run the command manually later.")


generate_nmap_command()
