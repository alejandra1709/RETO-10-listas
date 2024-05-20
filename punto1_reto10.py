#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
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