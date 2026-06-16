import numpy as np
import matplotlib.pyplot as plt

# Coeficientes de la serie trigonométrica (período T=1, ω0=2π)
a0 = 2 * (1 - np.cos(1))          # a0/2 = 1 - cos1
a_n = lambda n: 2 * (1 - np.cos(1)) / (1 - 4 * np.pi*2 * n*2)
b_n = lambda n: 4 * np.pi * n * np.sin(1) / (1 - 4 * np.pi*2 * n*2)

def serie_fourier(x, N):
    """
    Evalúa la serie de Fourier hasta el armónico N (inclusive)
    """
    f = a0 / 2  # término constante
    for n in range(1, N+1):
        f += a_n(n) * np.cos(2 * np.pi * n * x)
        f += b_n(n) * np.sin(2 * np.pi * n * x)
    return f

# Función original (solo en [0,1], luego se repite periódicamente)
def f_original(x):
    # Extensión periódica de período 1
    x_mod = x % 1.0
    return np.sin(x_mod)

# Gráfica
x = np.linspace(-1.5, 2.5, 500)  # Mostramos un par de períodos
valores_N = [1, 10, 100, 1000]

plt.figure(figsize=(12, 10))

for i, N in enumerate(valores_N, 1):
    plt.subplot(2, 2, i)
    y_fourier = serie_fourier(x, N)
    y_original = f_original(x)
    
    plt.plot(x, y_original, 'k--', linewidth=2, label='seno original (periódico)')
    plt.plot(x, y_fourier, 'r-', linewidth=1.5, label=f'Serie N={N}', color="#ff00ffb5")
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.xlim(-1.5, 2.5)
    plt.ylim(-1.2, 1.2)
    plt.grid(True, alpha=0.3)
    plt.title(f'Aproximación con N = {N} armónicos')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()

plt.tight_layout()
plt.show()