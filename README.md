# Aerodynamic Properties Simulator

This is a **Python wrapper** around the XFOIL program that simulates aerodynamic properties of NACA airfoils.  
It automates the process of generating airfoil data (CL, CD, CM) over a range of angles of attack using XFOIL's command-line interface.

---

## Features

- Supports multiple NACA airfoils (e.g., 2412, 0012, 0009)
- Automatically sweeps angles of attack (0° to 15°) (can be changed as well)
- Saves results to a clean, structured **CSV file**
- Handles convergence and output parsing gracefully
- Fully offline, runs with local `xfoil.exe`

---

## Requirements

- Python 3.x
- A working `xfoil.exe` in your project folder  
  [Download XFOIL binary](https://web.mit.edu/drela/Public/web/xfoil/)

---

## Usage

1. Drop `xfoil.exe` into your project folder.
2. Run the script:

```bash
python airfoil_comparison.py
```

## Future Improvements Planned
- Automatic Plots Generation
- Reynolds Number Variation
- Confidence Intervals

> Note: Legacy version of this project (which was just some basic graphs) is in the `legacy` folder.  
> While they're considered to be a part of the same project, the two scripts (`airfoil_comparison.py` and `airfoil_comparison.R`) differ wildly in their function.  
> The R script file (under the `legacy` folder) is just for graphs, while the python script is an xfoil.exe wrapper, which will do the simulations for you. It currently does not have plotting capability, but it will be added in a later update  
> If you're here from LinkedIn, and are looking for the script used for the report, it is under the `legacy` folder as well
