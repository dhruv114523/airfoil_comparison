import subprocess
import csv
import os
import numpy as np

airfoils = ["2412", "0012", "0009"]
aoa_range = range(0, 14)
np.random.seed(123)

def run_xfoil_batch(airfoil, aoas, reynolds_num, output_file):
    commands = [
        f"NACA {airfoil}",
        "OPER",
        f"VISC {int(reynolds_num)}",
        "Ncrit 9",
        "ITER 100",
        "PACC",
        output_file,
        "",  # blank line = no dump file
    ]
    for alpha in aoas:
        commands.append(f"ALFA {alpha}")
    commands += ["", "QUIT"]

    try:
        process = subprocess.Popen(
            [r"C:\Pyhton\PyCharm Community Edition 2024.2.1\Files\WEbScraping\Personal Projects\airfoils\xfoil.exe"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate('\n'.join(commands) + '\n\n', timeout=30)
        
        if process.returncode != 0:
            print(f"⚠️  XFOIL returned error code {process.returncode} for NACA {airfoil}, Re={reynolds_num}")
            return False
        
        return True
        
    except subprocess.TimeoutExpired:
        print(f"⚠️  XFOIL timed out for NACA {airfoil}, Re={reynolds_num}")
        process.kill()
        return False
    except FileNotFoundError:
        print("❌ XFOIL executable not found! Make sure xfoil.exe is in the project directory.")
        return False
    except Exception as e:
        print(f"⚠️  Unexpected error running XFOIL for NACA {airfoil}, Re={reynolds_num}: {e}")
        return False

def parse_polar_file(filepath, airfoil_name, reynolds_num):
    results = []
    reading = False
    
    try:
        with open(filepath, 'r') as f:
            for line in f:
                if "----" in line:
                    reading = True
                    continue
                if reading:
                    parts = line.split()
                    if len(parts) >= 6:
                        try:
                            alpha = float(parts[0])
                            cl = float(parts[1])
                            cd = float(parts[2])
                            cm = float(parts[4])
                            results.append([airfoil_name, reynolds_num, alpha, cl, cd, cm])
                        except ValueError:
                            continue
        return results
        
    except FileNotFoundError:
        print(f"⚠️  Polar file not found for {airfoil_name}, Re={reynolds_num}")
        return []
    except Exception as e:
        print(f"⚠️  Error parsing polar file for {airfoil_name}, Re={reynolds_num}: {e}")
        return []

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

# Final combined output
with open(r"test.csv", mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Airfoil", "Reynolds", "Alpha", "CL", "CD", "CM"])

    for airfoil in airfoils:
        print(f"⏳ Running NACA {airfoil}...")
        reynolds_nums = np.random.normal(loc=100_000, scale=2_000, size=10)  # Set to 10 for testing
        successful_runs = 0
        
        for i, Re in enumerate(reynolds_nums, start=1):
            Re = int(abs(Re))  # make sure Re is positive and integer
            polar_file = f"polar_{airfoil}.txt"
            
            # Run XFOIL with error handling
            if run_xfoil_batch(airfoil, aoa_range, Re, polar_file):
                data = parse_polar_file(polar_file, f"NACA{airfoil}", Re)
                
                if data:  # Only write if we got valid data
                    writer.writerows(data)
                    successful_runs += 1
                    print(f"✅ {ordinal(i)} simulation for NACA {airfoil} done — Re={Re}, Rows={len(data)}")
                else:
                    print(f"⚠️  {ordinal(i)} simulation for NACA {airfoil} failed (no data) — Re={Re}")
            else:
                print(f"⚠️  {ordinal(i)} simulation for NACA {airfoil} failed (XFOIL error) — Re={Re}")
            
            # Clean up polar file if it exists
            if os.path.exists(polar_file):
                os.remove(polar_file)
        
        print(f"🎯 NACA {airfoil} completed: {successful_runs}/{len(reynolds_nums)} successful runs")