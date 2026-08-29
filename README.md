# Airfoil Lift Modeling with Machine Learning

This project focuses on analyzing airfoil geometry and predicting the mean lift coefficient using data from `LM.csv`. The main script is `tree.py`, which prepares the dataset, extracts geometric features from each NACA airfoil code, creates diagnostic plots, and compares machine learning models for prediction.

The older linear-model workflow has been moved to the legacy archive under `legacy/lm/`.

---

## Main Script

- `tree.py` — current primary analysis workflow
- `LM.csv` — source data used for modeling
- `lm_plots/` — saved diagnostic plots and model visuals
- `legacy/lm/README.md` — archived legacy documentation
- `legacy/lm/lm.py` — archived legacy modeling script

---

## What `tree.py` Does

`tree.py` performs the following steps:

1. Loads `LM.csv` and groups the data by `Alpha` and `Airfoil` to reduce repeated measurements.
2. Extracts the NACA code from each airfoil label, such as `2412`, and converts it into:
   - `M` = max camber
   - `P` = position of max camber
   - `T` = thickness
3. Builds a geometry table with `Mean_CL` as the target variable.
4. Produces scatter plots and regression-style visualizations for `M`, `P`, and `T` against mean lift.
5. Splits the data into train and test sets.
6. Trains and evaluates:
   - Random Forest Regressor
   - XGBoost Regressor
7. Prints model performance metrics including RMSE, MAE, and R².

---

## Data Flow

The workflow is centered on the geometry-based lift model:

```text
LM.csv
  -> tree.py
  -> feature extraction (M, P, T)
  -> Mean_CL target
  -> train/test split
  -> model training
  -> RMSE / MAE / R² output
  -> lm_plots/*.png
```

---

## Requirements

Install the project dependencies:

```bash
pip install -r requirements.txt
```

The analysis in `tree.py` relies on the following Python packages:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `scikit-learn`
- `xgboost`

---

## Run the Analysis

From the project root:

```bash
python tree.py
```

This will generate visual outputs in the `lm_plots/` folder and print evaluation metrics for both trained models in the terminal.

---

## Output Files

The script creates and uses:

- `lm_plots/M_vs_cl.png`
- `lm_plots/P_vs_cl.png`
- `lm_plots/T_vs_cl.png`
- model summary output in the console

---

## Legacy Materials

The historical documentation and earlier modeling script were archived to preserve the original workflow:

- `legacy/lm/README.md`
- `legacy/lm/lm.py`

These files are kept for reference, while the active project workflow is now driven by `tree.py`.
