# Linear Regression

Sample program to model the data using linear regression, and show the graph.

### Environment

- Python 2.7.6
- Numpy
- Matplotlib

### Run

	$ python linear_regression.py

### Logic

Use the polynomial basis as the basis function.

![Polynomial Basis](https://github.com/takp/linear-regression-sample/images/polynomial_basis.jpg)

Then, the function can be expressed as below.

![General function](https://github.com/takp/linear-regression-sample/images/general_function.jpg)

This time, I define the basis function as 4 dimensional. Thence, 

![function](https://github.com/takp/linear-regression-sample/images/function.jpg)

Using matrix, these "omega" can be solved by this equation.

![omega equation](https://github.com/takp/linear-regression-sample/images/omega_equation.jpg)

Phi is the matrix as following.

![Phi](https://github.com/takp/linear-regression-sample/images/Phi.jpg)

### Reference

(Japanese) http://gihyo.jp/dev/serial/01/machine-learning/0011?page=1

