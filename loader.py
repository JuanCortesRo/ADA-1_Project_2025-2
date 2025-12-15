from classes import Jugador, Equipo, Sede

def cargar_desde_archivo(path):
    ns = {"Jugador": Jugador, "Equipo": Equipo, "Sede": Sede}
    
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    exec(code, ns)

    jugadores = [v for v in ns.values() if isinstance(v, Jugador)]
    equipos = [v for v in ns.values() if isinstance(v, Equipo)]
    sedes = [v for v in ns.values() if isinstance(v, Sede)]

    jug_dicts = []
    for idx, j in enumerate(jugadores, 1):
        jug_dicts.append({
            "id": idx,
            "nombre": j.nombre,
            "edad": j.edad,
            "rendimiento": j.rendimiento,
        })

    return jug_dicts, equipos, sedes