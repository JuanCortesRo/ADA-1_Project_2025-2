"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

PRIMERA SOLUCIÓN
Problema: Asociación de Deportes 
Estructura de datos utilizada: Arboles Rojinegros
Archivo: first_solution.py

Diciembre 2025
"""

# ========================================================================================
# CLASES BASE PARA NODOS Y ÁRBOLES (BASADAS EN EL CÓDIGO ORIGINAL)
# ========================================================================================

class NodoRB:
    """Nodo base del árbol rojinegro"""
    def __init__(self, id_elemento, dato1, dato2, nombre):
        self.id = id_elemento
        self.dato1 = dato1  # Para jugadores: edad
        self.dato2 = dato2  # Para jugadores: rendimiento
        self.nombre = nombre
        self.color = 'R'
        self.izq = None
        self.der = None
        self.padre = None


class ArbolRojiNegro:
    """Árbol Rojinegro base con operaciones de inserción y balanceo"""
    def __init__(self):
        self.NIL = NodoRB(None, None, None, None)
        self.NIL.color = 'B'
        self.raiz = self.NIL

    def rotar_izquierda(self, x):
        """Rotación izquierda para balance del árbol"""
        y = x.der
        x.der = y.izq
        if y.izq != self.NIL:
            y.izq.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.izq:
            x.padre.izq = y
        else:
            x.padre.der = y
        y.izq = x
        x.padre = y

    def rotar_derecha(self, x):
        """Rotación derecha para balance del árbol"""
        y = x.izq
        x.izq = y.der
        if y.der != self.NIL:
            y.der.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.der:
            x.padre.der = y
        else:
            x.padre.izq = y
        y.der = x
        x.padre = y

    def insertar_fixup(self, z):
        """Corrige propiedades del árbol después de insertar"""
        while z.padre and z.padre.color == 'R':
            if z.padre == z.padre.padre.izq:
                y = z.padre.padre.der
                if y and y.color == 'R':
                    z.padre.color = 'B'
                    y.color = 'B'
                    z.padre.padre.color = 'R'
                    z = z.padre.padre
                else:
                    if z == z.padre.der:
                        z = z.padre
                        self.rotar_izquierda(z)
                    z.padre.color = 'B'
                    z.padre.padre.color = 'R'
                    self.rotar_derecha(z.padre.padre)
            else:
                y = z.padre.padre.izq
                if y and y.color == 'R':
                    z.padre.color = 'B'
                    y.color = 'B'
                    z.padre.padre.color = 'R'
                    z = z.padre.padre
                else:
                    if z == z.padre.izq:
                        z = z.padre
                        self.rotar_derecha(z)
                    z.padre.color = 'B'
                    z.padre.padre.color = 'R'
                    self.rotar_izquierda(z.padre.padre)
        self.raiz.color = 'B'


# ========================================================================================
# ÁRBOL PARA JUGADORES (HEREDA DE ArbolRojiNegro)
# ========================================================================================

class ArbolJugadores(ArbolRojiNegro):
    """
    Árbol que ordena jugadores por:
    1. dato2 (rendimiento) ASCENDENTE
    2. dato1 (edad) DESCENDENTE (en caso de empate)
    3. id ASCENDENTE (en caso de empate)
    """
    def insertar(self, jugador):
        """Inserta un jugador como NodoRB"""
        nodo = NodoRB(
            jugador['id'],
            jugador['edad'],        # dato1 = edad
            jugador['rendimiento'], # dato2 = rendimiento
            jugador['nombre']
        )
        nodo.izq = self.NIL
        nodo.der = self.NIL
        nodo.padre = None

        y = None
        x = self.raiz

        while x != self.NIL:
            y = x
            # Orden: rendimiento ASC -> edad DESC -> id ASC
            if (nodo.dato2 < x.dato2 or 
                (nodo.dato2 == x.dato2 and nodo.dato1 > x.dato1) or
                (nodo.dato2 == x.dato2 and nodo.dato1 == x.dato1 and nodo.id < x.id)):
                x = x.izq
            else:
                x = x.der

        nodo.padre = y
        if y is None:
            self.raiz = nodo
        elif (nodo.dato2 < y.dato2 or 
              (nodo.dato2 == y.dato2 and nodo.dato1 > y.dato1) or
              (nodo.dato2 == y.dato2 and nodo.dato1 == y.dato1 and nodo.id < y.id)):
            y.izq = nodo
        else:
            y.der = nodo

        nodo.color = 'R'
        self.insertar_fixup(nodo)

    def recorrido_inorden(self, nodo, resultado):
        """Recorrido in-orden: devuelve jugadores ordenados"""
        if nodo != self.NIL:
            self.recorrido_inorden(nodo.izq, resultado)
            resultado.append(nodo)
            self.recorrido_inorden(nodo.der, resultado)


# ========================================================================================
# FUNCIONES AUXILIARES
# ========================================================================================

def construir_arbol_jugadores(lista_jugadores):
    """Construye árbol de jugadores y devuelve nodos ordenados"""
    arbol = ArbolJugadores()
    for j in lista_jugadores:
        arbol.insertar(j)
    
    resultado = []
    arbol.recorrido_inorden(arbol.raiz, resultado)
    return resultado


# ========================================================================================
# FUNCIÓN DE PRUEBA
# ========================================================================================

def ejecutar_prueba():
    # Datos de prueba del enunciado
    jugadores_data = [
        {"id": 1, "nombre": "Sofía García", "edad": 21, "rendimiento": 66},
        {"id": 2, "nombre": "Alejandro Torres", "edad": 27, "rendimiento": 24},
        {"id": 3, "nombre": "Valentina Rodríguez", "edad": 19, "rendimiento": 15},
        {"id": 4, "nombre": "Juan López", "edad": 22, "rendimiento": 78},
        {"id": 5, "nombre": "Martina Martínez", "edad": 30, "rendimiento": 55},
        {"id": 6, "nombre": "Sebastián Pérez", "edad": 25, "rendimiento": 42},
        {"id": 7, "nombre": "Camila Fernández", "edad": 24, "rendimiento": 36},
        {"id": 8, "nombre": "Mateo González", "edad": 29, "rendimiento": 89},
        {"id": 9, "nombre": "Isabella Díaz", "edad": 21, "rendimiento": 92},
        {"id": 10, "nombre": "Daniel Ruiz", "edad": 17, "rendimiento": 57},
        {"id": 11, "nombre": "Luciana Sánchez", "edad": 18, "rendimiento": 89},
        {"id": 12, "nombre": "Lucas Vásquez", "edad": 26, "rendimiento": 82}
    ]
    
    print("=" * 70)
    print("PRUEBA: Ranking de Jugadores (Ordenamiento Global)")
    print("=" * 70)
    print("Criterio: Rendimiento ASC -> Edad DESC -> ID ASC\n")
    
    todos_ordenados = construir_arbol_jugadores(jugadores_data)
    
    print("Ranking Jugadores:")
    ids_ordenados = [nodo.id for nodo in todos_ordenados]
    print("{" + ", ".join(map(str, ids_ordenados)) + "}")
    
    print("\nDetalle completo:")
    for nodo in todos_ordenados:
        print(f"ID: {nodo.id}, {nodo.nombre}, Edad: {nodo.dato1}, Rendimiento: {nodo.dato2}")


if __name__ == "__main__":
    ejecutar_prueba()