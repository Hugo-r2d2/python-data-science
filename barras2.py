import matplotlib.pyplot as plt
# Gráfico de barras para comparar dois eixos x e y

x1 = [1, 3, 5, 7, 9] 
y1 = [2, 3, 7, 1, 12]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 20]

titulo = 'Gráfico de Barras 2'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)



# Criação e Exibição
plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")
plt.legend()

plt.show()