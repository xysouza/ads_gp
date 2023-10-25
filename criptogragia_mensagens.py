def cifra_de_cesar(texto, chave):
    mensagem_criptografada = ""

    for caractere in texto:
        if caractere.isalpha():
            maiuscula = caractere.isupper()
            caractere = caractere.lower()
            codigo = ord(caractere) - ord('a')
            codigo = (codigo + chave) % 26
            caractere = chr(codigo + ord('a'))
            if maiuscula:
                caractere = caractere.upper()
        mensagem_criptografada += caractere

    return mensagem_criptografada

# Exemplo de uso
mensagem = "Olá, Mundo!"
chave = 3
mensagem_criptografada = cifra_de_cesar(mensagem, chave)
print("Mensagem Criptografada:", mensagem_criptografada)
