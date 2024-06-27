def cadastrar_usuario():
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha (deve ter mais de 8 caracteres): ")
    
    if len(senha) >= 8:
        print("Usuário cadastrado com sucesso!")
        return usuario, senha
    else:
        print("Erro: A senha deve ter mais de 8 caracteres.")
        return None, None

usuario_cadastrado = False
while not usuario_cadastrado:
    usuario, senha = cadastrar_usuario()
    if usuario and senha:
        usuario_cadastrado = True

print(f"Usuário: {usuario}")
print(f"Senha: {senha}")