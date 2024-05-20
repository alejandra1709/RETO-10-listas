#Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
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
