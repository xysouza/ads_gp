import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits 
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso:
tamanho_da_senha = 12
senha_gerada = gerar_senha(tamanho_da_senha)
print("Senha gerada:", senha_gerada)
