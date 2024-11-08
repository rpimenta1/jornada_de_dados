# Inicializa a constante de bônus
BONUS_CONSTANT = 1000

# Dicionário para armazenar o cadastro
cadastros = {}

# Função para cadastrar um usuário
def cadastro(user_id: int):
    nome_valido = False
    salario_valido = False
    bonus_valido = False

    # Loop para verificar o nome
    while not nome_valido:
        try:
            nome = input("Digite seu nome: ")
            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                print("Nome válido:", nome)
                nome_valido = True
        except ValueError as e:
            print(e)

    # Loop para verificar o salário
    while not salario_valido:
        try:
            salario = float(input("Digite o valor do seu salário: "))
            if salario < 0:
                print("Por favor, digite um valor positivo para o salário.")
            else:
                salario_valido = True
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")

    # Loop para verificar o bônus
    while not bonus_valido:
        try:
            bonus = float(input("Digite o valor do bônus recebido (em %): "))
            if bonus < 0:
                print("Por favor, digite um valor positivo para o bônus.")
            else:
                bonus_valido = True
        except ValueError:
            print("Entrada inválida para o bônus. Por favor, digite um número.")

    # Calcula o bônus final
    bonus_recebido = BONUS_CONSTANT + (salario * (bonus / 100))
    
    # Salva os dados no dicionário
    cadastros[user_id] = {
        'Nome': nome,
        'Salario': salario,
        'Bonus Recebido': bonus_recebido
    }
    
    # Exibe as informações cadastradas
    print(f"\n{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
    print("\nCadastro salvo com sucesso!\n")

# Realiza um único cadastro e exibe o resultado
user_id = 1
cadastro(user_id)

# Exibe o cadastro realizado
print("\nCadastro realizado:")
for user_id, dados in cadastros.items():
    print(f"ID {user_id}: {dados}")
