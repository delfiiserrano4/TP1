def laberinto(matriz, pos):
    matriz[pos[0]][pos[1]] = 2
    

def mover(matriz, pos):
     return matriz[pos[0]][pos[1]] == 0


mover_sendero = []  
sendero_direction = []


def fin_sendero(matriz, comienzo, final):
    laberinto(matriz, comienzo) 
    if comienzo == final: 
        mover_sendero.append(comienzo)
        return True
    
mover_direction = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]
    direction = ['↑', '↓', '←', '→']
    for i in range(4):
         next_start = (start[0] + mover_direction[i][0], comienzo[1] + mover_direction[i][1]) 
        if mover(matriz, siguiente_comienzo):  
            if fin_sendero(matriz, siguiente_comienzo, final):
                mover_sendero.append(start)
                sendero_direction.append(direction[i])  
                return True
    return False  

def gen_matriz(n, m):
  
    m += 2
    n += 2  
    maze = [[1 for i in range(n)] for j in range(m)]  
    for x in range(1, n-1):
        for y in range(1, m-1):
     if (x == 1 and y == 1) or (x == n - 2 and y == m - 2):
                matriz[x][y] = 0  
            else:
                matriz[x][y] = randint(0, 1)  
    return maze       

def print_matriz(matriz, texto ='El laberinto original es:', final1='   ', final2='\n\n', xs=0, xe=0, ys=0, ye=0):
  print(texto)
    n, m = len(matriz[0]), len(matriz)
    for x in range(xs, m-xe):
        for y in range(ys, n-ye):
            print(maze[x][y], final=final1)
        print(final=final2)  
    
def path_matriz(matriz, direcion_mapa):
    n, m = len(matriz[0]), len(matriz)
    for x in range(1, m-1):
        for y in range(1, n-1):
            matriz[x][y] = matriz[x][y] if matir[x][y] != 2 else 0 

    for x in range(m):
        for i in range(1, 2 * n - 1, 2):
            matriz[x].insert(i, '   ') 
            
            
    for x in range(1, 2 * m - 1, 2):
        matriz.insert(x, [' ', '   '] * (n-1) + [''])
        
    for direction in direcion_mapa:
        for direcion_posicion in direcion_mapa[direcion]:
            i, j = direcion_posicion
            i = 2 * i
            j = 2 * j
            if direcion == "↑":
                matriz[i - 1][j] = "↑"
            if direcion == "↓":
                maze[i + 1][j] = "↓"
            if direcion == "←":
                matriz[i][j] = " ← "
            if direcion == "→":
                matriz[i][j + 1] = " → "
    return matriz
        
def principal():
    matriz = \
        [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
     print_matriz(matriz)
    if fin_sendero(maztriz=(1, 1), final=(10, 12)):
        ms = mover_sendero[::-1]
        pd = sendero_direcion[::-1]   
        print('El orden del movimiento de coordenadas es:', [(pos[0]-1, pos[1]-1) for pos in ms])
        sendero_direcion_map = {
            '↑': [],
            '↓': [],
            '←': [],
            '→': []
        }
        
          for i in range(len(pd)):
                sendero_direcion[pd[i]].append(mp[i])
        matriz = sendero_matriz(matriz, sendero_direcion_map)
        print_matriz(matriz, textoo='El camino en movimiento del laberinto es:', final1='', final2='\n', xs=1, xe=1, ys=1, ye=1)
    else:
        print('Este laberinto no tiene solución')