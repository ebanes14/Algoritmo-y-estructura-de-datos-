mochi = ['E-11','E-22', 'DLT-19','A280','sable de luz']


cont = [0]


def usarLaFuerza(vec,sableDeLuz,cont):
    if (len(vec) == 1) and ((vec[0]) == sableDeLuz):
        print('La unica arma de la mochila es el sable de luz')
    else:
        if (vec[0] == sableDeLuz):
            print('Encontramos el sable de luz!')
        else:
            cont[0] += 1
            return usarLaFuerza(vec[1:], sableDeLuz, cont)



usarLaFuerza(mochi,'sable de luz', cont)
print('Se retiraron ',cont,' objetos para encontrar el sable de luz en la mochila')
