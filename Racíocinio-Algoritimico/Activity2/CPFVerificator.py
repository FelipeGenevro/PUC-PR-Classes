#algoritmo capaz de verificar a validade da idade e do CPF de um candidato para o teste do DETRAN!

age = int(input('Digite a sua idade: '))

if age < 18:
    print("Você não pode fazer o teste do DETRAN, pois tem menos de 18 anos!")
    exit()
elif 18 <= age <= 150:
    print("Você pode fazer o teste do DETRAN, pois tem mais de 18 anos!")
else:
    print("Digite uma idade válida!")
    exit()

cpf = input('Digite seu CPF: ')

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    #dígito 1
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    d1 = (soma * 10 % 11) % 10

    #dígito 2
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    d2 = (soma * 10 % 11) % 10

    return cpf[-2:] == f"{d1}{d2}"

if not validar_cpf(cpf):
    print("CPF inválido")
elif validar_cpf(cpf):
    print("CPF valido")