# coding: utf-8

# Importando os pacotes necessários

from __future__ import print_function
from include.license_plate import LicensePlateDetector
from include.descriptors import BlockBinaryPixelSum
import warnings
import numpy as np
import pickle
import imutils
import cv2


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
