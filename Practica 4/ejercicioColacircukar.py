class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1

    def esta_vacia(self):
        return self.frente == -1
    
    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente
    
    def encolar(self, dato):
        if self.esta_llena():
            print("La cola está llena, no se permiten mas turnos")
            return False
        
        if self.esta_vacia():
            self.frente = 0
            self.final = 0
        else: 
            self.final = (self.final + 1) % self.capacidad

        self.cola[self.final] = dato
        print(f"Turno '{dato}'se a agregado")
        return True

    def descolar(self):
        if self.esta_vacia():
            print("No hay turnos")
            return None                
        
        dato = self.cola[self.frente]
        print(f"Atendiendo a: {dato}")

        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        else: 
            self.frente = (self.frente + 1) % self.capacidad

        return dato    
    
    def ver_frente(self):
        if self.esta_vacia():
            print("La cola está vacía.")
            return None
        print(f"El siguiente turno es: {self.cola[self.frente]}")
        return self.cola[self.frente]
    
    def mostrar(self):
        if self.esta_vacia():
            print("[ Cola vacía ]")
            return
        
        elementos = []
        i = self.frente
        while True:
            elementos.append(self.cola[i])
            if i == self.final:
                break
            i = (i + 1) % self.capacidad
        print("Turnos actuales:", " -> ".join(map(str, elementos)))


def menu():
    sistema_turnos = ColaCircular(5) 
    
    while True:
        print("\n--- Gestion de turnos ---")
        print("1. Insertar turno")
        print("2. Atender turno (Eliminar)")
        print("3. Ver próximo turno")
        print("4. Mostrar los turnos totales")
        print("5. Verificar estado (Llena/Vacía)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre o  ID del turno: ")
            sistema_turnos.encolar(nombre)
        elif opcion == "2":
            sistema_turnos.descolar()
        elif opcion == "3":
            sistema_turnos.ver_frente()
        elif opcion == "4":
            sistema_turnos.mostrar()
        elif opcion == "5":
            if sistema_turnos.esta_llena():
                print("Estado: La cola está llena.")
            elif sistema_turnos.esta_vacia():
                print("Estado: La cola está vacia.")
            else:
                print("Estado: La cola tiene espacio disponible.")
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()