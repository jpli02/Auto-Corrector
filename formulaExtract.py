import cv2
from cnn import test_cnn
import numpy as np
from cut import cutWhite


def formulaE(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    formula = {}
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    """cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    cv2.imwrite("img.png",img)"""
    leftSymbol = 0
    rightSymbol = 0
    num = 0
    for contour in contours[1:]:
        x, y, w, h = cv2.boundingRect(contour)
        if w + x > len(img[0]) * 0.8:
            continue
        if w < len(img[0]) * 0.05:
            continue
        image = img[:, x:x + w]
        reg = test_cnn.cnn_recognizer(image)
        if reg == '+' or reg == '-' or reg == 'x' or reg == 'd':
            """cv2.imwrite("symbolImg.png", image)"""
            leftSymbol = x
            rightSymbol = x + w
            symbol = reg
            break
    """for contour in contours[1:]:
        x, y, w, h = cv2.boundingRect(contour)
        if w + x < len(img[0]) * 0.8:
            continue
        if x < rightSymbol:
            continue
        image = img[:, x:x + w]
        num += 1
        reg = test_cnn.cnn_recognizer(image)
        print("reg" + str(num - 1), reg)
        cv2.imwrite("reg" + str(num - 1) + ".png", image)
        if reg == '=':
            cv2.imwrite("equalImg.png", image)
            leftEqual = x
            rightEqual = x + w"""

    """firstImg = cutWhite(img[:, 0:leftSymbol], 127)"""
    firstImg = img[:, 0:leftSymbol]
    firstNum = test_cnn.cnn_recognizer(firstImg)
    """cv2.imwrite("firstNum.png", firstImg)"""
    """secondImg = cutWhite(img[:, rightSymbol:], 127)"""
    secondImg = img[:, rightSymbol:]
    secondNum = test_cnn.cnn_recognizer(secondImg)
    """cv2.imwrite("secondNum.png", secondImg)"""
    """result = img[:, rightEqual:]
    resultWidth = len(result[0])
    resultHeight = len(result)
    count = 0
    for h in range(resultHeight):
        for w in range(resultWidth):
            if result[h, w, 0] < 127:
                count += 1
    if count / (resultWidth * resultHeight) < 0.05:
        formula['resultTF'] = False
    else:
        formula['resultTF'] = True
    if formula['resultTF']:
        formula['result'] = test_cnn.cnn_recognizer(result)"""
    """ f = open('firstNum.png', 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    response = requests.post(request_url, data=params, headers=headers)
    print("first:", response.json())
    if response:
        print(response.json())
        if response.json()['words_result_num'] > 0:
            firstNum = response.json()['words_result'][0]['words']

    f = open('secondNum.png', 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    response = requests.post(request_url, data=params, headers=headers)
    print("second:", response.json())
    if response:
        if response.json()['words_result_num'] > 0:
            secondNum = response.json()['words_result'][0]['words']"""

    formula['firstNum'] = firstNum
    formula['symbol'] = symbol
    formula['secondNum'] = secondNum
    return (formula)
