# network-log-analyzer
# Reads router/switch log files and extracts errors and warnings
# Saves a clean report — replaces manual log searching

import re
from datetime import datetime

# create a sample network log file
def create_sample_log():
    with open("network.log", "w") as f:
        f.write("Jun 29 21:00:01 Router01 INFO: Interface GigabitEthernet0/0 is up\n")
        f.write("Jun 29 21:00:05 Switch01 WARNING: High CPU utilization 85% on Switch01\n")
        f.write("Jun 29 21:00:10 Router01 INFO: BGP neighbor 10.0.0.1 is established\n")
        f.write("Jun 29 21:00:15 Router02 ERROR: Interface GigabitEthernet0/1 is down\n")
        f.write("Jun 29 21:00:20 Firewall01 INFO: Connection established from 192.168.1.10\n")
        f.write("Jun 29 21:00:25 Switch02 ERROR: Spanning tree topology change detected\n")
        f.write("Jun 29 21:00:30 Router01 WARNING: Memory utilization 90% on Router01\n")
        f.write("Jun 29 21:00:35 Router02 ERROR: OSPF neighbor 10.0.0.2 is down\n")
        f.write("Jun 29 21:00:40 Switch01 INFO: MAC address table is full\n")
        f.write("Jun 29 21:00:45 Firewall01 WARNING: High traffic detected on outside interface\n")
    print("network.log created!")

# parse log and extract issues
def analyze_log(filename="network.log"):
    errors = []
    warnings = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if "ERROR" in line:
                errors.append(line)
            elif "WARNING" in line:
                warnings.append(line)

    print("\n=== Network Log Analysis ===\n")

    print("--- ERRORS ---")
    for e in errors:
        print(f"  {e}")

    print("\n--- WARNINGS ---")
    for w in warnings:
        print(f"  {w}")

    print(f"\nTotal errors  : {len(errors)}")
    print(f"Total warnings: {len(warnings)}")
    print(f"Total issues  : {len(errors) + len(warnings)}")

# run
create_sample_log()
analyze_log()
# Part 2 - Save analysis report to a dated file

def save_report(errors, warnings, filename=None):
    if not filename:
        date = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"report_{date}.txt"
    
    with open(filename, "w") as f:
        f.write("=== Network Log Analysis Report ===\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("--- ERRORS ---\n")
        for e in errors:
            f.write(f"  {e}\n")
        
        f.write("\n--- WARNINGS ---\n")
        for w in warnings:
            f.write(f"  {w}\n")
        
        f.write(f"\nTotal errors  : {len(errors)}\n")
        f.write(f"Total warnings: {len(warnings)}\n")
        f.write(f"Total issues  : {len(errors) + len(warnings)}\n")
    
    print(f"\nReport saved to {filename}")

# update analyze_log to return errors and warnings
def analyze_log(filename="network.log"):
    errors = []
    warnings = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if "ERROR" in line:
                errors.append(line)
            elif "WARNING" in line:
                warnings.append(line)

    print("\n=== Network Log Analysis ===\n")

    print("--- ERRORS ---")
    for e in errors:
        print(f"  {e}")

    print("\n--- WARNINGS ---")
    for w in warnings:
        print(f"  {w}")

    print(f"\nTotal errors  : {len(errors)}")
    print(f"Total warnings: {len(warnings)}")
    print(f"Total issues  : {len(errors) + len(warnings)}")
    
    # save report
    save_report(errors, warnings)

# run
create_sample_log()
analyze_log()