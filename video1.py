def fatores_primos(numero):
    fator = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            fator.append(divisor)
            numero = numero // divisor
        else:
            divisor += 1
    return print(fator)

numero = int(input("digite um numero inteiro: "))
fatores_primos(numero)
