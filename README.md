
# Parameter Estimation using Numerical Optimization

## Objective

The goal of this assignment is to estimate the unknown parameters θ, M and X of a parametric curve using the given set of (x, y) data points.

---

## Problem Statement

The curve is defined as

\[
x=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
\]

\[
y=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
\]

where

- 0° < θ < 50°
- -0.05 < M < 0.05
- 0 < X < 100
- 6 ≤ t ≤ 60

The objective is to estimate θ, M and X from the provided dataset.

---

## Methodology

1. Load the given dataset.
2. Implement the parametric equations.
3. Generate a dense parametric curve.
4. Compute the L1 distance between the observed points and the predicted curve.
5. Use Differential Evolution for global optimization.
6. Refine the solution using L-BFGS-B optimization.
7. Plot the fitted curve against the original data.

---

## Libraries Used

- NumPy
- Pandas
- Matplotlib
- SciPy

---

## Optimization Algorithm

- Differential Evolution (Global Search)
- L-BFGS-B (Local Refinement)

---

## Estimated Parameters

| Parameter | Value |
|-----------|--------|
| θ | 30.000036° |
| M | 0.03000046 |
| X | 55.000014 |

---

## Final Equation

```
(
t*cos(0.523599)
-e^(0.03*abs(t))*sin(0.3*t)*sin(0.523599)+55,

42+t*sin(0.523599)
+e^(0.03*abs(t))*sin(0.3*t)*cos(0.523599)
)
```

Domain:

```
6 ≤ t ≤ 60
```

---

## Repository Structure

```
parameter-estimation-flam
│
├── data
│   └── xy_data.csv
│
├── src
│   └── estimate.py
│
├── plots
│   └── fitted_curve.png
│
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

Run

```bash
python src/estimate.py
```

---

## Output

The script prints the estimated parameters and generates the fitted curve.

## Desmos Equation

```
(
t*cos(0.523599)-e^(0.03*abs(t))*sin(0.3*t)*sin(0.523599)+55,
42+t*sin(0.523599)+e^(0.03*abs(t))*sin(0.3*t)*cos(0.523599)
)
```

Domain:

```
6 ≤ t ≤ 60
```
