from classes import Jugador, Equipo, Sede

j1 = Jugador("Sofía García", 21, 66)
j2 = Jugador("Alejandro Torres", 27, 24)
j3 = Jugador("Valentina Rodríguez", 19, 15)
j4 = Jugador("Juan López", 22, 78)
j5 = Jugador("Martina Martínez", 30, 55)
j6 = Jugador("Sebastián Pérez", 25, 42)
j7 = Jugador("Camila Fernández", 24, 36)
j8 = Jugador("Mateo González", 29, 89)
j9 = Jugador("Isabella Díaz", 21, 92)
j10 = Jugador("Daniel Ruiz", 17, 57)
j11 = Jugador("Luciana Sánchez", 18, 89)
j12 = Jugador("Lucas Vásquez", 26, 82)

e1 = Equipo("Futbol", [j10, j2])
e2 = Equipo("Volleyball", [j1, j9, j12, j6])
e3 = Equipo("Futbol", [j11, j8, j7])
e4 = Equipo("Volleyball", [j3, j4, j5])

s1 = Sede("Sede Cali", [e1, e2])
s2 = Sede("Sede Medellín", [e3, e4])