matriz_Laberinto = [['1','9','9','9','9','9',],
                    ['1','1','9','1','9','9'],
                    ['9','1','1','1','9','9'],
                    ['9','1','9','9','9','9'],
                    ['9','1','1','1','1','F']]

def laberinto(matriz, x, y, resultado = []):
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 'F'):
            verdad = True
            resultado.append([x,y])
            print('Lograste salir del laberinto con exito')
            print('La posicion final en el laberinto es: ', resultado)
        else:
            if(matriz[x][y] == '1'):
                matriz[x][y] = 'c'
                laberinto(matriz, x, y+1, resultado)
                laberinto(matriz, x, y-1, resultado)
                laberinto(matriz, x-1, y, resultado)
                laberinto(matriz, x+1, y, resultado)
                matriz[x][y] = 1


laberinto(matriz_Laberinto,0,0)