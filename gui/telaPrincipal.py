# coding: utf-8
import subprocess
import os

from Tkinter import *

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
    #subprocess.run(['python /gui/telaMonitoramento.py'])
    #print(subprocess.check_output(['python /home/fernando/PycharmProjects/TG/gui/telaMonitoramento.py']))
    print("Chama a tela de monitoramento com código novo")
    os.system('python gui/telaMonitoramento.py')

def sobreSistema():
    print("Sistema de Auditoria de Transportes Coletivos")

telaPrincipal = Tk()
menu = Menu(telaPrincipal)
telaPrincipal.config(menu=menu)
placasMenu = Menu(menu)
menu.add_cascade(label="Placas", menu=placasMenu)
placasMenu.add_command(label="Cadastrar Placa...", command=cadastrarPlaca)
placasMenu.add_command(label="Editar Placas...", command=editarPlaca)

horariosMenu = Menu(menu)
menu.add_cascade(label="Horários", menu=horariosMenu)
horariosMenu.add_command(label="Cadastrar Horário...", command=cadastrarHorario)
horariosMenu.add_command(label="Editar Horários...", command=editarHorario)

monitoramentoMenu = Menu(menu)
menu.add_cascade(label="Monitoramento", menu=monitoramentoMenu)
monitoramentoMenu.add_command(label="Iniciar Monitoramento", command=iniciarMonitoramento)

sobreMenu = Menu(menu)
menu.add_cascade(label="Sobre", menu=sobreMenu)
sobreMenu.add_command(label="Sobre o Sistema...", command=sobreSistema)
sobreMenu.add_separator()
sobreMenu.add_command(label="Sair", command=telaPrincipal.quit)

telaPrincipal.geometry("600x450+650+150")
telaPrincipal.title("Sistema de Monitoramento de Transportes")

mainloop()