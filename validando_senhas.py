import re

def verifica_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[0-9]', senha):
        return False
    return True 

# Exemplo de uso: 
senha = "SenhaSegura123"
if verifica_senha(senha):
    print("A senha atende aos critérios de segurança.")
else:
    print("A senha não atende aos critérios de segurança.")