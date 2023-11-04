# Função para converter decimal para binário
def decimal_para_binario(decimal):
    inteiro = int(decimal)
    fracao = decimal - inteiro

    parte_inteira = bin(inteiro).replace("0b", "")
    parte_fracionaria = ""

    if fracao > 0:
        parte_fracionaria = "."
        max_bits = 15  # Definindo um limite para os bits da parte fracionária
        while fracao > 0 and max_bits > 0:
            fracao *= 2
            bit = int(fracao)
            parte_fracionaria += str(bit)
            fracao -= bit
            max_bits -= 1

    return parte_inteira + parte_fracionaria

# Função para converter binário para decimal
def binario_para_decimal(binario):
    partes = binario.split(".")
    parte_inteira = int(partes[0], 2)
    parte_fracionaria = 0.0

    if len(partes) == 2:
        fracao = partes[1]
        for i in range(len(fracao)):
            parte_fracionaria += int(fracao[i]) * 2 ** -(i + 1)

    return parte_inteira + parte_fracionaria

# Converter decimal para binário
def converter_decimal_para_binario():
    numero_decimal = float(input("Digite um número decimal: "))
    binario_resultante = decimal_para_binario(numero_decimal)
    print(f'O número decimal {numero_decimal} em binário é: {binario_resultante}')

# Converter binário para decimal
def converter_binario_para_decimal():
    numero_binario = input("Digite um número binário: ")
    decimal_resultante = binario_para_decimal(numero_binario)
    print(f'O número binário {numero_binario} em decimal é: {decimal_resultante}')

# Interagir com o usuário
opcao = input("Escolha uma opção:\n 1 - Decimal para Binário\n 2 - Binário para Decimal\n")

if opcao == '1':
    converter_decimal_para_binario()
elif opcao == '2':
    converter_binario_para_decimal()
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
