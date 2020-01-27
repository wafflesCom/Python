vocal = ['A','E','I','O','U','a','e','i','o','u']
numero = [12,10,1,5]
lista = ['a', 2]
def maxi(a, b):
    if(a>b):
        print(a)
    else:
        print(b)

def maxi_tres(a,b,c):
    if (a>b and a>c):
        print(a)
    elif(b>c and b>a):
        print(b)
    else:
        print(c)

def cadena(chain):
    i= 0
    for x in chain:
        i += 1
    print(i)

def carac(chain):
    for x in chain:
        if(x in vocal):
            print(True)
        else:
            print(False)

def suma(lista):
    suma = 0
    for x in lista:
        suma += x
    print(suma)

def revez(chain):
    cadenaInvertida = chain[::-1]
    print(cadenaInvertida)

def palindromo(chain):
    palin = chain[::-1]
    if(palin in chain):
        print(True)
    else:
        print(False)

def superposicion(lista, numero):
    bandera = False
    for x in lista:
        for y in numero:
            if(y == x):
                bandera = True
    print(bandera)

def caracter_n():
    letra = input("ingrese un caracter:")
    num = int(input("Cuantas veces quieres que se repita:"))
    out = letra * num
    print(out)

def histograma(numero):
    for x in numero:
        cadena = '*' * x
        print(cadena)

"""


"""
a = int(input("dame numero:"))
b = int(input("dame otro numero:"))
c = int(input("dame otro numero:"))
chain= input("Escribe una palabra:")
print("comparación dos numeros")
maxi(a,b)
print("conparación tres numeros")
maxi_tres(a,b,c)
print("Tamaño de la cadena")
cadena(chain)
print("comparación de los caracteres")
carac(chain)
print("suma los numeros de una arreglo predeterminado")
suma(numero)
print("muestra la cadena ingresada al revez")
revez(chain)
print("muestra si la cadena es un palindromo")
palindromo(chain)
print("indica si hay un solo elemento de una lista en otra lista")
superposicion(numero, vocal)
print("repite caracter n veces")
caracter_n()
histograma(numero)
