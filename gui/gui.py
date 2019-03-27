# coding: utf-

# USAGE: python3.6 gui/gui.py

import os

try:
    import tkinter as tk
    from tkinter import ttk

except ImportError:
    import Tkinter as tk


LARGE_FONT = ("Verdana", 12)


class MonitorGUI(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="images/icon.ico")
        tk.Tk.wm_title(self, "Sistema de Monitoramento")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Autenticacao, PaginaPrincipal, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            # frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame(Autenticacao)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Autenticacao(tk.Frame):

    def __init__(self, parent, master=None):

        tk.Frame.__init__(self, parent)
        # label = ttk.Label(self, text="Página Inicial", font=LARGE_FONT)
        # label.pack(pady=10, padx=10)
        #
        # button1 = ttk.Button(self, text="Ir para página 1", command=lambda: controller.show_frame(PageOne))
        # button1.pack()

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = tk.Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        self.segundoContainer = tk.Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = tk.Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = tk.Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = tk.Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=tk.LEFT)

        self.nome = tk.Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=tk.LEFT)

        self.senhaLabel = tk.Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=tk.LEFT)

        self.senha = tk.Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=tk.LEFT)

        self.autenticar = tk.Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = tk.Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        # Método verificar senha

    def verificaSenha(self):

        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "admin" and senha == "admin":
            self.mensagem["text"] = "Autenticado"

            PaginaPrincipal(parent=None, controller=None)
            print(usuario)
            print(senha)

        else:
            self.mensagem["text"] = "Erro na autenticação"


class PaginaPrincipal(tk.Frame):

    def __init__(self, parent, controller):

        def cadastrarPlaca():
            print("Chama a tela para cadastrar uma nova placa aqui")

        def editarPlaca():
            print("Chama a tela para editar as placas aqui")

        def cadastrarHorario():
            print("Chama a tela para cadastrar um horário aqui")

        def editarHorario():
            print("Chama a tela para editar os horários aqui")

        def iniciarMonitoramento():
            telaPrincipal.quit()
            # subprocess.run(['python /gui/telaMonitoramento.py'])
            # print(subprocess.check_output(['python /home/fernando/PycharmProjects/TG/gui/telaMonitoramento.py']))
            print("Chama a tela de monitoramento com código novo GIT")
            os.system('python gui/telaMonitoramento.py')

        def sobreSistema():
            print("Sistema de Auditoria de Transportes Coletivos")

        telaPrincipal = tk.Tk()
        menu = tk.Menu(telaPrincipal)
        telaPrincipal.config(menu=menu)
        placasMenu = tk.Menu(menu)
        menu.add_cascade(label="Placas", menu=placasMenu)
        placasMenu.add_command(label="Cadastrar Placa...", command=cadastrarPlaca)
        placasMenu.add_command(label="Editar Placas...", command=editarPlaca)

        horariosMenu = tk.Menu(menu)
        menu.add_cascade(label="Horários", menu=horariosMenu)
        horariosMenu.add_command(label="Cadastrar Horário...", command=cadastrarHorario)
        horariosMenu.add_command(label="Editar Horários...", command=editarHorario)

        monitoramentoMenu = tk.Menu(menu)
        menu.add_cascade(label="Monitoramento", menu=monitoramentoMenu)
        monitoramentoMenu.add_command(label="Iniciar Monitoramento", command=iniciarMonitoramento)

        sobreMenu = tk.Menu(menu)
        menu.add_cascade(label="Sobre", menu=sobreMenu)
        sobreMenu.add_command(label="Sobre o Sistema...", command=sobreSistema)
        sobreMenu.add_separator()
        sobreMenu.add_command(label="Sair", command=telaPrincipal.quit)

        telaPrincipal.geometry("600x450+650+150")
        telaPrincipal.title("Sistema de Monitoramento de Transportes")

        # tk.Frame.__init__(self, parent)
        # label = ttk.Label(self, text="Página 1", font=LARGE_FONT)
        # label.pack(pady=10, padx=10)
        #
        # button1 = ttk.Button(self, text="Voltar para a Página Inicial", command=lambda: controller.show_frame(StartPage))
        # button1.pack()
        #
        # button2 = ttk.Button(self, text="Ir para a Página 2", command=lambda: controller.show_frame(PageTwo))
        # button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Página 2", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # button1 = ttk.Button(self, text="Voltar para a Página Inicial", command=lambda: controller.show_frame(StartPage))
        # button1.pack()
        #
        # button2 = ttk.Button(self, text="Ir para página 1", command=lambda: controller.show_frame(PageOne))
        # button2.pack()


app = MonitorGUI()
app.mainloop()
