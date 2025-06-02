def verificar(palavra):
    letras = []
    n = len(palavra)
    letras = list(palavra)
    palindromo = []
    for n in range(len(palavra)):
        palindromo = letras[n] 
        n = n -1
    if palavra == palindromo:
        return print("A palavra é um palíndromo")
    else:
        return print("A palavra não é um palíndromo")
    
palavra = input("Digite uma palavra: ")    
verificar(palavra)



