#Desarrollar una función que permita convertir un número romano en un número decimal.


romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 100} #Hacemos uso del diccionario para saber que letra representa cada decimal
    
def romanoEntero(romano):
    if(len(romano) == 1):
        return romanos[romano]
    else:
        if(romanos[romano[0]]) >= (romanos[romano[1]]):
            return (romanos[romano[0]]) + romanoEntero((romano[1:]))
        else:
            return (- romanos[romano[0]]) + romanoEntero(romano[1:])    
        
    

print(romanoEntero('CXXIII'))


