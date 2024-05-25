
import numpy as np
import matplotlib.pyplot as plt

def fator_amplificacao(z, W):
    return 1 + z + W * z**2

def plot_regiao_estabilidade(ax, W):
    x = np.linspace(-10, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    R = fator_amplificacao(Z, W)
    abs_R = np.abs(R)
    contour = ax.contour(X, Y, abs_R, levels=[1], colors='black')
    ax.contourf(X, Y, abs_R, levels=[0, 1], colors='black', alpha=0.1)
    ax.clabel(contour, inline=True, fontsize=8, fmt=f'W = {W}')

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(which='both', color='gray', linestyle='--', linewidth=0.5)
    ax.set_aspect('equal')
    ax.set_title(f'Região de Estabilidade para W = {W}')

W_values = [-1, 0.1, 1]

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

for ax, W in zip(axs, W_values):
    plot_regiao_estabilidade(ax, W)

plt.tight_layout()
plt.show()


