import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

# Título
plt.title("Meu primeiro gŕafico com python")

# Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Cria o gráfico
plt.plot(x, y)
# Exibe o gráfico
plt.show()
