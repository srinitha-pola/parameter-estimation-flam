
# Parameter Estimation using Numerical Optimization

## Objective

The goal of this assignment is to estimate the unknown parameters θ, M and X of a parametric curve using the given set of (x, y) data points.

---

## Problem Statement

The curve is defined as

```text
x = t*cos(θ) - e^(M|t|) * sin(0.3t) * sin(θ) + X

y = 42 + t*sin(θ) + e^(M|t|) * sin(0.3t) * cos(θ)
```

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
| θ | 30.000005° |
| M | 0.03000068 |
| X | 54.999999 |

Final L1 Loss: 10.371581837269922
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



## Additional Mathematics and Techniques Used

### 1. Parameter Estimation as an Optimization Problem

The unknown parameters (θ, M, X) were estimated by formulating the problem as a nonlinear optimization task.

The objective function minimizes the L1 distance between the observed dataset and the generated parametric curve.

Objective:

L(θ,M,X)=Σ|Pobserved−Ppredicted|

where

Pobserved=(x,y)

Ppredicted=(x(t),y(t))

### 2. Differential Evolution

A global optimization algorithm (Differential Evolution) was used to search the parameter space.

Advantages:

- Avoids local minima
- Works without gradient information
- Suitable for nonlinear functions

### 3. Local Optimization

After obtaining a good initial estimate from Differential Evolution, the solution was refined using the L-BFGS-B optimizer.

This improves parameter precision while respecting the parameter bounds.

### 4. KD-Tree Based Distance Computation

The dataset contains only (x,y) points and does not provide the corresponding parameter t.

Therefore, instead of matching points index-wise, the nearest point on the generated curve is found for every observed point.

SciPy's cKDTree was used to perform this nearest-neighbor search efficiently.

### 5. Dense Parametric Sampling

The curve was sampled using 3000 uniformly spaced values of t between 6 and 60.

A dense sampling improves approximation accuracy while maintaining reasonable computational cost.

### 6. Parameter Constraints

The optimization was performed under the following constraints:

θ ∈ (0°,50°)

M ∈ (-0.05,0.05)

X ∈ (0,100)

These constraints reduce the search space and improve convergence.

### 7. Computational Efficiency

The optimization repeatedly evaluates thousands of candidate curves.

Using KD-Tree reduces nearest-neighbor search complexity from approximately O(N²) to approximately O(N log N), making optimization significantly faster.



## Mathematical Formulation

The parametric curve is defined by:

```text
x(t) = t * cos(θ) - exp(M * |t|) * sin(0.3t) * sin(θ) + X

y(t) = 42 + t * sin(θ) + exp(M * |t|) * sin(0.3t) * cos(θ)
```

The objective is to estimate the unknown parameters **θ**, **M**, and **X** by minimizing the total L1 distance between the observed data points and the generated parametric curve.

The optimization problem is:

```text
Minimize:

L(θ, M, X) = Σ |P_observed - P_predicted|
```

Subject to the constraints:

- 0° < θ < 50°
- -0.05 < M < 0.05
- 0 < X < 100
- 6 ≤ t ≤ 60

| Method | Purpose |
|---------|---------|
| Differential Evolution | Global parameter search |
| L-BFGS-B | Local refinement |
| KD-Tree | Fast nearest-neighbor search |
| L1 Distance | Error metric |
