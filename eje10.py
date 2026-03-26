def es_primo(numero):

    if numero < 2:
        return False
    
    if numero == 2:
        return True
    
    if numero % 2 == 0:
        return False
    
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    
    return True


# Ejemplo de uso
numero = int(input("Ingresa un número: "))
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")