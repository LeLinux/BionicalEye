from PySide6 import QtTest, QtWidgets, QtGui, QtCore
import qdarktheme
import sys
import time
import cv2
import matplotlib.pyplot as plt
import numpy as np

import symbols

class Camera(QtWidgets.QGroupBox):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        #self.label = QtWidgets.QLabel(self, text = "NONE")
        self.setStyleSheet("""QGroupBox{border: 0px;}""")
        self.setContentsMargins(0,0,0,0)
        self.parent = parent
        self.active = 0

    def __run__(self):
        cap = cv2.VideoCapture(0)
        self.active = 1

        while self.active:
            ret, frame = cap.read()
            im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
            img = cv2.medianBlur(gray, 5)

            th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 8)
            contours, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

            img_contours = cv2.drawContours(np.uint8(np.zeros((im.shape[0], im.shape[1]))), contours, -1, (255, 255, 255), 0)

            resized_img = cv2.resize(img_contours, (8,8), interpolation=cv2.INTER_AREA)

            ret,thresh1 = cv2.threshold(resized_img,0,255,cv2.THRESH_BINARY)
            print(thresh1)
            self.parent.parent.viewbox.__draw__(thresh1)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def __hide__(self):
        self.active = 0
        self.hide()


class Symbols(QtWidgets.QGroupBox):
    def __init__(self, parent = None):
        super().__init__(parent = parent)

        self.update = 0
        self.current_symbol = 0

        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        self.line_1_hbox = QtWidgets.QHBoxLayout(self)
        self.line_1_group = QtWidgets.QGroupBox(self)
        self.line_1_group.setLayout(self.line_1_hbox)
        self.a = QtWidgets.QToolButton(self, text = "a")
        self.b = QtWidgets.QToolButton(self, text = "b")
        self.c = QtWidgets.QToolButton(self, text = "c")
        self.d = QtWidgets.QToolButton(self, text = "d")
        self.e = QtWidgets.QToolButton(self, text = "e")
        self.f = QtWidgets.QToolButton(self, text = "f")
        self.line_1_hbox.addWidget(self.a)
        self.line_1_hbox.addWidget(self.b)
        self.line_1_hbox.addWidget(self.c)
        self.line_1_hbox.addWidget(self.d)
        self.line_1_hbox.addWidget(self.e)
        self.line_1_hbox.addWidget(self.f)
                
        self.line_2_hbox = QtWidgets.QHBoxLayout(self)
        self.line_2_group = QtWidgets.QGroupBox(self)
        self.line_2_group.setLayout(self.line_2_hbox)
        self.g = QtWidgets.QToolButton(self, text = "g")
        self.h = QtWidgets.QToolButton(self, text = "h")
        self.i = QtWidgets.QToolButton(self, text = "i")
        self.j = QtWidgets.QToolButton(self, text = "j")
        self.k = QtWidgets.QToolButton(self, text = "k")
        self.l = QtWidgets.QToolButton(self, text = "l")
        self.line_2_hbox.addWidget(self.g)
        self.line_2_hbox.addWidget(self.h)
        self.line_2_hbox.addWidget(self.i)
        self.line_2_hbox.addWidget(self.j)
        self.line_2_hbox.addWidget(self.k)
        self.line_2_hbox.addWidget(self.l)
        

        self.line_3_hbox = QtWidgets.QHBoxLayout(self)
        self.line_3_group = QtWidgets.QGroupBox(self)
        self.line_3_group.setLayout(self.line_3_hbox)
        self.m = QtWidgets.QToolButton(self, text = "m")
        self.n = QtWidgets.QToolButton(self, text = "n")
        self.o = QtWidgets.QToolButton(self, text = "o")
        self.p = QtWidgets.QToolButton(self, text = "p")
        self.q = QtWidgets.QToolButton(self, text = "q")
        self.r = QtWidgets.QToolButton(self, text = "r")
        self.line_3_hbox.addWidget(self.m)
        self.line_3_hbox.addWidget(self.n)
        self.line_3_hbox.addWidget(self.o)
        self.line_3_hbox.addWidget(self.p)
        self.line_3_hbox.addWidget(self.q)
        self.line_3_hbox.addWidget(self.r)
        

        self.line_4_hbox = QtWidgets.QHBoxLayout(self)
        self.line_4_group = QtWidgets.QGroupBox(self)
        self.line_4_group.setLayout(self.line_4_hbox)
        self.s = QtWidgets.QToolButton(self, text = "s")
        self.t = QtWidgets.QToolButton(self, text = "t")
        self.u = QtWidgets.QToolButton(self, text = "u")
        self.v = QtWidgets.QToolButton(self, text = "v")
        self.w = QtWidgets.QToolButton(self, text = "w")
        self.x = QtWidgets.QToolButton(self, text = "x")
        self.line_4_hbox.addWidget(self.s)
        self.line_4_hbox.addWidget(self.t)
        self.line_4_hbox.addWidget(self.u)
        self.line_4_hbox.addWidget(self.v)
        self.line_4_hbox.addWidget(self.w)
        self.line_4_hbox.addWidget(self.x)
        

        self.line_5_hbox = QtWidgets.QHBoxLayout(self)
        self.line_5_group = QtWidgets.QGroupBox(self)
        self.line_5_group.setLayout(self.line_5_hbox)
        self.y = QtWidgets.QToolButton(self, text = "y")
        self.z = QtWidgets.QToolButton(self, text = "z")
        self.line_5_hbox.addWidget(self.y)
        self.line_5_hbox.addWidget(self.z)

        self.line_6_hbox = QtWidgets.QHBoxLayout(self)
        self.line_6_group = QtWidgets.QGroupBox(self)
        self.line_6_group.setLayout(self.line_6_hbox)
        self.one = QtWidgets.QToolButton(self, text = "1")
        self.two = QtWidgets.QToolButton(self, text = "2")
        self.three= QtWidgets.QToolButton(self, text = "3")
        self.four = QtWidgets.QToolButton(self, text = "4")
        self.five = QtWidgets.QToolButton(self, text = "5")
        self.line_6_hbox.addWidget(self.one)
        self.line_6_hbox.addWidget(self.two)
        self.line_6_hbox.addWidget(self.three)
        self.line_6_hbox.addWidget(self.four)
        self.line_6_hbox.addWidget(self.five)
    
        self.line_7_hbox = QtWidgets.QHBoxLayout(self)
        self.line_7_group = QtWidgets.QGroupBox(self)
        self.line_7_group.setLayout(self.line_7_hbox)
        self.six = QtWidgets.QToolButton(self, text = "6")
        self.seven = QtWidgets.QToolButton(self, text = "7")
        self.eight = QtWidgets.QToolButton(self, text = "8")
        self.nine = QtWidgets.QToolButton(self, text = "9")
        self.zero = QtWidgets.QToolButton(self, text = "0")
        self.line_7_hbox.addWidget(self.six)
        self.line_7_hbox.addWidget(self.seven)
        self.line_7_hbox.addWidget(self.eight)
        self.line_7_hbox.addWidget(self.nine)
        self.line_7_hbox.addWidget(self.zero)

        self.vbox.addWidget(self.line_1_group)
        self.vbox.addWidget(self.line_2_group)
        self.vbox.addWidget(self.line_3_group)
        self.vbox.addWidget(self.line_4_group)
        self.vbox.addWidget(self.line_5_group)
        self.vbox.addWidget(self.line_6_group)
        self.vbox.addWidget(self.line_7_group)

        self.setMaximumWidth(300)
        
