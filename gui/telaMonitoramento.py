# coding: utf-8

import time
from Tkinter import *
import cv2

import PIL
from PIL import Image, ImageTk

##########

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


    (h, w) = frame.shape[:2]

#    print(h)
#    print(w)



telaMonitoramento = Tk()

telaMonitoramento.geometry("920x610")
telaMonitoramento.title("Sistema de Monitoramento de Transportes")

telaMonitoramento.update_idletasks()
width, height = (telaMonitoramento.winfo_width()-50), (telaMonitoramento.winfo_height()-50)

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

print(telaMonitoramento.winfo_width())
print(telaMonitoramento.winfo_height())


def cadastrarPlaca():
    print("Chama a tela para cadastrar uma nova placa aqui")

def editarPlaca():
    print("Chama a tela para editar as placas aqui")

def cadastrarHorario():
    print("Chama a tela para cadastrar um horário aqui")

def editarHorario():
    print("Chama a tela para editar os horários aqui")

def iniciarMonitoramento():
    print("Chama a tela de monitoramento")

def sobreSistema():
    print("Sistema de Auditoria de Transportes Coletivos")

# Fontes utilizadas nos labels

fonteGrande = "-family {DejaVu Sans} -size 20 -weight bold -slant " "roman -underline 0 -overstrike 0"
fonteNormal = "-family {DejaVu Sans} -size 12 -weight bold -slant " "roman -underline 0 -overstrike 0"
fonteNegrito = "-family {DejaVu Sans} -size 12 -weight bold -slant " "roman -underline 0 -overstrike 0"

time = time.strftime("%H:%M:%S")

# Menu Superior

menu = Menu(telaMonitoramento)

telaMonitoramento.config(menu=menu)
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
sobreMenu.add_command(label="Sair", command=telaMonitoramento.quit)



#TODO: centralizar tela

lmain = Label(telaMonitoramento)
lmain.pack()

# Moldura da área dos dados

telaMonitoramento.Canvas1 = Canvas(telaMonitoramento)
telaMonitoramento.Canvas1.place(relx=0.037, rely=0.805, relheight=0.180, relwidth=0.925)
telaMonitoramento.Canvas1.configure(borderwidth="2")
telaMonitoramento.Canvas1.configure(relief='ridge')
telaMonitoramento.Canvas1.configure(width=565)


# Labels com os dados

telaMonitoramento.Label1 = Label(telaMonitoramento)
telaMonitoramento.Label1.place(relx=0.054, rely=0.820, height=30, width=278)
telaMonitoramento.Label1.configure(font=fonteGrande)
telaMonitoramento.Label1.configure(text='Status do Veículo:')

telaMonitoramento.Label2 = Label(telaMonitoramento)
telaMonitoramento.Label2.place(relx=0.388, rely=0.820, height=30, width=147)
telaMonitoramento.Label2.configure(font=fonteGrande)
telaMonitoramento.Label2.configure(activeforeground="#0bd633")
telaMonitoramento.Label2.configure(foreground="#0bd633")
telaMonitoramento.Label2.configure(text='PONTUAL')

telaMonitoramento.Label3 = Label(telaMonitoramento)
telaMonitoramento.Label3.place(relx=0.044, rely=0.875, height=30, width=290)
telaMonitoramento.Label3.configure(font=fonteGrande)
telaMonitoramento.Label3.configure(text='''Horário da Leitura:''')

telaMonitoramento.Label4 = Label(telaMonitoramento)
telaMonitoramento.Label4.place(relx=0.390, rely=0.875, height=30, width=140)
telaMonitoramento.Label4.configure(font=fonteGrande)
telaMonitoramento.Label4.configure(text=time)

telaMonitoramento.Label5 = Label(telaMonitoramento)
telaMonitoramento.Label5.place(relx=0.059, rely=0.930, height=30, width=290)
telaMonitoramento.Label5.configure(font=fonteGrande)
telaMonitoramento.Label5.configure(text='''Placa Detectada:''')

telaMonitoramento.Label6 = Label(telaMonitoramento)
telaMonitoramento.Label6.place(relx=0.390, rely=0.930, height=30, width=140)
telaMonitoramento.Label6.configure(font=fonteGrande)
telaMonitoramento.Label6.configure(text=time)

# Botão para Encerrar o Monitoramento

telaMonitoramento.botaoEncerrar = Button(telaMonitoramento)
telaMonitoramento.botaoEncerrar.place(relx=0.730, rely=0.870, height=31, width=186)
telaMonitoramento.botaoEncerrar.configure(activebackground="#d9d9d9")
telaMonitoramento.botaoEncerrar.configure(text='''Encerrar Monitoramento''')


def configure(event):
    w, h = telaMonitoramento.winfo_width()-100, telaMonitoramento.winfo_height()-100
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

telaMonitoramento.bind("<Configure>", configure)
telaMonitoramento.resizable(False, False)

show_frame()
telaMonitoramento.mainloop()