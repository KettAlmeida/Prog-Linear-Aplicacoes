#--------------------------------------------------------------------------------------------------------------
#Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se
# é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
#---------------------------------------------------------------------------------------------------------------

cpf = input('Digite o CPF: ')
if len(cpf) > 11:
    cpf = cpf.zfill(11)
print(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}, CPF Válido!')

if cpf == cpf[::-1]:
    print(f' CPF inválido !')


