# Aula 40 - Calculadora com While
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numero_validos = None
    numero1_float = 0
    numero2_float = 0

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numero_validos = True
    except:
        numero_validos = None

    if numero_validos is None:
        print('Um ou ambos dos números digitados são inválidos!')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta, confira o resultado abaixo: ')

    if operador == '+':
        print(f'{numero1_float} + {numero2_float} =', numero1_float + numero2_float)
    elif operador == '-':
       print(f'{numero1_float} - {numero2_float} =', numero1_float - numero2_float)
    elif operador == '/':
        print(f'{numero1_float} / {numero2_float} =', numero1_float / numero2_float)
    elif operador == '*':
        print(f'{numero1_float} * {numero2_float} =', numero1_float * numero2_float)
    else:
        print('Existe algum erro na nossa validação, contate o suporte.')

    sair = input ('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break