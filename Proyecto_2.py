'''
Universidad del Valle de Guatemala
Matemática Discreta
Ing. Mario Castillo
'''
# Importaciones para procesos específicos
import random

# Función utiliza el algoritmo de Euclides para encontrar el máximo común divisor (MCD) de dos números.
def mcd(a, b):
    # Validación de casos especiales
    if b == 0:
        return abs(a)
    if a == 0:
        return abs(b)
    if(b<= 0 or a<=0):
        return 0
    # Impletemntación de lagoritmp
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b 
    return b

#a = int(input("Ingrese un entero positivo a: "))
#b = int(input("Ingrese un entero positivo b: "))
#print("El mdc de", a, "y", b, "es", mcd(a, b))

# Función genera un número primo aleatorio dentro de un rango especificado por el usuario.
def generar_primo(rango_inferior, rango_superior):
    primes_range = []
    prime_list = Criba(int(rango_superior))
    
    for i in prime_list:
        if( rango_inferior <= i <= rango_superior):
            primes_range.append(i)
    #print(primes_range)
    if primes_range: 
        return random.choice(primes_range), len(primes_range)
    else:
        return None, 0

# FUnción Criba para poder obtener una lista de números primos 
def Criba(n):
    # Lista para almacenar primos y no primos
    primes = []
    not_primes = set()
    # Recorre desde dos hasta el número aumentado en uno
    for i in range(2,n+1):
        # Verifica si i está en no primos, si ya está salta el índice
        if i in not_primes:
            continue
        # Verifica los múltiplos de i y los agrega en la lista de no primos de j hasta n
        for j in range(i*2,n+1,i):
            not_primes.add(j)
        # Después de las validaciones añade a i al array de primos
        primes.append(i)
    return primes

def validation(number):
    while True:
        num = input(number)
        if num.isdigit(): 
            num = int(num)
            if num >= 0:
                return num  
            else:
                print("\n * Ingrese un número mayor o igual a 0.")
        else:
            print("\n * Entrada inválida. Debe ingresar un número entero mayor o igual a 0.")
            

def inverso_modular(e, n):

    # Paso 1: Inicializar valores
    a, b = n, e
    t1, t2 = 0, 1  # Coeficientes iniciales

    # Paso 2: Iterar hasta que b sea 0
    while b > 0:
        # Dividir a entre b
        cociente = a // b
        
        # Actualizar restos
        a, b = b, a - cociente * b

        # Actualizar coeficientes
        t1, t2 = t2, t1 - cociente * t2

    # Paso 3: Revisar si existe inverso
    if a != 1:
        return None  # No hay inverso porque el MCD no es 1

    # Paso 4: Ajustar resultado si es negativo
    if t1 < 0:
        t1 += n

    return t1

def generar_llaves(rango_inferior, rango_superior):
    # Paso 1: Generar los dos números primos
    print("Generando números primos...")
    primo1 = generar_primo(rango_inferior, rango_superior)[0]
    primo2 = generar_primo(rango_inferior, rango_superior)[0]
    
    print(f"Números primos generados: {primo1}, {primo2}")
    
    # Asegurarse de que los dos números primos sean diferentes
    while primo1 == primo2:
        print(f"Los números primos generados son iguales ({primo1}), buscando otro primo...")
        primo2 = generar_primo(rango_inferior, rango_superior)[0]
    
    # Calculamos n y φ(n)
    n = primo1 * primo2
    phi = (primo1 - 1) * (primo2 - 1)
    print(f"Valores calculados: n = {n}, φ(n) = {phi}")

    # Elegimos un número e que sea coprimo con φ(n)
    e = None
    for i in range(2, phi):
        if mcd(i, phi) == 1:
            e = i
            break

    if e is None:
        print("No se encontró un valor adecuado para e.")
        return None

    print(f"Valor elegido para e: {e}")

    # Calculamos el inverso modular de e
    d = inverso_modular(e, phi)
    if d is None:
        print("No se pudo calcular el inverso modular de e.")
        return None

    print(f"Valor calculado para d: {d}")

    # Validamos que la llave pública y privada sean diferentes
    if e == d:
        print("e y d son iguales. No se puede generar un par de llaves válido.")
        return None

    # Finalmente retornamos la llave pública y privada
    llave_publica = (e, n)
    llave_privada = (d, n)
    print("Llaves generadas exitosamente.")
    return llave_publica, llave_privada


    
def main():
    print(" +--------------------------------------------+")
    print(" |              Criptografía: RSA             |")
    print(" +--------------------------------------------+\n")
    
    while True:
        print("\n +--------------------------------------------+")
        print("Seleccione una opción:")
        print("1. Generar números primos")
        print("2. Generar claves RSA")
        print("3. Salir")
        
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            print("\nGeneración de números primos:")
            rango_inferior = validation(" - Ingrese el límite inferior: ")
            rango_superior = validation(" - Ingrese el límite superior (mayor que el límite inferior): ")
            
            if rango_superior > rango_inferior:
                generated_prime1, primes_counter = generar_primo(rango_inferior, rango_superior)
                if primes_counter != 0:
                    if primes_counter == 1:
                        print("\n * En el rango hay solo un primo, para RSA se necesitan dos. Ingrese otro rango.")
                    elif primes_counter >= 2:
                        generated_prime2, primes_counter = generar_primo(rango_inferior, rango_superior)
                        while generated_prime1 == generated_prime2:
                            generated_prime2, primes_counter = generar_primo(rango_inferior, rango_superior)
                        
                        print("\n * El primer número primo generado es:", generated_prime1)
                        print(" * El segundo número primo generado es:", generated_prime2)
                else:
                    print(f"\n * No se encontró un número primo en el rango {rango_inferior} a {rango_superior}. Ingrese otro rango.")
            else:
                print(" * El rango superior debe ser mayor que el rango inferior. Intente nuevamente.")
        
        elif opcion == "2":
            print("\nGeneración de claves RSA:")
            rango_inferior = validation(" - Ingrese el límite inferior: ")
            rango_superior = validation(" - Ingrese el límite superior (mayor que el límite inferior): ")
            
            if rango_superior > rango_inferior:
                llaves = generar_llaves(rango_inferior, rango_superior)
                if llaves:
                    llave_publica, llave_privada = llaves
                    print("\n * Clave pública generada: ", llave_publica)
                    print(" * Clave privada generada: ", llave_privada)
                else:
                    print("\n * No se pudieron generar las claves. Intente con otro rango.")
            else:
                print(" * El rango superior debe ser mayor que el límite inferior. Intente nuevamente.")
        
        elif opcion == "3":
            print("\nGracias por usar el programa. ¡Hasta luego!")
            break
        
        else:
            print("\n * Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()


