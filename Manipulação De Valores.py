op = 0
while op != 5:
    valor1 = float(input('Insira um valor: '))
    valor2 = float(input('Insira um valor: '))
    print('Agora escolha uma opção por favor')
    print('[1] Somar valores\n[2] Multiplicar valores\n[3] Identificar maior\n[4] Digitar novos números\n[5] Sair')
    op = int(input('Insira sua opção: '))
    while op not in {1, 2, 3, 4, 5}:
        print('Opção inválida! Tente novamente')
        print('=' * 50)
        op = int(input('Insira sua opção: '))
    if op == 1:
        print(f'A soma entre {valor1} e {valor2} é igual a {valor1 + valor2}!')
        break
    elif op == 2:
        print(f'A multiplicação entre {valor1} e {valor2} é igual a {valor1 * valor2}')
        break
    elif op == 3:
        if valor1 > valor2:
            print(f'O valor {valor1} é maior do que o valor {valor2}!')
            break
        if valor2 > valor1:
            print(f'O valor {valor2} é maior do que o valor {valor1}!')
            break
        print('Não existe valor maior pois são iguais!')
        break
    elif op == 4:
        print('='*50)
    elif op == 5:
        print('FIM')
