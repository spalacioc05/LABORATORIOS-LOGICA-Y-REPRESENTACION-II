from collections import defaultdict
from tabulate import tabulate

class Trabajador:
    def __init__(self, nombre, habilidades, disponibilidad):
        self.nombre = nombre
        self.habilidades = set(habilidades)
        self.disponibilidad = disponibilidad
        self.horasAsignadas = 0

class Turno:
    def __init__(self, habilidadesRequeridas, duracion, prioridad):
        self.habilidadesRequeridas = habilidadesRequeridas
        self.duracion = duracion
        self.prioridad = prioridad

def asignarTurnos(trabajadores, turnos):
    # Ordenar turnos por prioridad (mayor prioridad primero)
    turnos.sort(key=lambda x: x.prioridad, reverse=True)
    
    # Se almacena la mejor asignación
    dp = defaultdict(lambda: float('-inf'))
    dp[0] = 0  # Caso base: ningún turno asignado, ninguna hora trabajada
    
    # Seguimiento
    mejorAsignacion = {}
    
    for turno in turnos:
        nuevoDP = dp.copy()
        
        for estado, valor in dp.items():
            for trabajador in trabajadores:
                if trabajador.habilidades >= set(turno.habilidadesRequeridas) and trabajador.disponibilidad - trabajador.horasAsignadas >= turno.duracion:
                    nuevoEstado = estado | (1 << turnos.index(turno))
                    nuevoValor = valor + turno.prioridad
                    
                    if nuevoValor > nuevoDP[nuevoEstado]:
                        nuevoDP[nuevoEstado] = nuevoValor
                        mejorAsignacion[nuevoEstado] = (trabajador, turno)
                        trabajador.horasAsignadas += turno.duracion
        dp = nuevoDP
    
    # Mejor asignación
    maxEstado = max(dp, key=dp.get)
    asignacion = []
    
    while maxEstado:
        trabajador, turno = mejorAsignacion[maxEstado]
        asignacion.append((trabajador.nombre, turno.habilidadesRequeridas, turno.duracion))
        maxEstado &= ~(1 << turnos.index(turno))
    
    return asignacion


trabajadores = [
    Trabajador("Santiago", ["soldadura", "ensamblaje"], 40),
    Trabajador("Sarai", ["control de calidad", "ensamblaje"], 40),
    Trabajador("Sarah", ["soldadura", "control de calidad"], 40),
    Trabajador("Angelo", ["soldadura", "ensamblaje", "control de calidad"], 40),
    Trabajador("Victor", ["ensamblaje"], 40),
    Trabajador("Susana", ["control de calidad"], 40)
]

turnos = [
    Turno(["soldadura", "ensamblaje"], 8, 3),
    Turno(["control de calidad"], 4, 2),
    Turno(["ensamblaje"], 6, 1),
    Turno(["soldadura"], 5, 4),
    Turno(["ensamblaje", "control de calidad"], 7, 5),
    Turno(["soldadura", "control de calidad"], 6, 3),
    Turno(["ensamblaje"], 4, 2),
    Turno(["control de calidad"], 3, 1)
]

asignacion = asignarTurnos(trabajadores, turnos)

tabla = [["Trabajador", "Habilidades Requeridas", "Duración (horas)"]]

for a in asignacion:
    tabla.append([a[0], ", ".join(a[1]), a[2]])

print(tabulate(tabla, headers="firstrow", tablefmt="grid"))