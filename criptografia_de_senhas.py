import hashlib

def criptografar_senha(senha):
    # Crie um objeto de hash usando o algoritmo SHA-256
    hash_obj = hashlib.sha256()
    
    # Atualize o objeto de hash com a senha convertida para bytes
    hash_obj.update(senha.encode('utf-8'))
    
    # Obtenha a senha criptografada em formato hexadecimal
    senha_criptografada = hash_obj.hexdigest()
    
    return senha_criptografada

# Exemplo de uso da função
senha = "minha_senha_secreta"
senha_criptografada = criptografar_senha(senha)
print("Senha criptografada:", senha_criptografada)
