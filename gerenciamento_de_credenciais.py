# Lista de dicionários com as credenciais dos usuários
credenciais = [
    {"username": "usuario1", "password": "senha1"},
    {"username": "usuario2", "password": "senha2"},
    {"username": "usuario3", "password": "senha3"}
]

# Função para fazer login
def fazer_login(username, password):
    for usuario in credenciais:
        if usuario["username"] == username and usuario["password"] == password:
            return True
    return False

# Função para adicionar um novo usuário
def adicionar_usuario(username, password):
    novo_usuario = {"username": username, "password": password}
    credenciais.append(novo_usuario)

# Exemplo de uso da função de login
usuario = input("Digite seu username: ")
senha = input("Digite sua senha: ")

if fazer_login(usuario, senha):
    print("Login bem-sucedido!")
else:
    print("Login falhou. Verifique suas credenciais.")

# Exemplo de uso da função para adicionar um novo usuário
novo_usuario = input("Digite o novo username: ")
nova_senha = input("Digite a nova senha: ")

adicionar_usuario(novo_usuario, nova_senha)
print("Novo usuário adicionado com sucesso.")
