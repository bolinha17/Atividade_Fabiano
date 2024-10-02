def saudacao(nome):
    print(f"Olá {nome}!")
saudacao('jonata')

#############################################

def soma(a, b):
    return a + b
resultado = soma(10,5)
print(resultado)

##############################################

#Criar uma função que calcule a média de três números e retorne o resultado.

def media(a,b,c):
    return (a+b+c)/3
result = media(2,8,9)
print(result)

#############################################

#Maior ou menor de idade.

def idade_filtro(idade):
    if idade >= 18:
        resultado = (f"A idade {idade} é maior que 18!")
    else:
        resultado = (f"A idade {idade} é menor que 18!")
    return resultado
print(idade_filtro(25))

##############################################

