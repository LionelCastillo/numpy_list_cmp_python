from ast import While
import random

from pyparsing import White
# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''
def blackjack():
    nombre = str(input('ingrese su nombre: '))

    numeros = [random.randint(1,10) for x in range(2)]

    while sum(numeros) < 21:
        print(nombre, 'tus numeros son: ', numeros)
        opcion = str(input('si desea recibir mas cartas ingrese SI en otro caso ingrese NO: '))
        if opcion == 'SI':
            numeros.append(random.randint(1,10))
        elif opcion == 'NO': 
            break
        else:
            print('elige una de las dos opciones, SI o NO') 

    print(nombre, 'tus numeros son: ', numeros)

    if sum(numeros) > 21:
        print('Has perdido')
        resultado = {'puntaje': 0, 'jugador': nombre}       
        return resultado

    resultado = {'puntaje': sum(numeros), 'jugador': nombre}        
    return resultado

if __name__ == '__main__':
    print("Ahora sí! buena suerte :)")
    
    print('Ingrese la cantidad de jugadores')

    numero_jugadores = int(input())    

    jugadores = [blackjack() for x in range(numero_jugadores)]

    jugadores.sort(reverse=True, key=lambda x: x['puntaje'])

    [print ('*' ,end='') for x in range(45)]
    print('')
    print('Ranking!! :D')
    [print ('*' ,end='') for x in range(45)]
    print('')
    [print('jugador >', x.get('jugador'),'puntaje:', x.get('puntaje')) for x in jugadores]
    [print ('*' ,end='') for x in range(45)]
    print('')
    ranking = [x.get('puntaje') for x in jugadores]

    if numero_jugadores > 1:

        if ranking[1] == ranking[0]:
            print('Empate!')

        elif sum(ranking) == 0:
            print('Perdedores!')

        else:
            winner = [x.get("jugador") for x in jugadores if x.get('puntaje') == ranking[0]]
            print('Ganó', winner[0], '!!')

    elif numero_jugadores == 0:
        print('Volvé otro día entonces...')

    else:
        if ranking[0] > 0:
           player = [x.get("jugador") for x in jugadores if x.get('puntaje') == ranking[0]]
           print('Ganaste', player[0], '!!')

        else:
           player = [x.get("jugador") for x in jugadores if x.get('puntaje') == ranking[0]]
           print('Perdiste', player[0], '!!')

    print("terminamos")