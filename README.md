# jacobian-matrix-explorer
A Python tool that computes numerical Jacobians to explore stability and local behavior in multivariable systems. A project I originally wrote after high school when I was trying to understand Calc 3 and start to practice linear algebra. I kept the design simple by defining functions directly in the code rather than adding user input, which made the exploration more focused.

To Run:
- Specify the multivariable function
  - Ex.
  - def vector_field(x):
    x1, x2 = x
    return np.array([
        x1 * (1 - x2),
        x2 * (x1 - 1)
    ])
- Choose a point to evaluate the jacobian
  - Ex. point = np.array([1.0, 1.0])

libraries used:
- Scipy
- Numpy
- Matplotlib
