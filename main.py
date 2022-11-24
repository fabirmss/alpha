login_secreta = "fabi"
senha_secreta = "125"


login = input("Digite o seu login:")

if(login == login_secreta):
    senha =input("Digite a senha:")
    if(senha == senha_secreta):
        print ("Bem vindo ao sistema!")
    else:
        print ("Vc errou sua senha!")
else:
    print("Esse login não existe na base de dados")
