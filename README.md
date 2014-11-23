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

![Polynomial Basis](http://www.sciweavers.org/tex2img.php?eq=%20%5Cphi_%7Bm%7D%20%20%28x%29%20%3D%20%20x%5E%7Bm-1%7D&bc=White&fc=Black&im=jpg&fs=18&ff=arev&edit=0)

Then, the function can be expressed as below.

![General function](http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%20%5Comega_%7B1%7D%20%2B%20%5Comega_%7B2%7Dx%20%2B%20%5Comega_%7B3%7Dx%5E%7B2%7D%20%2B%20...%20%2B%20%5Comega_%7BM%7Dx%5E%7BM-1%7D&bc=White&fc=Black&im=jpg&fs=18&ff=arev&edit=0)

This time, I define the basis function as 4 dimensional. Thence, 

![function](http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%20%5Comega_%7B1%7D%20%2B%20%5Comega_%7B2%7Dx%20%2B%20%5Comega_%7B3%7Dx%5E%7B2%7D%20%2B%20%5Comega_%7B4%7Dx%5E%7B3%7D&bc=White&fc=Black&im=jpg&fs=18&ff=arev&edit=0)

Using matrix, these "omega" can be solved by this equation.

![omega equation](http://www.sciweavers.org/tex2img.php?eq=%5Comega%20%3D%20%28%20%5CPhi%5E%7BT%7D%5CPhi%20%29%5E%7B-1%7D%5CPhi%5E%7BT%7Dt&bc=White&fc=Black&im=jpg&fs=18&ff=arev&edit=0)
	w = (PhiT Phi)

Phi is the matrix as following.

![Phi](http://www.sciweavers.org/tex2img.php?eq=%20%5CPhi%20%3D%20%20%5Cbegin%7Bbmatrix%7D%20%5Cphi_%7B1%7D%28x_%7B1%7D%29%20%26%20%5Cphi_%7B2%7D%28x_%7B1%7D%29%20%26%20...%20%26%20%5Cphi_%7BM%7D%28x_%7B1%7D%29%20%5C%5C%20...%20%26%20...%20%26%20...%20%26%20...%20%5C%5C%20%5Cphi_%7B1%7D%28x_%7BN%7D%29%20%26%20%5Cphi_%7B2%7D%28x_%7BM%7D%29%20%26%20...%20%26%20%5Cphi_%7BM%7D%28x_%7BN%7D%29%20%5Cend%7Bbmatrix%7D%20&bc=White&fc=Black&im=jpg&fs=18&ff=arev&edit=0)

### Reference

(Japanese) http://gihyo.jp/dev/serial/01/machine-learning/0011?page=1

