import re

def avalia_forca_senha(senha):
    pontuacao = 0

    # Verifica o comprimento da senha
    if len(senha) >= 8:
        pontuacao += 2

    # Verifica se a senha contém letras maiúsculas e minúsculas
    if re.search(r'[a-z]', senha) and re.search(r'[A-Z]', senha):
        pontuacao += 2

    # Verifica se a senha contém números
    if re.search(r'\d', senha):
        pontuacao += 2

    # Verifica se a senha contém caracteres especiais
    if re.search(r'[!@#\$%\^&\*\(\)_\+=\[\]\{\};:\'",<>\./?\\|`~]', senha):
        pontuacao += 2

    return pontuacao

# Exemplo de uso:
senha = "SenhaSegura123!"
pontuacao = avalia_forca_senha(senha)
print("Pontuação da senha:", pontuacao)
