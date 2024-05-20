# RETO 10 - listas
>***1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.***
```python
def prom(arreglo:list)->float: #Función para hallar el promedio, recibe una lista y devuelve un float.
    suma:float=0 #Se inicia variable suma en 0.
    for i in arreglo: #For para recorrer el arreglo.
        suma+=i #Se va sumando cada término de la lista a suma.
    promedio=suma/len(arreglo) #El promedio es la suma de todos los números del arreglo, dividida entre la longitud del arreglo.
    return promedio #Se devuelve el promedio.
if __name__ == "__main__":
    a=float(input("Ingrese un número para el arreglo: "))
    b=float(input("Ingrese un número para el arreglo: "))
    c=float(input("Ingrese un número para el arreglo: "))
    d=float(input("Ingrese un número para el arreglo: "))
    e=float(input("Ingrese un número para el arreglo: "))
    f=float(input("Ingrese un número para el arreglo: "))
    g=float(input("Ingrese un número para el arreglo: "))
    h=float(input("Ingrese un número para el arreglo: "))
    i=float(input("Ingrese un número para el arreglo: "))
    j=float(input("Ingrese un número para el arreglo: "))
    arreglo = [a,b,c,d,e,f,g,h,i,j] #Arreglo de 10 términos.
    arreglo2 = [a,c,e,g,i] #Arreglo de 5 términos
    arreglo3 = [a,j] #Arreglo de 2 términos (Para probar que sirve con arreglos de diferente tamaño).
    promedio=prom(arreglo) #Se evalúa el promedio del arreglo por medio de la función prom a la cual se le envía la lista como argumento.
    print("------------------------------------------------------------")
    print("Arreglo:",arreglo)#Se imprime la lista y el promedio.
    print("Promedio:",promedio)
    print("------------------------------------------------------------")
    promedio2=prom(arreglo2) 
    print("Arreglo:",arreglo2)
    print("Promedio:",promedio2)
    print("------------------------------------------------------------")
    promedio3=prom(arreglo3)
    print("Arreglo:",arreglo3)
    print("Promedio:",promedio3)
```
>***2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.***
```python
def producto_punto (lista1:list,lista2:list)->int: #Función para hallar el producto punto, recibe dos listas y devuelve un entero.
    p_p=0 #Se inicia variable en 0.
    for i in range(len(lista1)): #Ciclo for en el que i empieza en 0 y aumenta de uno en uno hasta llegar al tamaño de la lista (puede ser cualquiera porque tienen igual longitud).
        p_p+=(lista1[i]*lista2[i]) #Se suma a p_p el producto de los números en la posición i de cada lista.
    return p_p #Se retorna el valor de la variable p_p.
if __name__ == "__main__":
    a1=int(input("Ingrese un número para el primer arreglo: ")) #Se solicitan números para los arreglos.
    a2=int(input("Ingrese un número para el primer arreglo: "))
    a3=int(input("Ingrese un número para el primer arreglo: "))
    a4=int(input("Ingrese un número para el primer arreglo: "))
    a5=int(input("Ingrese un número para el primer arreglo: "))
    a6=int(input("Ingrese un número para el primer arreglo: "))
    a7=int(input("Ingrese un número para el primer arreglo: "))
    a8=int(input("Ingrese un número para el primer arreglo: "))
    b1=int(input("Ingrese un número para el segundo arreglo: "))
    b2=int(input("Ingrese un número para el segundo arreglo: "))
    b3=int(input("Ingrese un número para el segundo arreglo: "))
    b4=int(input("Ingrese un número para el segundo arreglo: "))
    b5=int(input("Ingrese un número para el segundo arreglo: "))
    b6=int(input("Ingrese un número para el segundo arreglo: "))
    b7=int(input("Ingrese un número para el segundo arreglo: "))
    b8=int(input("Ingrese un número para el segundo arreglo: "))
    a=[a1,a2,a3,a4,a5,a6,a7,a8] #Dos arreglos de igual tamaño.
    b=[b1,b2,b3,b4,b5,b6,b7,b8]
    print("El primer arreglo es:",a) #Se imprimen ambos arreglos
    print("El segundo arreglo es:",b)
    p_pt=producto_punto(a,b) #Se evalúa la función producto punto con las listas a y b como argumentos y el valor retornado se guarda en p_pt.
    print("Su producto punto es:",p_pt) #Se imprime el producto punto
    print("------------------------------------------------") #Línea divisora para probar con otras dos listas ahora de menor tamaño.
    a_a=[a1,a3,a5,a7]
    b_b=[b2,b4,b6,b8]
    print("El primer arreglo es:",a_a)
    print("El segundo arreglo es:",b_b)
    p_pt=producto_punto(a_a,b_b)
    print("Su producto punto es:",p_pt)
```
>***3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.***
```python
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
```
