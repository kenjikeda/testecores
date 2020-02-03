import cv2
import numpy as np
import time


def capturarCor():
    vid = cv2.VideoCapture(0)
    file = "C:\\Users\\Ikedas\\Desktop\\pisicultura_QualidadeDaAgua_cPythonEOpenCV\\teste.png"

    while(1):
        _, image = vid.read()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        cv2.imshow('image_window_name',image)
        cv2.waitKey(5)
        print(hsv[100, 100, 0])
        print(hsv[100, 100, 1])
        print(hsv[100, 100, 2])
        time.sleep(10)

    cv2.imwrite(file, image)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    import sys
    #sys.exit(main(sys.argv))
    sys.exit(capturarCor())
