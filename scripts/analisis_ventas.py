
import pandas as pd
import matplotlib.pyplot as plt

# Leer dataset
df = pd.read_csv("datos/ventas.csv")

# Calcular ventas totales
ventas_totales = df["total"].sum()

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()

# Ventas por producto
ventas_por_producto = df.groupby("producto")["total"].sum()

# Mostrar resultados
print("Ventas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)

# Crear gráfico
ventas_por_producto.plot(kind="bar")

plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

print("Gráfico guardado en resultados/")
