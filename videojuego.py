"""RETO: Sistema de Matchmaking para Videojuego Online

Contexto:

Estás desarrollando el sistema de emparejamiento para un juego competitivo online. Los jugadores tienen un nivel de habilidad que va de 0 a 3000. Cuando un jugador quiere jugar, entra a una cola de espera y el sistema debe emparejarlo con otro jugador de nivel similar.

Requisitos:

Los jugadores entran a la cola con su ID y nivel 
El sistema debe emparejar jugadores cuya diferencia de nivel sea máximo 150 puntos
Si hay varios candidatos válidos, priorizar al que lleva más tiempo esperando 
Si no hay pareja disponible, el jugador permanece en la cola"""

class Jugador:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel

class SistemaMatchmaking:
    def __init__(self):
        self.cola = []

    def entrar_cola(self, jugador):
        # Buscar posible rival
        for i in range(len(self.cola)):
            rival = self.cola[i]

            if abs(jugador.nivel - rival.nivel) <= 150:
                # Emparejar
                print("Partida encontrada:")
                print("Jugador", jugador.id, "vs Jugador", rival.id)
                
                # Quitar rival de la cola
                self.cola.pop(i)
                return
        
        # Si no hay rival, se queda en la cola
        self.cola.append(jugador)
        print("Jugador", jugador.id, "entra a la cola de espera")

    def mostrar_cola(self):
        print("\nJugadores en cola:")
        for j in self.cola:
            print("ID:", j.id, "Nivel:", j.nivel)


# Crear sistema
matchmaking = SistemaMatchmaking()

# Simulación de jugadores entrando
matchmaking.entrar_cola(Jugador(1, 1200))
matchmaking.entrar_cola(Jugador(2, 1300))
matchmaking.entrar_cola(Jugador(3, 2000))
matchmaking.entrar_cola(Jugador(4, 2100))
matchmaking.entrar_cola(Jugador(5, 1250))

matchmaking.mostrar_cola()
