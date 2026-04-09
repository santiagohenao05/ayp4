class Paciente:
    def __init__(self, nombre, prioridad):
        self.nombre= nombre
        self.prioridad= prioridad
    
    def __lt__(self, otro):
        return self.prioridad < otro.prioridad
class Hospital:
    def __init__(self):
        self.pacientes= []
    
    def agregar_paciente(self, paciente):
        heapq.heappush(self.pacientes, paciente)
    
    def siguiente_paciente(self):
        if not self.pacientes:
            return None
        return heapq.heappop(self.pacientes)
hospital= Hospital()
#debo agrgar yo los nombres y prioridades de los pacientes para probar el programa
hospital.agregar_paciente(Paciente("Juan", 2))
hospital.agregar_paciente(Paciente("Maria", 1)) 
hospital.agregar_paciente(Paciente("Pedro", 3))
hospital.agregar_paciente(Paciente("Juan", 1))
siguiente= hospital.siguiente_paciente()
print(f"Siguiente paciente a atender: {siguiente.nombre} con prioridad {siguiente.prioridad}")
siguiente= hospital.siguiente_paciente()
print(f"Siguiente paciente a atender: {siguiente.nombre} con prioridad {siguiente.prioridad}")