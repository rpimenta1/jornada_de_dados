BONUS_CONSTANT = 1000
# Solicita o nome ao usuario
try:
    name = input("Write your name: ")
    if len(name) == 0:
        raise ValueError("O nome não pode estar vazio")
    elif any(char.isdigit() for char in name):
        raise ValueError("O nome não deve conter numeros")
except ValueError as e:
    print(e)

#Solicita o valor do salario ao usuario
try:
    salary = float(input("Write your salary (only numbers allowed): "))
    if salary <= 0:
        print("O valor digitado não pode ser menor nem igual a 0")
except ValueError:
    print("Entrada inválida para o campo salário, favor reveja o valor inputado")

#Solicitado o bonus ao usuario
try:
    bonus = float(input("Write your bonus (only numbers - example 1.5): "))
    if bonus <= 0:
        print("O valor digitado não pode ser menor nem igual a 0")
except ValueError:
    print("Entrada inválida para o campo bonus, favor reveja o valor inputado")

bonus_value = BONUS_CONSTANT + salary * bonus
print(f"The user {name} have a total bonus of {bonus_value}")