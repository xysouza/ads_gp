import random
import string

# Senha alvo (você pode substituir por qualquer senha que desejar)
senha_alvo = "senha123"

# Função para gerar uma senha aleatória
def gerar_senha_aleatoria(tamanho):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Tentativas para encontrar a senha correta
tentativas = 0

while True:
    tentativa = gerar_senha_aleatoria(len(senha_alvo))
    tentativas += 1

    if tentativa == senha_alvo:
        print(f"Senha encontrada: {tentativa}")
        print(f"Número de tentativas: {tentativas}")
        break