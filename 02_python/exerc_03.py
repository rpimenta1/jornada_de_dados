# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_usuario = input("Digite uma data no format dd/mm/aaaa: ")
lista_dia_mes_ano = data_usuario.split("/")
dia_usuario = lista_dia_mes_ano[0]
mes_usuario = lista_dia_mes_ano[1]
ano_usuario = lista_dia_mes_ano[2]

print(f"O dia selecinado foi: {dia_usuario}, o mes selecionado foi: {mes_usuario} e o ano selecionado foi {ano_usuario}")
