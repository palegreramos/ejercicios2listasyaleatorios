
from random import choice

def solicitar_cantidad():
    """Solicita un número entero positivo.

    Returns:
        int: Cantidad de palabras.
    """
    while True:
        try:
            cantidad = int(input("¿Cuántas palabras quieres introducir? "))

            if cantidad <= 0:
                raise ValueError("El número debe ser mayor que cero.")

            return cantidad

        except ValueError as error:
            print(f"Error: {error}")


def solicitar_palabra(mensaje):
    """Solicita una palabra que no esté vacía.

    Args:
        mensaje (str): Texto que se muestra al usuario.

    Returns:
        str: Palabra introducida.
    """
    while True:
        palabra = input(mensaje).strip()

        if palabra:
            return palabra

        print("Error: la palabra no puede estar vacía.")


def crear_lista(cantidad):
    """Crea una lista de palabras.

    Args:
        cantidad (int): Número de palabras que se solicitarán.

    Returns:
        list: Lista de palabras.
    """
    palabras = []

    for i in range(cantidad):
        palabra = solicitar_palabra(f"Introduce la palabra {i + 1}: ")
        palabras.append(palabra)

    return palabras


def modificar_palabra_central(palabras):
    """Sustituye la palabra central de la lista.

    Args:
        palabras (list): Lista de palabras que se modificará.
    """
    nueva_palabra = solicitar_palabra("Introduce la nueva palabra: ")
    indice = len(palabras) // 2
    palabras[indice] = nueva_palabra


def buscar_palabra(palabras):
    """Comprueba si una palabra está en la lista.

    Args:
        palabras (list): Lista en la que se buscará.
    """
    palabra = solicitar_palabra("¿Qué palabra quieres buscar? ")

    if palabra in palabras:
        print(f"La palabra {palabra} está en la lista.")
    else:
        print(f"La palabra {palabra} NO está en la lista.")


def seleccionar_palabra(palabras):
    """Selecciona una palabra aleatoria de la lista.

    Args:
        palabras (list): Lista de palabras.

    Returns:
        str: Palabra seleccionada aleatoriamente.
    """
    return choice(palabras)


def main():
    """Gestiona la creación, modificación y consulta de palabras."""
    cantidad = solicitar_cantidad()
    palabras = crear_lista(cantidad)

    print(f"\nLista original: {palabras}")

    modificar_palabra_central(palabras)
    print(f"Lista modificada: {palabras}")

    buscar_palabra(palabras)

    print(f"Palabra aleatoria: {seleccionar_palabra(palabras)}")


if __name__ == "__main__":
    main()
