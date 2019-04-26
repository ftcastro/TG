def verificaSenha(self):
    usuario = self.nome.get()
    senha = self.senha.get()
    if usuario == "admin" and senha == "admin":
        self.mensagem["text"] = "Autenticado"
        print(usuario)
        print(senha)
    else:
        self.mensagem["text"] = "Erro na autenticação"