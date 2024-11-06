### Exercício 2. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "Essa é a aula 3 de python do bootcamp"

contagem_palavras = {}
palavras = texto.split(" ")

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] = +1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)