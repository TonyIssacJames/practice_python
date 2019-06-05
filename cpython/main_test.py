import equation_cy
import equation_py
import timeit

if __name__=='__main__':
	print(equation_cy.equation(1), equation_cy.equation(10))
	cy = timeit.timeit(equation_cy.equation(33),number= 10000)
	py = timeit.timeit(equation_py.equation(33),number= 10000)

	print("Cython time: ", cy)
	print("Python time: ", py)
