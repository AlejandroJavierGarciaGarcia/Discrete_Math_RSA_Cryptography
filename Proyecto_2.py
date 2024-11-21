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

    
def main():
    print(" +--------------------------------------------+")
    print(" |              Criptografía: RSA             |")
    print(" +--------------------------------------------+\n")
    
    while True:
        print("\n +--------------------------------------------+")
        print("Generación de números primos:")
        # Solicitud de los límites
        rango_inferior = validation(" - Ingrese el límite inferior: ")
        rango_superior = validation(" - Ingrese el límite superior (mayor que el límite inferior): ")
        # Validación de rango
        if rango_superior > rango_inferior:
            generated_prime1, primes_counter = generar_primo(rango_inferior, rango_superior)
            # Validar que si se puedan generar primos para dar mensaje
            if primes_counter != 0:
                # Como se necesitan dos primos si solo hay un primo en la lista de generar primos, entonces dar mensaje para ingresar nuevo rango
                if primes_counter == 1:
                    print("\n * En el rango hay solo un primo, para RSA se necesitan dos. Ingrese otro rango.")
                elif primes_counter >= 2:
                    generated_prime2, primes_counter = generar_primo(rango_inferior, rango_superior)
                    # Verificar que los dos primos sean diferentes
                    while generated_prime1 == generated_prime2:
                        # Salir del bucle hasta que ambos primos son diferentes
                        generated_prime2, primes_counter = generar_primo(rango_inferior, rango_superior)
                    
                    print("\n * El primer número primo generado es:", generated_prime1)
                    print(" * El segundo número primo generado es:",generated_prime2)
                    break  
            else:
                print(f"\n * No se encontró un número primo en el rango {rango_inferior} a {rango_superior}. Ingrese otro rango.")
        else:
            print(" * El rango superior debe ser mayor que el rango inferior. Intente nuevamente.")


if __name__ == "__main__":
    main()


