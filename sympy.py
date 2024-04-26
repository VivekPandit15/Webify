import sympy

# Create a symbol
x = sympy.Symbol('x')

# Create an expression
e = x**2 + 2*x + 1

# Differentiate the expression
diff = sympy.diff(e, x)

# Print the result
print(diff)
