import cv2
from cnn import test_cnn
import numpy as np


def fomulaE(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    fomula = {}
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    """cv2.drawContours(img, contours, -1, (0, 0, 255), 1)"""
    leftSymbol = 0
    rightSymbol = 0
    for contour in contours[1:]:
        x, y, w, h = cv2.boundingRect(contour)
        image = img[:, x:x + w]
        reg = test_cnn.cnn_recognizer(image)
        if reg == '+' or reg == '-' or reg == 'x' or reg == 'd':
            leftSymbol = x
            rightSymbol = x + w
            symbol = reg
            break
    for contour in contours[1:]:
        x, y, w, h = cv2.boundingRect(contour)
        image = img[:, x:x + w]
        reg = test_cnn.cnn_recognizer(image)
        if reg == '=':
            leftEqual = x
            rightEqual = x + w

    firstNum = recognize(img[:, 0:leftSymbol])
    secondNum = recognize(img[:, rightSymbol:leftEqual])
    formula['firstNum'] = firstNum
    formula['symbol'] = symbol
    formula['secondNum'] = secondNum
    print(fomula)
    return (formula)
