#Algoritmo que solicita o nome completo do usuário e retorna o primeiro e o último nome

nome_completo = input("Digite seu nome completo: ").strip()

partes = nome_completo.split()

primeiro_nome = partes[0]
ultimo_nome = partes[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")