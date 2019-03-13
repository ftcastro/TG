# coding: utf-8

# EXECUÇÃO
# python -W ignore recognize_video.py --video ../testing_lp_dataset --char-classifier output/simple_char.cpickle --digit-classifier output/simple_digit.cpickle
# python -W ignore recognize_video.py --video ../testing_lp_dataset --char-classifier output/adv_char.cpickle --digit-classifier output/adv_digit.cpickle

# Importando os pacotes necessários

from __future__ import print_function
from include.license_plate import LicensePlateDetector
from include.descriptors import BlockBinaryPixelSum
from imutils import paths
import warnings
import numpy as np
import argparse
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

    # Construindo o Argument Parser para passar os argumentos
        ap = argparse.ArgumentParser()
        # ap.add_argument("-v", "--video", required=True, help="Caminho para o vídeo a ser analisado. Argumento obrigatório")
        ap.add_argument("-v", "--video", help="Caminho para o vídeo a ser analisado. Argumento opcional")
        ap.add_argument("-c", "--char-classifier", required=True, help="Caminho para a saída do classificador de letras")
        ap.add_argument("-d", "--digit-classifier", required=True, help="Caminho para a saídado classificador de dígitos")
        args = vars(ap.parse_args())
	
    # Carregar os classificadores de dígitos e letras
	charModel = pickle.loads(open(args["char_classifier"], "rb").read())
	digitModel = pickle.loads(open(args["digit_classifier"], "rb").read())

    # Inicializar o descritor
	blockSizes = ((5, 5), (5, 10), (10, 5), (10, 10))
	desc = BlockBinaryPixelSum(targetSize=(30, 15), blockSizes=blockSizes)

    # Se um arquivo de vídeo não for fornecido, utilizar a webcam
    if not args.get("video", False):
        camera = cv2.VideoCapture(0)

    # Caso contrário, utilizar o arquivo fornecido
    else:
        camera = cv2.VideoCapture(args["video"])

    # Realizando a busca
    while True:

        fxn()

        # Captura o frame atual
        (grabbed, frame) = camera.read()

        # Se estivermos vendo um vídeo e não capturamos um frame, chegamos ao final do arquivo
        if args.get("video") and not grabbed:
            break

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
                #cv2.drawContours(frame, [lpBox], -1, (0, 255, 0), 2)
                #cv2.putText(frame, text, (cX - (cX / 5), cY - 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

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
