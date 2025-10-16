# from datetime import datetime

# # Solicita a data de nascimento
# data_nasc_str = input("Digite sua data de nascimento (formato: dd/mm/aaaa): ")

# # Converte a string para um objeto datetime
# data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y")

# # Pega a data atual
# hoje = datetime.today()

# # Calcula a idade
# idade = hoje.year - data_nasc.year

# # Ajusta se a pessoa ainda não fez aniversário neste ano
# if (hoje.month, hoje.day) < (data_nasc.month, data_nasc.day):
#     idade -= 1

# # Exibe o resultado
# # print(f"Você tem {idade} anos.")

# dia = int(input('Dia "Formato 1 a 7: '))

# match dia:
#     case 1:
#         print('Domingo')
#     case 2:
#         print('Segunda')
#     case 3:
#         print('Terça ')
#     case 4:
#         print('Quarta')
#     case 5:
#         print('Quinta')
#     case 6:
#         print('Sexta')
#     case 7:
#         print('Sabado')
#     case _:
#         print('Dia inválido')

from datetime import datetime

# Solicita uma data no formato dia/mês/ano
data_str = input("Digite uma data (no formato dd/mm/aaaa): ")

# Converte o texto em um objeto datetime
data = datetime.strptime(data_str, "%d/%m/%Y")

# Pega a data de hoje (sem horário)
hoje = datetime.now()

# Lista com os dias da semana
dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]

# Calcula a diferença em dias
diferenca = (data - hoje).days

# Mostra o dia da semana
print(f"\nA data {data_str} cai em uma {dias_semana[data.weekday()]}.")

# Mostra se a data é passada, presente ou futura
if diferenca > 0:
    print(f"Faltam {diferenca} dias para essa data.")
elif diferenca < 0:
    print(f"Essa data foi há {-diferenca} dias.")
else:
    print("Essa data é hoje!")
