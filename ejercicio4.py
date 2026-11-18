
def solicitar_num(mensaje):
    """Solicita un número decimal positivo.

    Args:
        mensaje (str): Texto que se muestra al usuario.

    Returns:
        float: Número positivo introducido.
    """
    while True:
        try:
            num = float(input(mensaje))

            if num <= 0:
                raise ValueError("El número debe ser mayor que cero.")

            return num

        except ValueError as error:
            print(f"Error: {error}")


def calcular_imc(peso, estatura):
    """Calcula el índice de masa corporal.

    Args:
        peso (float): Peso de la persona en kilogramos.
        estatura (float): Estatura de la persona en metros.

    Returns:
        float: Índice de masa corporal calculado.
    """
    return peso / estatura ** 2


def main():
    """Solicita el peso y la estatura y muestra el IMC."""
    peso = solicitar_num("Introduce tu peso en kg: ")
    estatura = solicitar_num("Introduce tu estatura en metros: ")

    imc = calcular_imc(peso, estatura)

    print(f"Tu índice de masa corporal es {imc:.2f}")


if __name__ == "__main__":
    main()
