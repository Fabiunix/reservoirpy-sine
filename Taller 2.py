import sympy as sp

# Definir la variable y constante
x = sp.Symbol('x', real=True, positive=True)
k = sp.Symbol('k', real=True)

# f(x) = k * x^2   para 0 < x < 6
# 1) Calcular k para que el área total sea 1
integral_k = sp.integrate(k * x**2, (x, 0, 6))
k_value = sp.solve(sp.Eq(integral_k, 1), k)[0]

# 2) Definir la función de densidad con k encontrado
f_x = k_value * x**2

# 3) Calcular la función de distribución acumulada F(x)
F_x = sp.integrate(f_x, (x, 0, x))

# 4) Calcular la probabilidad P(X < 5)
P_X_less_5 = F_x.subs(x, 5)

# 5) Calcular la media E[X]
E_X = sp.integrate(x * f_x, (x, 0, 6))

# 6) Calcular E[X^2]
E_X2 = sp.integrate(x**2 * f_x, (x, 0, 6))

# 7) Calcular la varianza Var(X) = E[X^2] - (E[X])^2
Var_X = E_X2 - E_X**2

# Mostrar resultados
print("Constante de normalización k =", k_value)
print("f(x) =", f_x)
print("F(x) =", F_x)
print("P(X < 5) =", P_X_less_5, "≈", float(P_X_less_5))
print("E[X] =", E_X, "≈", float(E_X))
print("E[X^2] =", E_X2, "≈", float(E_X2))
print("Var(X) =", Var_X, "≈", float(Var_X))




