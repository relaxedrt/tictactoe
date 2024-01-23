#Creamos la variable del tablero
tablero = ["0","1","2","3","4","5","6","7","8","9"]

#Creamos la variable del jugador 1
p1 = "X"

#Creamos la variable del jugador 2
p2 = "O"

#Definimos la variable de victoria como un númerico
win = 0

#Creamos un contador
cont = 0 

def checkwin(player):
    if tablero[1] == player and tablero[2] == player and tablero[3] == player:
        return True
    elif tablero[1] == player and tablero[4] == player and tablero[7] == player:
        return True
    elif tablero[1] == player and tablero[5] == player and tablero[9] == player:
        return True
    elif tablero[7] == player and tablero[8] == player and tablero[9] == player:
        return True
    elif tablero[3] == player and tablero[6] == player and tablero[9] == player:
        return True
    elif tablero[4] == player and tablero[5] == player and tablero[6] == player:
        return True
    elif tablero[2] == player and tablero[5] == player and tablero[8] == player:
        return True
    elif tablero[7] == player and tablero[5] == player and tablero[3] == player:
        return True
    else:
        return False

#Que empiece el juego
while win == 0:

    #Ficha de P1
    print(f" {tablero[7]} | {tablero[8]} | {tablero[9]} ")
    print(f"-----------")
    print(f" {tablero[4]} | {tablero[5]} | {tablero[6]} ")
    print(f"-----------")
    print(f" {tablero[1]} | {tablero[2]} | {tablero[3]} ")
    print("")
    fp1 = int(input("Donde quieres colocar la ficha X? "))
    
    #Comprobamos que no este utilizado ya
    while (tablero[fp1] == p1) or (tablero[fp1] == p2):
        print("Esa casilla no esta disponible, intenta otra vez.")
        fp1 = int(input("Donde quieres colocar la ficha X? "))
    
    #Volvemos a comprobar por asegurar y asignamos el valor
    if (tablero[fp1] != p1) or (tablero[fp1] != p2):
        tablero[fp1] = p1

    if checkwin(p1) == True:
        win = 1
        break
    
    if (tablero[1] == p1 or tablero[1] == p2) and (tablero[2] == p1 or tablero[2] == p2) and (tablero[3] == p1 or tablero[3] == p2) and (tablero[4] == p1 or tablero[4] == p2) and (tablero[5] == p1 or tablero[5] == p2) and (tablero[6] == p1 or tablero[6] == p2) and (tablero[7] == p1 or tablero[7] == p2) and (tablero[8] == p1 or tablero[8] == p2) and (tablero[9] == p1 or tablero[9] == p2):
        win = 3
        break

    #Ficha de P2
    print(f" {tablero[7]} | {tablero[8]} | {tablero[9]} ")
    print(f"-----------")
    print(f" {tablero[4]} | {tablero[5]} | {tablero[6]} ")
    print(f"-----------")
    print(f" {tablero[1]} | {tablero[2]} | {tablero[3]} ")
    print("")
    fp2 = int(input("Donde quieres colocar la ficha O? "))

    #Comprobamos que no este utilizado ya
    while (tablero[fp2] == p1) or (tablero[fp2] == p2):
        print("Esa casilla no esta disponible, intenta otra vez.")
        fp2 = int(input("Donde quieres colocar la ficha O? "))
    
    #Volvemos a comprobar por asegurar y asignamos el valor
    if (tablero[fp2] != p1) or (tablero[fp2] != p2):
        tablero[fp2] = p2

    if checkwin(p2) == True:
        win = 2
        break

    if (tablero[1] == p1 or tablero[1] == p2) and (tablero[2] == p1 or tablero[2] == p2) and (tablero[3] == p1 or tablero[3] == p2) and (tablero[4] == p1 or tablero[4] == p2) and (tablero[5] == p1 or tablero[5] == p2) and (tablero[6] == p1 or tablero[6] == p2) and (tablero[7] == p1 or tablero[7] == p2) and (tablero[8] == p1 or tablero[8] == p2) and (tablero[9] == p1 or tablero[9] == p2):
        win = 3
        break

print(f" {tablero[7]} | {tablero[8]} | {tablero[9]} ")
print(f"-----------")
print(f" {tablero[4]} | {tablero[5]} | {tablero[6]} ")
print(f"-----------")
print(f" {tablero[1]} | {tablero[2]} | {tablero[3]} ")
print("")

if win == 1:
    print(f"Ganan {p1}")
elif win == 2:
    print(f"Ganan {p2}")
elif win == 3:
    print("EMPATE")