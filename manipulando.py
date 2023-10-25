senhas = [1521, 5245, 5848, 8542, 7777, 7539, 9517, 8523, 5424]

#print(senhas)

nova_senha = 5878

senhas.append(nova_senha)

#print(senhas)

senhas.remove(1521)

#print(senhas)

contagem = len(senhas)

#print(contagem)

senha_mais_longa = ""

for senha in senhas:
    senha_str = str(senha)
    if len(senha_str) > len(senha_mais_longa):
        senha_mais_longa = senha_str

print(f"A senha mais longa é: {senha_mais_longa}")
