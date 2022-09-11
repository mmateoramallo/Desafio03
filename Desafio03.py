import Soporte as soporte
import collections

def create_array():
    # Creamos el array
    v = soporte.vector_unknown_range(300000)
    return v


def main():
    # Crear Arreglos
    num = []
    cont = []
    # Vamos a obtener el arreglo creado con la funcion vector_unkown_range
    v = create_array()
    #Variables
    pos = None
    mayor_valor = 0
    #Recorreria todo el vector v
    for i in range(len(v)):
        pass
    #Usamos la libreria collections, tenemos un diccionario con los numeros que se repiten y la cantidad de veces que se repiten
    v_dict = collections.Counter(v)
    #En este punto obtenemos las llaves del diccionario de la linea pasada para contar la cantidad que son
    v_dict_d = v_dict.keys()
    #En estas lineas contamos la cantidad distintas de llaves que hay, es decir la cantidad de numeros que se repiten
    cont_frec = 0
    for i in range(len(v_dict_d)):
        cont_frec += 1

    print(len(v_dict_d))
    print(cont_frec)
    print()

    #Buscamos el valor modal del array v_dict, dado que este es un diccionario que tiene de valor en la clave a la cantidad de veces que se repite la key de number, de vuelta tengo que acceder al diccionario de numeros repetidos y cantidad de veces que se repitio
    



if __name__ == "__main__":
    main()
    