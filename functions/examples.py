import numpy as np
import matplotlib.pyplot as plt
from jacobian import numerical_jacobian


def vector_field(x):
    """
    Example nonlinear system:
        dx/dt = x1 * (1 - x2)
        dy/dt = x2 * (x1 - 1)
    """
    x1, x2 = x
    return np.array([
        x1 * (1 - x2),
        x2 * (x1 - 1)
    ])

point = np.array([1.0, 1.0])
J = numerical_jacobian(vector_field, point)

print("Jacobian at", point)
print(J)


def plot_vector_field():
    x_vals = np.linspace(-2, 2, 20)
    y_vals = np.linspace(-2, 2, 20)

    X, Y = np.meshgrid(x_vals, y_vals)
    U = X * (1 - Y)
    V = Y * (X - 1)

    plt.figure(figsize=(6, 6))
    plt.quiver(X, Y, U, V, color="purple")
    plt.title("Vector Field Visualization")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


