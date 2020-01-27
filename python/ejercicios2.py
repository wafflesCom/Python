lista = [1,5,6,8,2,4]
cadenas = ["hola","perras","parangaricutirimicuaro"]
def mayor_lista(lista):
    x = 0
    for i in lista:
        if(i > x):
            x = i
    return x

def larga(cadenas):
    x = 0
    y = 0
    for i in cadenas:
        x = len(i)
        if(x > y):
            y = x
            palabra = i
    return palabra

def filtrar_palabras(dame):
    n = int(input("dame un numero:"))
    x = 0
    for i in dame:
        x = len(i)
        if(x >= n):
            pal = i
            print(pal)

def contar_mayus(chain):
    x = 0
    for i in chain:
        num = ord(i)
        if(num >= 65 and num <= 90):
            x += 1
    print(x)
   
def binario(en):
    for x in en:
        bina = ''
        while x // 2 != 0:
            bina = str(x%2) + bina
            x = x // 2
        print(str(x)+bina)
        x = 0

def edad():
    edad= []
    i = 0
    actual = int(input("año en curso"))
    for i in range(3):
        year_born = int(input("año en el que nacio una persona"))
        edad.append(year_born)

    for x in edad:
        exacta = actual - x
        print("esta persona tiene ", exacta)
        
"""

"""
print("Muestra el numero mayor alojado en una lista", "\n", mayor_lista(lista))
print("Muestra la cadena más larga alojada en una lista","\n", larga(cadenas))
print("Muestra la cadena que tenga más caracteres que n")
filtrar_palabras(cadenas)
print("Muestra cuantas mayúsculas hay en una cadena")
chain = input("Escribe algo:")
contar_mayus(chain)
binario(lista)
edad()
