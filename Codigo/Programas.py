import random   #Importamos libreria

Nombre = str(input("Introduce tu nombre: ")) #Str de string, Input para entradas de teclado

print("-----------------------")
NUM1 = int(input("Introduce un numero entero: ")) #int para un entero
NUM2 = int(input("Introduce otro numero entero: "))
NUM3 = int(input("Introduce otro numero entero: "))
SUMA = NUM1 + NUM2 + NUM3                               #Se realiza la suma de los numeros obtenidos
print("-----------------------")

print(f"Tu nombre es: {Nombre}")                        #  1) Se imprime el nombre escrito por el usuario
print("-----------------------")
print(f"El resultado de la suma de los tres numeros es: {SUMA}")        # 2) se imprime el resultado de la suma
print("-----------------------")

#####################################################

for v in range(1,11,1):         #3) "FOR" v se repetira hasta qe se cpmplete el ciclo e ira sumando 1
    print("Numero: ",v)


#####################################################
print("-----------------------")

if NUM1 > 0 and NUM2 > 0:       # 4) "AND" si num1 es mayor que 0 y num2 es mayor que 0
	print("los numeros son mayores que 0")      #se imprime 

if NUM1 > 0 and NUM2 > 0 and NUM3 > 0:
	print("los numeros son mayores que 0")      #si num1, num2 y num3 son mayores que 0 se imprime este mensaje

else:
	print("al menos un numero no es mayor que 0")   #si uno no es mayor se imprime este mensaje
	
#####################################################
print("-----------------------")	

if NUM1 > 0 or NUM2 > 0:                                    # 5) "OR"
	print("cualquiera de los nuneros es mayor que 0")       #si hay almenos un numero mayor a 0 se imprime este mensaje
else:
    print("Ninguno de los numeros son mayores que 0")       #si ninguno lo es se imprime este

if NUM2 > 0 or NUM3 > 0:
	print("Cualquiera de los numeros es mayor que 0")       #si hay almenos un numero mayor a 0 se imprime este mensaje

else:
	print("Ninugno de los numeros es mayor que 0")          #si ninguno lo es se imprime este
#####################################################
print("-----------------------")

a = []                                                      #6) "NOT"

if not a:
    print("la lista esta vacia")
else: print(a)
#####################################################
print("-----------------------")


intentos = 0                                                #7) Escoger numero aleatorio

NUMR = random.randint(1, 20)

print(f"Bueno hora de un juego {Nombre}, estoy pensando en un numero del 1 al 20")

while intentos < 6:                                         # Mientras no gaste los 6 intentos podra seguir jugando
    print("Intenta adivinar: ")
    estimacion = input()
    estimacion = int(estimacion)

    intentos = intentos + 1                                 #si falla se acaban los intentos
    
    if estimacion < NUMR:                                   #Si el numero dado es menor que el numero al azar da el siguiente mensaje
        print("Tu estimación es muy baja.")

    if estimacion > NUMR:                                   #Si el numero dado es mayor que el numero al azar da el siguiente mensaje
        print("Tu estimación es muy alta")

    if estimacion == NUMR:
        break

if estimacion == NUMR:
    intentos = str(intentos)                                #Si el numero dado es igual al numero al azar gana y se muesrtra este mensaje
    print(f"Felicidades {Nombre} has adivinado el numero en {intentos} intentos!!")

if estimacion != NUMR:                                      #Si se le acabaron los intentos y no adivino, se muestra este mensaje
    NUMR = str(NUMR)
    print(f"El numero que estaba pensando era: {NUMR}")





