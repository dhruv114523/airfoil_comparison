# Airfoil Cl vs Cd Analysis (NACA 4-Digit Series)

This project visualizes aerodynamic performance metrics — specifically the **Lift Coefficient (Cl)** and **Lift-to-Drag Ratio (Cl/Cd)** — for several NACA 4-digit airfoils. The analysis uses real-world data to compare how different airfoil shapes perform across various angles of attack (AOA).

---

## 📊 What This Script Does

The `01_plot_cl_vs_cd.R` script performs the following:

- **Reads performance data** for airfoils NACA 0009, 0012, and 2412.
- **Plots Cl vs AOA** for each airfoil to observe lift generation.
- **Plots Cl/Cd vs AOA** to evaluate aerodynamic efficiency before stall.
- Visualizes and compares the behavior of each airfoil across identical conditions.

---

## 🛠 Technologies Used

- **R**
- **ggplot2** for plotting
- **Base R** for data manipulation

---

## 📁 File Structure
project-root/
│
├── data/
│ └── all_naca_cl_vs_cd.csv # Input dataset with Cl, Cd, and AOA values
│
├── 01_plot_cl_vs_cd.R # Main script for Cl and Cl/Cd plots
├── README.md 


---

## ▶️ How to Run

1. Open `01_plot_cl_vs_cd.R` in RStudio.
2. Ensure the CSV file is located in the `data/` folder.
3. Run the script to generate the plots.
4. The output will display in RStudio's **Plots** panel.

---

##  Notes

- The plots focus on **pre-stall behavior** to highlight efficient operating ranges.
- All values are based on assumed or experimental aerodynamic data from different AOA values.
- File paths are relative to ensure compatibility across systems.

---

## Sample Output
![cl_cd vs AOA](https://github.com/user-attachments/assets/f0c4cc81-b2da-4db8-b64b-a5557885c729)

---

## Author

Dhruv — personal project for airfoil performance comparison.  


