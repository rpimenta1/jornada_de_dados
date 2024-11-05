# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math


raio = float(input("Digite o valor do raio: "))
area_circulo = math.pi*raio**2
print(f"{area_circulo:.2f}")