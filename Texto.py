def contar_caracteres_e_palavras(texto):
    # Contar caracteres, incluindo espaços e pontuação
    num_caracteres = len(texto)
    
    # Dividir o texto em palavras e contar o número de palavras
    palavras = texto.split()
    num_palavras = len(palavras)
    
    return num_caracteres, num_palavras

# Solicitar ao usuário que insira um texto
texto = input("Digite um texto: ")

# Contar caracteres e palavras
num_caracteres, num_palavras = contar_caracteres_e_palavras(texto)

# Exibir os resultados
print(f"Número de caracteres: {num_caracteres}")
print(f"Número de palavras: {num_palavras}")
