#prueba

print("Programa que usa el algoritmo de warshall para hacer el cierre transitivo de una relacion")
print()
v=int(input("Introduce la cantida de vertices de tu grafo: "));
print()
#ahora lo que vamos a hacer es por defecto pedir los valores de la matriz para poder ejecutarla.
Ma1=[]#declaramos la matriz para poder usarla mas adelante
Ma2=[]# la seguna matriz que me da el volumen
for i in range(v):
    Ma1.append([])

#ACA YA CREE LA MATRIZ NECESARIA PARA PODER TRABAJAR
var1=0
var2=0
count1=0
a=0
while a<4:
    var1=var1+1
    for i in range(v):
        var2=i+1
        print("Fila ",var1)
        print("Introduce el numero de la columna ", var2)
        b=int(input(": "))
        Ma1[count1].append(b)
    a=a+1
    count1=count1+1



for k in range(v):
    for i in range(v):
        for j in range (v):
        Ma1[i][j]=Ma1[i][j] or (Ma1[i][k] and Ma1[k][j]) #para acceder o hacer slicing es necesario porner los dos corchetes
print("El resultado del cierre transitivo es el siguiente: ")
print()
for i in range(v):
    print(Ma1[i])
    print()
