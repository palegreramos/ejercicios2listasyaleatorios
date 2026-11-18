
from random import randint

def generar_numeros():
    """Genera una lista con una cantidad aleatoria de números.

    Returns:
        list: Lista de números aleatorios entre 1 y 20.
    """
    numeros = []

    cantidad = randint(1, 20)
    for _ in range(cantidad):
        numeros.append(randint(1, 20))

    return numeros


def main():
    """Genera y muestra una lista de números aleatorios."""
    numeros = generar_numeros()
    print(f"Lista de números: {numeros}")
    print(f"Número de elementos: {len(numeros)}")


if __name__ == "__main__":
    main()
