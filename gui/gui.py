# coding: utf-8

# USAGE: python3 gui/gui.py

# Importando os arquivos de scripts e outros necessários
import sys
sys.path.insert(0, './scripts')
import scripts


# Imports to Matplotlib utilizados para o teste, devem ser retirados em  breve
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

try:
    import tkinter as tk
    from tkinter import ttk

except ImportError:
    import Tkinter as tk


LARGE_FONT = ("Verdana", 12)


# Dentro dos parênteses passam as heranças.
class MonitorGUI(tk.Tk):

    # Dentro desses parênteses vão os métodos a serem inicializados assim que a classe é chamada.
    # Self é implícito, não precisa ser passado, mas é convenção.
    # Args são qualquer número ou variável que pode ser passado
    # Kwargs são argumentos do teclado, basicamente dicionários

    def __init__(self, *args, **kwargs):

        # Inicialização do Tkinter
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.wm_iconbitmap(self, default="camera.ico")
        tk.Tk.wm_title(self, "Sistema de Monitoramento")

        container = tk.Frame(self)

        # O container é a nossa janela. Aqui está setada a orientação, o fill e se ele é expansível.
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Autenticacao, PaginaPrincipal, Monitoramento, Cadastro, Listar, Excluir, Inserir, Editar, About):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Autenticacao)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Autenticacao(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label1 = ttk.Label(self, text="Autenticação")
        label1.pack(pady=10, padx=10)

        inputNome = ttk.Entry(self)
        inputNome["width"] = 30
        inputNome.pack()

        label2 = ttk.Label(self, text="Senha")
        label2.pack()

        inputSenha = ttk.Entry(self)
        inputSenha["width"] = 30
        inputSenha["show"] = "*"
        inputSenha.pack()

        button1 = ttk.Button(self, text="Autenticar", command=lambda: controller.show_frame(Monitoramento))
        button1.pack(pady=10)


class PaginaPrincipal(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Tela Inicial", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Monitoramento", command=lambda: controller.show_frame(Monitoramento))
        button1.pack()

        button2 = ttk.Button(self, text="Cadastro", command=lambda: controller.show_frame(Cadastro))
        button2.pack()

        button3 = ttk.Button(self, text="Listar", command=lambda: controller.show_frame(Listar))
        button3.pack()

        button4 = ttk.Button(self, text="Excluir", command=lambda: controller.show_frame(Excluir))
        button4.pack()

        button5 = ttk.Button(self, text="Inserir", command=lambda: controller.show_frame(Inserir))
        button5.pack()

        button6 = ttk.Button(self, text="Editar", command=lambda: controller.show_frame(Editar))
        button6.pack()

        button7 = ttk.Button(self, text="About", command=lambda: controller.show_frame(About))
        button7.pack()


class Monitoramento(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Monitoramento", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Voltar para a Página Inicial", command=lambda: controller.show_frame(PaginaPrincipal))
        button1.pack()


class Cadastro(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Cadastro", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Voltar para a Página Inicial", command=lambda: controller.show_frame(PaginaPrincipal))
        button1.pack()


class Listar(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Listar", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Voltar para a Página Inicial", command=lambda: controller.show_frame(PaginaPrincipal))
        button1.pack()


class Excluir(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Excluir", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Voltar para a Página Inicial", command=lambda: controller.show_frame(PaginaPrincipal))
        button1.pack()


class Inserir(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Inserir", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Voltar para a Página Inicial", command=lambda: controller.show_frame(PaginaPrincipal))
        button1.pack()


class Editar(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Editar", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Voltar para a Página Inicial", command=lambda: controller.show_frame(PaginaPrincipal))
        button1.pack()


class About(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Voltar para a Página Inicial", command=lambda: controller.show_frame(PaginaPrincipal))
        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 1])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)


app = MonitorGUI()
app.mainloop()
