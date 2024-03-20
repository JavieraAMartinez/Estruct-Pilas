class Pila:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tope = -1
        self.pila = [None] * tamanio

    def esta_vacia(self):
        return self.tope == -1

    def esta_llena(self):
        return self.tope == self.tamanio - 1

    def insertar(self, dato):
        if self.esta_llena():
            print("Error: Desbordamiento de pila")
            return
        self.tope += 1
        self.pila[self.tope] = dato

    def eliminar(self):
        if self.esta_vacia():
            print("Error: Subdesbordamiento de pila")
            return None
        dato = self.pila[self.tope]
        self.tope -= 1
        return dato

    def mostrar(self):
        if self.esta_vacia():
            print("Pila vacía")
            return
        for i in range(self.tope, -1, -1):
            print(self.pila[i])

def main():
    tamanio = 8
    pila = Pila(tamanio)

    pila.insertar("X")
    pila.insertar("Y")
    pila.insertar("Z")
    pila.eliminar()
    pila.eliminar()
    pila.eliminar()
    pila.insertar("V")
    pila.insertar("W")
    pila.eliminar()
    pila.insertar("R")

    print("Estado final de la pila:")
    pila.mostrar()
    print(f"Cantidad de elementos en la pila: {pila.tope + 1}")

if __name__ == "__main__":
    main()


