import sympy as sp

# =====================================================
# ============ PROBLEMA 1: Probabilidad Discreta ======
# =====================================================

# Probabilidades dadas (hipergeométricas)
# P(0,0), P(1,0), P(0,1)
P_00 = 3/28
P_10 = 9/28
P_01 = 6/28

# Probabilidad total
P_total = P_00 + P_10 + P_01

print("=== Problema 1 ===")
print("P(0,0) =", P_00)
print("P(1,0) =", P_10)
print("P(0,1) =", P_01)
print("P total =", P_total)
print()


# =====================================================
# ============ PROBLEMA 2: Densidad Conjunta Continua =
# =====================================================

# Variables simbólicas
x, y = sp.symbols('x y', real=True, nonnegative=True)

# Función de densidad
f_xy = (2/5) * (2*x + 3*y)

# Verificación de normalización: integral total debe ser 1
integral_total = sp.integrate(sp.integrate(f_xy, (x, 0, 1)), (y, 0, 1))

# Probabilidad en la región R: 0 < x < 1/2, 1/4 < y < 1/2
P_region = sp.integrate(sp.integrate(f_xy, (x, 0, 1/2)), (y, 1/4, 1/2))

print("=== Problema 2 ===")
print("Integral total =", integral_total)
print("Probabilidad en la región R =", P_region)
print()


# =====================================================
# ============ PROBLEMA 3: Distribución Discreta ======
# =====================================================

# (a) P(x+y=4)
P_xy_eq4 = 0

# (b) P(x > y)
total_posibilidades = 31
favorables = 15
P_x_mayor_y = favorables / total_posibilidades

# (c) P(x ≥ 2, y ≤ 1)
favorables_c = 2
P_x2_y1 = favorables_c / total_posibilidades

print("=== Problema 3 ===")
print("P(x+y=4) =", P_xy_eq4)
print("P(x > y) =", P_x_mayor_y)
print("P(x ≥ 2, y ≤ 1) =", P_x2_y1)
print()


# =====================================================
# ============ EJEMPLO 1: Probabilidad Condicional ====
# =====================================================

P_E = 0.7
P_A = 0.6
P_EA = 0.55

# P(A|E) = P(E ∩ A) / P(E)
P_A_dado_E = P_EA / P_E

print("=== Ejemplo 1 ===")
print("P(A|E) =", P_A_dado_E)
print()


# =====================================================
# ============ EJEMPLO 2: Probabilidad Conjunta =======
# =====================================================

# Densidad constante en el rectángulo definido
f_xy_const = 0.05

# Región: 7 ≤ x ≤ 10, 7 ≤ y ≤ 8
P_cafe = sp.integrate(sp.integrate(f_xy_const, (x, 7, 10)), (y, 7, 8))

print("=== Ejemplo 2 ===")
print("P(7 ≤ x ≤ 10, 7 ≤ y ≤ 8) =", P_cafe)
