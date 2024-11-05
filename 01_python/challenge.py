BONUS_CONSTANT = 1000
name = input("Write your name: ")
salary = float(input("Write your salary (only numbers allowed: "))
bonus = float(input("Write your bonus (only numbers - example 1.5): "))

bonus_value = BONUS_CONSTANT + salary * bonus
print(f"The user {name} have a total bonus of {bonus_value}")