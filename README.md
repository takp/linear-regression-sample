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

![Polynomial Basis](https://raw.githubusercontent.com/takp/linear-regression-sample/master/images/polynomial_basis.jpg)

Then, the function can be expressed as below.

![General function](https://raw.githubusercontent.com/takp/linear-regression-sample/master/images/general_function.jpg)

This time, I define the basis function as 4 dimensional. Thence, 

![function](https://raw.githubusercontent.com/takp/linear-regression-sample/master/images/function.jpg)

Using matrix, these "omega" can be solved by this equation.

![omega equation](https://raw.githubusercontent.com/takp/linear-regression-sample/master/images/omega_equation.jpg)

Phi is the matrix as following.

![Phi](https://raw.githubusercontent.com/takp/linear-regression-sample/master/images/Phi.jpg)

### Graph

![Graph](https://raw.githubusercontent.com/takp/linear-regression-sample/master/images/graph.png)


### Reference

(Japanese) http://gihyo.jp/dev/serial/01/machine-learning/0011?page=1

