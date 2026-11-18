
def main():
    """Crea una lista del 1 al 100 y la muestra en orden inverso."""

    numeros = list(range(1, 101))
    numeros.reverse()
    print(", ".join(map(str, numeros)))


if __name__ == "__main__":
    main()
