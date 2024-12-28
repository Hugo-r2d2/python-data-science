import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5] # No gráfico de barra isso quer dizer a barra 1, 2, 3, 4 e 5
y = [2, 3, 7, 1, 12] # Aqui temos o tamanho da barra respectivamente ao x

titulo = 'Gráfico de Barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Criação e Exibição
plt.bar(x, y)
plt.show()