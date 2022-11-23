import random
N = int(input("Cantidad de partidas:     "))
pmaquina,pjugador,rondas = 0,0,0
while(rondas<N):
    maquina = random.randint(1,3)
    jugador = int(input("Ingrese piedra(1), papel(2) o tijera(3) :    "))
    if(jugador<1 or jugador >3):
        print("Respuesta no valida.")
    else:
        rondas+=1
        if(maquina == 1):
            print(f"Maquina = Piedra")
        elif(maquina == 2):
            print(f"Maquina = Papel")
        elif(maquina==3):
            print(f"Maquina = Tijera")

        if(maquina == jugador):
            print("Nadie gana")
        elif(maquina == 1 and jugador ==2):
            print("Jugador gana.")
            pjugador +=1
        elif(maquina == 1 and jugador == 3):
            print("Maquina gana.")
            pmaquina +=1           
        elif(maquina == 2 and jugador == 1):
            print("Maquina gana.")
            pmaquina +=1           
        elif(maquina == 2 and jugador == 3):
            print("Jugador gana.")     
            pjugador +=1                 
        elif(maquina == 3 and jugador == 1):
            print("Jugador gana.")
            pjugador+=1           
        elif(maquina == 3 and jugador == 2):
            print("Maquina gana.")
            pmaquina+=1
print(f"\nRESULTADOS\nMaquina: {pmaquina}\nJugador:   {pjugador}")
