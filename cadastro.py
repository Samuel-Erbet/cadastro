from time import sleep
print('=-'*20)
print('seja bem vindo ao nosso sistema \n escolha uma das opções abaixo:')

while True:
    print('=-'*20)
    print('[1] - cadastrar no sistema \n '
      '[2] entrar no sistema \n'
      '[3] sair do sistema \n')
    print('=='*20)
    opcao_usuario= int(input('qual a sua opção: '))
    if opcao_usuario ==1:
        cad_usuario = str(input('informe um usuário: '))
        print(f'Úsuario {cad_usuario} cadastrado com sucesso!')
        cad_senha = input('insira uma senha de no minimo 8 caracteres: ')
        while len(cad_senha)<8:
            print('sua senha é pequena demais.')
            print('')
            print('insira novamente a senha: ')
        print('senha cadastrada com sucesso!')
    elif opcao_usuario == 2:
        veri_usuario = str(input('insira o nome de usuário: '))
        if veri_usuario == cad_usuario:
            veri_senha = input('insira o valor da senha: ')
            if veri_senha == cad_senha:
                print('logado com sucesso!')
                break
            else:
                print('senha incorreta!')
                while True: 
                    print('[1] - tentar novamente \n'
                          '[2] - Sair ')
                    opc = int(input('sua opção: '))
                    if opc ==1:
                        veri_senha = input('senha: ')
                        if veri_senha == cad_senha:
                            print('logado com sucesso!')
                            break
                    elif opc==2:
                        print('obrigado, tenha um otimo dia!')
                        break
                    else: 
                        print('escolha somente uma das opções abaixo')

        else:
            print('usuário incorreto!')
            while True: 
                print('[1] - Tentar novamente \n'
                      '[2] - Sair')
                opc = int(input('insira sua opção: '))
                if opc ==1:
                    veri_usuario = input('usuário: ')
                    if veri_usuario == cad_usuario:
                        print(f'usuário {cad_usuario} está correto.')
                        veri_senha = input('insira a sua senha: ')
                        if veri_senha == cad_senha:
                            print('logado com sucesso!')
                            break
                        else:
                            print('senha incorreta!')
                            while True: 
                                print('[1] - Tentar novamente \n'
                                      '[2] - Sair')
                                opc = int(input('insira a sua opção: '))
                                if opc == 1:
                                    veri_senha=input('insira a senha: ')
                                    if veri_senha == cad_senha:
                                        print('logado com sucesso!')
                                        break
                                    elif opc == 2:
                                        print('obrigado! tenha um otimo dia!')
                                        break
                                    else:
                                        print('escolha somente uma das alternativas acima: ')
                elif opc == 2:
                    break
                else:
                    print('escolha somente uma das alternativas abaixo')
    elif opcao_usuario ==3:
        print('sistema encerrando em...')
        for c in range(3,0,-1):
            sleep(1)
            print(c)
        sleep(1)
        break
    else:
        print('escolha somente uma das alternativas abaixo')                            
