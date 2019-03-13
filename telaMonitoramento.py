# coding: utf-8



from __future__ import print_function
from include.license_plate import LicensePlateDetector
from include.descriptors import BlockBinaryPixelSum
import warnings
import numpy as np
import pickle
import imutils
import cv2
import time
from Tkinter import *
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

################################################################################

# Ignorando os warning de deprecated do sistema
def fxn():
    warnings.warn("deprecated", DeprecationWarning)

if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fxn()

	camera = cv2.VideoCapture(0)
    char_classifier = "output/adv_char.cpickle"
    digit_classifier = "output/adv_digit.cpickle"

    # Carregar os classificadores de dígitos e letras

    charModel = pickle.load(open(str(char_classifier), 'rb'))
    digitModel = pickle.load(open(str(digit_classifier), "rb"))

    # Inicializar o descritor
    blockSizes = ((5, 5), (5, 10), (10, 5), (10, 10))
    desc = BlockBinaryPixelSum(targetSize=(30, 15), blockSizes=blockSizes)

    # Realizando a busca
    while True:

        fxn()

        # Captura o frame atual
        (grabbed, frame) = camera.read()

        # Redimensiona o frame, converte para grayscale e inicia a detecção
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Inicializa o detector de placas e detecta as placas e os caracteres
        lpd = LicensePlateDetector(frame, numChars=7)
        plates = lpd.detect()

        # Faz o looping nas placas detectadas
        for (lpBox, chars) in plates:
            # Inicializa o texto contendo os caracteres reconhecidos
            text = ""

            # Faz o looping em cada caractere
            for (i, char) in enumerate(chars):

                # Realiza o pré-processamento do caractere e sua descrição
                try:
                    char = LicensePlateDetector.preprocessChar(char)
                    features = desc.describe(char).reshape(1, -1)
                except Exception:
                    continue

                # Se forem os três primeiros caracteres, utilizamos o reconhecedor de letras
                if i < 3:
                    prediction = charModel.predict(features)[0]

                # Caso contrário, utilizamos o reconhecedor de números
                else:
                    prediction = digitModel.predict(features)[0]

                # Atualizamos o texto com os caracteres reconhecidos em CAIXA ALTA
                text += prediction.upper()

            # Apenas desenhe o quadrado se tiver algo que foi reconhecido e haja caracteres a serem exibidos
            if len(chars) > 0:
                # processar o centro da caixa da placa do veículo
                M = cv2.moments(np.array([lpBox]))
                M = cv2.moments(lpBox)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # Desenhar a região da placa e o texto com os caracteres na imagem

                lpBox = np.array(lpBox).reshape((-1,1,2)).astype(np.int32)
                cv2.drawContours(frame, [lpBox], -1, (0, 255, 0), 2)
                cv2.putText(frame, text, (cX - (cX // 5), cY - 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
                print(text)

        # Exibir o vídeo na tela
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # Se a tecla "q" for pressionada, acabar com o loop
        if key == ord("q"):
            break

    # Liberar a câmera e fechar as janelas abertas
    camera.release()
    cv2.destroyAllWindows()
