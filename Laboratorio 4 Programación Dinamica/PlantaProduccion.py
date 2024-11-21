from collections import defaultdict


class Trabajador:
    def __init__(self, nombre, habilidades, disponibilidad):
        self.nombre = nombre
        self.habilidades = set(habilidades)
        self.disponibilidad = disponibilidad
        self.horas_asignadas = 0


class Turno:
    def __init__(self, habilidades_requeridas, duracion, prioridad):
        self.habilidades_requeridas = habilidades_requeridas
        self.duracion = duracion
        self.prioridad = prioridad


def asignar_turnos(trabajadores, turnos):
    # Ordenar turnos por prioridad (mayor prioridad primero)
    turnos.sort(key=lambda x: x.prioridad, reverse=True)

    # Tabla DP para almacenar la mejor asignación
    dp = defaultdict(lambda: float('-inf'))
    dp[0] = 0  # Caso base: ningún turno asignado, ninguna hora trabajada

    # Seguimiento de la mejor asignación
    mejor_asignacion = {}

    for turno in turnos:
        nuevo_dp = dp.copy()
        for estado, valor in dp.items():
            for trabajador in trabajadores:
                if trabajador.habilidades >= set(
                        turno.habilidades_requeridas) and trabajador.disponibilidad - trabajador.horas_asignadas >= turno.duracion:
                    nuevo_estado = estado | (1 << turnos.index(turno))
                    nuevo_valor = valor + turno.prioridad
                    if nuevo_valor > nuevo_dp[nuevo_estado]:
                        nuevo_dp[nuevo_estado] = nuevo_valor
                        mejor_asignacion[nuevo_estado] = (trabajador, turno)
                        trabajador.horas_asignadas += turno.duracion
        dp = nuevo_dp

    # Extraer la mejor asignación
    max_estado = max(dp, key=dp.get)
    asignacion = []
    while max_estado:
        trabajador, turno = mejor_asignacion[max_estado]
        asignacion.append((trabajador.nombre, turno.habilidades_requeridas, turno.duracion))
        max_estado &= ~(1 << turnos.index(turno))

    return asignacion


# Ejemplo de uso
trabajadores = [
    Trabajador("Alicia", ["soldadura", "ensamblaje"], 40),
    Trabajador("Roberto", ["control_calidad", "ensamblaje"], 40),
    Trabajador("Carlos", ["soldadura", "control_calidad"], 40)
]

turnos = [
    Turno(["soldadura", "ensamblaje"], 8, 3),
    Turno(["control_calidad"], 4, 2),
    Turno(["ensamblaje"], 6, 1)
]

asignacion = asignar_turnos(trabajadores, turnos)
for a in asignacion:
    print(f"Trabajador {a[0]} asignado al turno que requiere {a[1]} por {a[2]} horas")