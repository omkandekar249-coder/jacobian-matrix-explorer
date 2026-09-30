import numpy as np
from jacobian import numerical_jacobian

def vector_field(x):
    # Example nonlinear system
    # x = [x1, x2]
    x1, x2 = x
    return np.array([
        x1 * (1 - x2),
        x2 * (x1 - 1)
    ])

point = np.array([1.0, 1.0])
J = numerical_jacobian(vector_field, point)

print("Jacobian at", point)
print(J)
