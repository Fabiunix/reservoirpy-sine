import numpy as np
import matplotlib.pyplot as plt
from reservoirpy.nodes import Reservoir, Ridge

# 1. Generar datos (una onda seno)
t = np.linspace(0, 20*np.pi, 2000)
data = np.sin(t)

# Usamos los primeros 1500 puntos para entrenar y el resto para probar
train_data = data[:200].reshape(-1, 1)
test_data = data[1500:].reshape(-1, 1)

# 2. Crear un reservorio y una capa de salida (ridge regression)
reservorio = Reservoir(100, sr=0.9)   # 100 neuronas en el reservorio
salida = Ridge(ridge=1e-6)

# 3. Conectar reservorio -> salida
model = reservorio >> salida

# 4. Entrenar el modelo (input = seno actual, output = seno siguiente)
X_train = train_data[:-1]
y_train = train_data[1:]
model = model.fit(X_train, y_train)

# 5. Predecir la serie de prueba
X_test = test_data[:-1]
y_test = test_data[1:]
y_pred = model.run(X_test)

# 6. Graficar resultados
plt.figure(figsize=(10,5))
plt.plot(y_test, label="Real")
plt.plot(y_pred, label="Predicho", linestyle="--")
plt.title("Predicción de una onda seno con ReservoirPy")
plt.legend()
plt.show()
