#python 3.7.1
'''

Desenvolva um diagrama que:
- Leia 4 (quatro) números;
- Calcule o quadrado de cada um;
- Se o valor resultante do quadrado do terceiro for >= 1000, imprima-o e finalize;
- Caso contrário, imprima os valores lidos e seus respectivos quadrados.

'''

print ("Nesse algoritmo iremos calcular o quadrado de quatro números e fazer o que se pede.")
primeiro_numero = int(input("Digite o primeiro número por favor:"))
primeiro_quadrado = primeiro_numero * primeiro_numero
print (f"O quadrado de {primeiro_numero} é {primeiro_quadrado}")
segundo_numero = int(input("Digite o segundo número por favor:"))
segundo_quadrado = segundo_numero * segundo_numero
print (f"O quadrado de {segundo_numero} é {segundo_quadrado}")
terceiro_numero = int(input("Digite o terceiro número por favor:"))
terceiro_quadrado = terceiro_numero * terceiro_numero
if (terceiro_quadrado) >= 1000:
    print (f"O quadrado de {terceiro_numero} é {terceiro_quadrado}")
else:    
    quarto_numero = int(input("Digite o quarto número por favor:"))
    quarto_quadrado = quarto_numero * quarto_numero
    print (f"O quadrado de {quarto_numero} é {quarto_quadrado}")