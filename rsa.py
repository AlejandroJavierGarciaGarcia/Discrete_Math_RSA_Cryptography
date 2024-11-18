'''
Universidad del Valle de Guatemala
Matemática Discreta
Ing. Mario Castillo
'''


def mcd(a, b):
    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b 
    return b
print(" ------------------------------------------------")
print(" |                    MCD                       |")
print(" ------------------------------------------------")
a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))
print("El mdc de", a, "y", b, "es", mcd(a, b))


# Función que lee un entero positivo y valida que sea mayor que 0
def validacion(num):
    while True:
        if num.isdigit():  
            num = int(num)
            if num >=2:
                return num
            else:
                print(" * Ingrese un entero positivo.")
        else:
            print(" * Entrada inválida. Debe ingresar un número entero mayor o igual a 2.")
        
        num = input("\n - Ingrese nuevamente un número: ")


def Criba(n):
    # Lista de primos
    primes = []
    # LIstas de no primos
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

# Punto de inico del programa
print(" ------------------------------------------------")
print(" |            CRIBA DE ERATÓSTENES             |")
print(" ------------------------------------------------")
num = validacion(input(" - Introduzca un número: "))
print(" - Los primos menores o iguales a 28 son:", Criba(int(num)))




def Criba(n):
    # Lista de primos
    primes = []
    # LIstas de no primos
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

def prime_test(n):
    # Llama a funcion Criba y guarda los número primos en otro arreglo
    prime_list = Criba(int(n**0.5))
    # Verifica divisibilidad del n según la lista de primos
    for i in prime_list:
        # Si el número es divisible dentro de algún primo, entonces, es compuesto
        if n % i==0:
            print("El número ", n, " no es primo, pues lo divide ", i)
            dividers(num)
            return False
    print("El número ", n, " es primo")
    return True

def dividers(n):
    dividers = []
    prime_list = Criba(int(n))
    # Verifica divisibilidad del n según la lista de primos4
    for i in prime_list:
        # Si el número es divisible dentro de algún primo, entonces, es compuesto
        while n % i==0:
            dividers.append(i)
            n //= i

    print("  - Factorización prima:", ' x '.join(map(str, dividers)))

