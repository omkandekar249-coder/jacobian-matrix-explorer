# jacobian-matrix-explorer
A Python tool that computes numerical Jacobians to explore stability and local behavior in multivariable systems. I originally put this project together right after high school as a way to get my hands dirty with Calculus III and Linear Algebra concepts before my college classes started. 

My thinking: 
- Direct Vector Functions: Defined systems directly in Python code rather than building a text parser/GUI. This avoided unnecessary software clutter and kept the focus purely on the mathematics.

- Numerical Differentiation: Used SciPy (scipy.optimize.approx_fprime) to calculate finite-difference approximations for Jacobian matrices.

- Phase-Space Mapping: Integrated NumPy and Matplotlib to render vector fields, flow patterns, and dynamic trajectories near equilibria.

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
- Numpy (Array vectorization & linear algebra operations)
- Scipy (Numerical differentiation via approx_fprime)
- Matplotlib (Vector field and phase-plane visualization)
