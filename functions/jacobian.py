import numpy as np
from scipy.optimize import approx_fprime

def numerical_jacobian(func, x, epsilon=1e-6):
    """
    Compute numerical Jacobian of a vector-valued function.
    func: function R^n -> R^m
    x: point (numpy array)
    """
    x = np.asarray(x)
    m = len(func(x))
    n = len(x)
    J = np.zeros((m, n))

    for i in range(m):
        def fi(x):
            return func(x)[i]
        J[i, :] = approx_fprime(x, fi, epsilon)

    return J
