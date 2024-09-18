def convertir_lista_a_tupla(lista):
    return tuple(lista)

if __name__ == "__main__":
    compras = input("Ingrese una lista de compras: ")
    productos = compras.split(", ")
    print(f"Los productos en la lista de compras son: {productos}")
