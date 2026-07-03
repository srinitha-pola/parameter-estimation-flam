import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import differential_evolution, minimize
from scipy.spatial import cKDTree

data = pd.read_csv("data/xy_data.csv")


def parametric_curve(t, theta, M, X):
    """
    Generate the parametric curve.
    theta is in radians.
    """

    x = (
        t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    )

    y = (
        42 + t * np.sin(theta) + np.exp(M * np.abs(t))*np.sin(0.3 * t) * np.cos(theta)
    )

    return x, y



def loss_function(params):
    theta, M, X = params

    t = np.linspace(6, 60, 3000)

    x_pred, y_pred = parametric_curve(t, theta, M, X)

    predicted_points = np.column_stack((x_pred, y_pred))
    actual_points = data[["x", "y"]].values

    tree = cKDTree(predicted_points)

    _, indices = tree.query(actual_points)

    nearest_points = predicted_points[indices]

    l1_distance = np.abs(actual_points - nearest_points).sum(axis=1)

    return np.sum(l1_distance)


def main():

    bounds = [
        (np.deg2rad(0), np.deg2rad(50)),
        (-0.05, 0.05),
        (0, 100),
    ]

    print("=" * 60)
    print("Starting Parameter Estimation...")
    print("=" * 60)

    result = differential_evolution(
        loss_function,
        bounds=bounds,
        strategy="best1bin",
        maxiter=100,
        popsize=20,
        tol=1e-7,
        polish=False,
        seed=42,
    )

    refined = minimize(
        loss_function,
        result.x,
        method="L-BFGS-B",
        bounds=bounds,
    )

    theta, M, X = refined.x

    print("\nEstimated Parameters")
    print("-" * 40)
    print(f"Theta : {np.degrees(theta):.6f} degrees")
    print(f"M     : {M:.8f}")
    print(f"X     : {X:.6f}")
    print(f"L1 Loss : {refined.fun:.6f}")

    t = np.linspace(6, 60, 3000)

    x_fit, y_fit = parametric_curve(t, theta, M, X)

    plt.figure(figsize=(8, 8))

    plt.scatter(
        data["x"],
        data["y"],
        s=8,
        label="Given Data",
    )

    plt.plot(
        x_fit,
        y_fit,
        "r",
        linewidth=2,
        label="Estimated Curve",
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Actual vs Estimated Curve")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()

    plt.savefig("plots/fitted_curve.png", dpi=300)

    plt.show()


if __name__ == "__main__":
    main()
