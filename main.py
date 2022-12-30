import sys
import cv2
import imutils as imutils
import numpy as np
import qimage2ndarray
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMouseTracking(True)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.before = QLabel(self.centralwidget)
        self.before.setObjectName(u"before")
        self.before.setGeometry(QRect(50, 130, 400, 400))
        self.RefreshButton = QPushButton(self.centralwidget)
        self.RefreshButton.setObjectName(u"RefreshButton")
        self.RefreshButton.setGeometry(QRect(1050, 90, 161, 71))
        self.toGray = QPushButton(self.centralwidget)
        self.toGray.setObjectName(u"toGray")
        self.toGray.setGeometry(QRect(1050, 390, 161, 23))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1050, 250, 75, 23))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1050, 220, 75, 23))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1140, 220, 75, 23))
        self.after = QLabel(self.centralwidget)
        self.after.setObjectName(u"after")
        self.after.setGeometry(QRect(560, 130, 400, 400))
        self.beforeTextLabel = QLabel(self.centralwidget)
        self.beforeTextLabel.setObjectName(u"beforeTextLabel")
        self.beforeTextLabel.setGeometry(QRect(220, 100, 60, 20))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.beforeTextLabel.setFont(font)
        self.afterTextLabel = QLabel(self.centralwidget)
        self.afterTextLabel.setObjectName(u"afterTextLabel")
        self.afterTextLabel.setGeometry(QRect(730, 100, 60, 20))
        self.afterTextLabel.setFont(font)
        self.arrowLabel = QLabel(self.centralwidget)
        self.arrowLabel.setObjectName(u"arrowLabel")
        self.arrowLabel.setGeometry(QRect(490, 330, 56, 31))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.arrowLabel.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1120, 192, 56, 20))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(1140, 250, 75, 23))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1050, 450, 161, 23))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1120, 360, 56, 20))
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(1050, 310, 161, 23))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(250, 20, 81, 41))
        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(390, 20, 81, 41))
        self.toolButton_3 = QToolButton(self.centralwidget)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(530, 20, 81, 41))
        self.toolButton_4 = QToolButton(self.centralwidget)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(670, 20, 81, 41))
        self.CaptureButton = QToolButton(self.centralwidget)
        self.CaptureButton.setObjectName(u"CaptureButton")
        self.CaptureButton.setGeometry(QRect(430, 580, 121, 51))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(1050, 420, 161, 23))
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(1050, 280, 75, 23))
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(1140, 280, 75, 23))
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(1050, 480, 161, 23))
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(1050, 510, 161, 23))
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(1050, 540, 161, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.RefreshButton.clicked.connect(MainWindow.backToDefault)
        self.pushButton_2.clicked.connect(MainWindow.invert)
        self.pushButton_3.clicked.connect(MainWindow.horizontalFlip)
        self.pushButton_4.clicked.connect(MainWindow.verticalFlip)
        self.toGray.clicked.connect(MainWindow.toGrayScale)
        self.pushButton_7.clicked.connect(MainWindow.rotate)
        self.pushButton_6.clicked.connect(MainWindow.sharpen)
        self.pushButton_8.clicked.connect(MainWindow.blur)
        self.toolButton.clicked.connect(MainWindow.NewAction)
        self.toolButton_2.clicked.connect(MainWindow.OpenAction)
        self.toolButton_3.clicked.connect(MainWindow.SaveAction)
        self.toolButton_4.clicked.connect(MainWindow.QuitAction)
        self.CaptureButton.clicked.connect(MainWindow.capture)
        self.pushButton_9.clicked.connect(MainWindow.gaussianNoise)
        self.pushButton_10.clicked.connect(MainWindow.lighten)
        self.pushButton_11.clicked.connect(MainWindow.darken)
        self.pushButton_12.clicked.connect(MainWindow.contrast)
        self.pushButton_13.clicked.connect(MainWindow.mosaic)
        self.pushButton_14.clicked.connect(MainWindow.embossing)

        QMetaObject.connectSlotsByName(MainWindow)
        # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.before.setText("")
        self.RefreshButton.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uae30\ud654", None))
        self.toGray.setText(QCoreApplication.translate("MainWindow", u"\ud751\ubc31", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uc0c9\ubc18\uc804", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\uc88c\uc6b0\ubc18\uc804", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud558\ubc18\uc804", None))
        self.after.setText("")
        self.beforeTextLabel.setText("")
        self.afterTextLabel.setText("")
        self.arrowLabel.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc870\uc815", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"90\ub3c4 \ud68c\uc804", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\uc120\uba85\ud558\uac8c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ud544\ud130", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\ube14\ub7ec", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc9c4 \ucc0d\uae30", None))
        self.toolButton_2.setText(
            QCoreApplication.translate("MainWindow", u"\uc0ac\uc9c4 \ubd88\ub7ec\uc624\uae30", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.toolButton_4.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
        self.CaptureButton.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\ud751\ubc31+\ub178\uc774\uc988", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\ubc1d\uac8c", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\uc5b4\ub461\uac8c", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\uc9c4\ud558\uac8c", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\uc790\uc774\ud06c", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\uc5e0\ubcf4\uc2f1", None))
        # retranslateUi

isOn = False

class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Hotoshop")
        self.setWindowIcon(QIcon("MyPhotoShop.png"))
        self.CaptureButton.hide()

        self.show()

    def NewAction(self):
        if self.after:
            self.after.clear()
            self.beforeTextLabel.clear()
            self.afterTextLabel.clear()
            self.arrowLabel.clear()
        global isOn, cameraImg
        isOn = True
        capture = cv2.VideoCapture(0)
        frame_rate = capture.get(cv2.CAP_PROP_FPS)
        delay = int(1000 / frame_rate)
        self.CaptureButton.show()

        if not capture.isOpened():
            raise Exception("카메라 연결 실패")

        while isOn:
            ret, frame1 = capture.read()

            if not ret or cv2.waitKey(delay) >= 0:
                break

            cameraImg = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            cameraImg = imutils.resize(cameraImg, width=400)
            h, w, c = cameraImg.shape
            cameraQImg = QtGui.QImage(cameraImg.data, w, h, w * c, QtGui.QImage.Format_RGB888)
            cameraPixmap = QtGui.QPixmap.fromImage(cameraQImg)
            self.before.setPixmap(cameraPixmap)
            self.before.setGeometry(QtCore.QRect(300, 130, 400, 400))
            self.before.show()
        capture.release()
        cv2.destroyAllWindows()

    def capture(self):
        global isOn
        if isOn:
            isOn = False
            self.img = cameraImg
            self.qimg = self.img
        self.CaptureButton.hide()

    def OpenAction(self):
        openFileName = QFileDialog.getOpenFileName(self, "Open File", "./")
        if openFileName[0] != '':
            if self.after:
                self.after.clear()
                self.beforeTextLabel.clear()
                self.afterTextLabel.clear()
                self.arrowLabel.clear()
            self.img = cv2.imread(openFileName[0])
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.img = imutils.resize(self.img, width = 400)
            self.qimg = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_RGB888)
            self.beforePixmap = QtGui.QPixmap.fromImage(self.qimg)
            self.qimg = self.img
            self.before.setPixmap(self.beforePixmap)
            self.before.setGeometry(QtCore.QRect(300, 130, 400, 400))

    def SaveAction(self):
        saveFileName = QFileDialog.getSaveFileName(self, "Save File", ".\\")
        if saveFileName[0] != '':
            self.qimg = cv2.cvtColor(self.qimg, cv2.COLOR_BGR2RGB)
            cv2.imwrite(saveFileName[0], self.qimg)
            self.qimg = cv2.cvtColor(self.qimg, cv2.COLOR_BGR2RGB)
            self.img = self.qimg

    def QuitAction(self):
        app.quit()

    def horizontalFlip(self):
        flipped = cv2.flip(self.qimg, 1)
        self.qimg = flipped
        self.showImage(self.qimg)

    def verticalFlip(self):
        flipped = cv2.flip(self.qimg, 0)
        self.qimg = flipped
        self.showImage(self.qimg)

    def invert(self):
        src = self.qimg
        self.qimg = cv2.bitwise_not(src)
        self.showImage(self.qimg)

    def rotate(self):
        self.tempImg = self.qimg
        self.tempImg = cv2.rotate(self.qimg, cv2.ROTATE_90_CLOCKWISE)
        self.qimg = self.tempImg
        self.showImage(self.tempImg)

    def lighten(self):
        arr = np.full(self.qimg.shape, (20, 20, 20), dtype=np.uint8)
        self.tempImg = cv2.add(self.qimg, arr)
        self.qimg = self.tempImg
        self.showImage(self.tempImg)

    def darken(self):
        arr = np.full(self.qimg.shape, (20, 20, 20), dtype=np.uint8)
        self.tempImg = cv2.subtract(self.qimg, arr)
        self.qimg = self.tempImg
        self.showImage(self.tempImg)

    def blur(self):
        blurred = cv2.blur(self.qimg, (5, 5))
        self.qimg = blurred
        self.showImage(self.qimg)

    def toGrayScale(self):
        src = self.qimg
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        dst = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        self.qimg = dst
        self.showImage(self.qimg)

    def gaussianNoise(self):
        self.tempImg = cv2.cvtColor(self.qimg, cv2.COLOR_BGR2GRAY)
        h, w = self.tempImg.shape
        self.imgToShow = np.zeros((h, w), dtype=np.uint8)
        for i in range(h):
            for j in range(w):
                noise = np.random.normal() * 25
                self.imgToShow[i][j] = self.tempImg[i][j] + noise
        self.showImage(self.imgToShow)

    def contrast(self):
        func = (1 + 1.0) * self.qimg - (1.0 * 128)
        dst = np.clip(func, 0, 255).astype(np.uint8)
        self.qimg = dst
        self.showImage(self.qimg)

    def sharpen(self):
        sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened = cv2.filter2D(self.qimg, -2, sharp)
        self.qimg = sharpened
        self.showImage(self.qimg)

    def mosaic(self):
        self.tempImg = cv2.resize(self.qimg, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
        self.qimg = cv2.resize(self.tempImg, self.qimg.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
        self.showImage(self.qimg)

    def embossing(self):
        gray = cv2.cvtColor(self.qimg, cv2.COLOR_BGR2GRAY)
        filter = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
        self.qimg = cv2.filter2D(gray, -1, filter)
        self.showImage(self.qimg)

    def showImage(self, basicimg):
        self.beforeAfter()
        imgToShow = qimage2ndarray.array2qimage(basicimg, normalize=False)
        showImage_pixmap = QPixmap.fromImage(imgToShow)
        self.after.setPixmap(QPixmap(showImage_pixmap))

    def backToDefault(self):
        self.qimg = self.img
        self.showImage(self.img)

    def beforeAfter(self):
        self.before.setGeometry(QtCore.QRect(50, 130, 400, 400))
        self.beforeTextLabel.setText("before")
        self.afterTextLabel.setText("after")
        self.arrowLabel.setText("->")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    app.exec_()