class Animations(QtWidgets.QGroupBox):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.group = QtWidgets.QGroupBox(self)
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.group.setLayout(self.vbox)

        self.pacman = QtWidgets.QToolButton(self, text = "PacMan")
        self.vbox.addWidget(self.pacman)
        self.setMaximumWidth(300)
        

class LeftBox(QtWidgets.QGroupBox):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setContentsMargins(0,0,0,0)

        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        self.mode_label = QtWidgets.QLabel(self, text = "Mode")
        self.camera_button = QtWidgets.QToolButton(self, text = "Camera")
        self.camera_button.clicked.connect(self._OpenCamera)
        self.symbols_button = QtWidgets.QToolButton(self, text = "Symbols")
        self.symbols_button.clicked.connect(self._OpenSymbols)
        self.animation_button = QtWidgets.QToolButton(self, text = "Animations")
        self.animation_button.clicked.connect(self._OpenAnimations)

        self.camera = Camera(self)
        self.symbols = Symbols(self)
        self.animations = Animations(self)

        self.vbox.addWidget(self.mode_label)
        self.vbox.addWidget(self.camera_button)
        self.vbox.addWidget(self.symbols_button)
        self.vbox.addWidget(self.animation_button)
        self.vbox.addWidget(self.camera)
        self.vbox.addWidget(self.symbols)
        self.vbox.addWidget(self.animations)

        #self.symbols.hide()
        self.camera.hide()
        self.animations.hide()

        #self.setMaximumHeight(200)

    def _OpenSymbols(self):
        self.camera.__hide__()
        self.animations.hide()
        self.symbols.show()

    def _OpenCamera(self):
        self.camera.show()
        self.camera.__run__()
        self.animations.hide()
        self.symbols.hide()
    
    def _OpenAnimations(self):
        self.camera.__hide__()
        self.animations.show()
        self.symbols.hide()

class ViewBox(QtWidgets.QGroupBox):
    def __init__(self, parent = None):
        super().__init__(parent = parent)

        self.size = 55
        self.mass = []

        for i in range(8):
            temp = []
            for j in range(8):
                self.segment = QtWidgets.QLabel(self)
                self.segment.setPixmap(QtGui.QIcon("icons/white.svg").pixmap(self.size, self.size))
                
                self.segment.setMinimumHeight(self.size)
                self.segment.setMaximumHeight(self.size)
                self.segment.setMaximumWidth(self.size)
                self.segment.setMinimumWidth(self.size)
                self.segment.move(i * self.size, j * self.size)
                temp.append(self.segment)
            self.mass.append(temp)

    def __draw__(self, massive):
        print(1000)
        for i in range(8):
            for j in range(8):
                if(massive[i][j] == 255):
                    self.mass[j][i].setPixmap(QtGui.QIcon("icons/white.svg").pixmap(self.size, self.size))
                else:
                    self.mass[j][i].setPixmap(QtGui.QIcon("icons/black.svg").pixmap(self.size, self.size))
        QtTest.QTest.qWait(30)


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BioEye")

        self.main_groupbox = QtWidgets.QGroupBox()
        self.main_groupbox.setContentsMargins(0,0,0,0)

        self.main_hbox = QtWidgets.QHBoxLayout(self)
        self.main_hbox.setContentsMargins(0,0,0,0)
        self.main_groupbox.setLayout(self.main_hbox)

        self.leftbox = LeftBox(self)
        self.viewbox = ViewBox(self)
        self.main_hbox.addWidget(self.leftbox)
        self.main_hbox.addWidget(self.viewbox)

        self.setCentralWidget(self.main_groupbox)
        

app = QtWidgets.QApplication([])

qdarktheme.setup_theme()
gui = GUI()
gui.show()
sys.exit(app.exec())