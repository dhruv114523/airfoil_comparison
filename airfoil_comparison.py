import subprocess
import csv
import os

airfoils = ["2412", "0012", "0009"]
aoa_range = range(0, 16)

def run_xfoil_batch(airfoil, aoas, output_file):
    commands = [
        f"NACA {airfoil}",
        "OPER",
        "VISC 100000",
        "Ncrit 9",
        "ITER 100",
        "PACC",
        output_file,
        "",  # blank line = no dump file
    ]
    for alpha in aoas:
        commands.append(f"ALFA {alpha}")
    commands += ["", "QUIT"]

    process = subprocess.Popen(
        [r"C:\Pyhton\PyCharm Community Edition 2024.2.1\Files\WEbScraping\Personal Projects\airfoils\xfoil.exe"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    process.communicate('\n'.join(commands) + '\n\n')

def parse_polar_file(filepath, airfoil_name):
    results = []
    reading = False
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
                        results.append([airfoil_name, alpha, cl, cd, cm])
                    except ValueError:
                        continue
    return results

# Final combined output
with open(r"C:\Pyhton\PyCharm Community Edition 2024.2.1\Files\WEbScraping\Personal Projects\airfoils\airfoil_results.csv", mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Airfoil", "Alpha", "CL", "CD", "CM"])

    for airfoil in airfoils:
        print(f"⏳ Running NACA {airfoil}...")
        polar_file = f"polar_{airfoil}.txt"
        run_xfoil_batch(airfoil, aoa_range, polar_file)
        data = parse_polar_file(polar_file, f"NACA{airfoil}")
        writer.writerows(data)
        os.remove(polar_file)  # Clean up after parse
        print(f"✅ Done: {airfoil} ({len(data)} rows)")
