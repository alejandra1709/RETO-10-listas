#Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
def ceros (lista:list)->list: #Función que recibe una lista y retorna una lista.
    cantidad_ceros=lista.count(0) #Se hace la cuenta de la cantidad de ceros que hay en la lista.
    for i in range (cantidad_ceros): #Ciclo para eliminar todos los ceros.
        lista.remove(0) #Se elimina el actual primer cero de izquierda a derecha.
    for i in range (cantidad_ceros): #Ciclo para añadir la cantidad de ceros borrada al final.
        lista.append(0) #Se añade un cero al final de la lista.
    return(lista) #Se devuelve la lista actualizada.
if __name__ == "__main__":
    lista1=[1,2,0,0,4,4,3,7,8,0,9,3,0,1,3,0,6,0,0,0,4,3,2,1,5] #Lista de 25 términos con 8 ceros.
    print("Lista inicial:",lista1) #Se imprime la lista.
    lista_nueva=ceros(lista1) #Se evalúa la función ceros con el argumento de lista 1.
    print("Lista con los ceros al final:",lista_nueva) #Se imprime la lista actualizada.
    print("---------------------------------------------------------------------------------------------------------")
    lista2=[1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,1,0] #Lista de 20 términos con 10 ceros.
    print("Lista inicial:",lista2) #Se imprime la lista.
    lista_nueva=ceros(lista2) #Se evalúa la función ceros con el argumento de lista 2.
    print("Lista con los ceros al final:",lista_nueva) #Se imprime la lista actualizada.
    print("---------------------------------------------------------------------------------------------------------")
    lista3=[6,0,0,0,8,8,4,4,0,1] #Lista de 10 términos con 4 ceros.
    print("Lista inicial:",lista3) #Se imprime la lista.
    lista_nueva=ceros(lista3) #Se evalúa la función ceros con el argumento de lista 3.
    print("Lista con los ceros al final:",lista_nueva) #Se imprime la lista actualizada.
    print("---------------------------------------------------------------------------------------------------------")
    lista4=[7,0,0,6,9] #Lista de 5 términos con 2 ceros.
    print("Lista inicial:",lista4) #Se imprime la lista.
    lista_nueva=ceros(lista4) #Se evalúa la función ceros con el argumento de lista 4.
    print("Lista con los ceros al final:",lista_nueva) #Se imprime la lista actualizada.