# Clases para interpretar los inputs del proyecto
class Jugador:
    def __init__(self, nombre, edad, rendimiento):
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento


class Equipo:
    def __init__(self, deporte, jugadores):
        self.deporte = deporte
        self.jugadores = jugadores  

class Sede:
    def __init__(self, nombre, equipos):
        self.nombre = nombre
        self.equipos = equipos
