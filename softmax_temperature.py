#Path: evoapi_mcp\softmax_temperature.py

import numpy as np

def softmax(x):
    """
    Implementação da função softmax
    """
    exp_x = np.exp(x - np.max(x))  # Subtrai o máximo para estabilidade numérica
    return exp_x / exp_x.sum()

# Definindo os valores
T = 0.01  # Temperatura baixa
a = np.array([1, 2, 3, 4])

# Calculando softmax normal
print("Softmax normal:")
print(softmax(a))

# Calculando softmax com temperatura baixa
print("\nSoftmax com temperatura baixa (T=0.01):")
print(softmax(a/T))

if __name__ == "__main__":
    # Exemplo de uso com diferentes temperaturas
    temperatures = [0.01, 0.5, 1, 1000000]
    
    print("\nComparando diferentes temperaturas:")
    for temp in temperatures:
        print(f"\nTemperatura = {temp}")
        print(softmax(a/temp)) 