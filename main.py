from PyQt5.QtWidgets import (QApplication, QWidget,QLabel,QPushButton,QTabWidget,QSlider,QSpinBox,
                             QVBoxLayout,QHBoxLayout,QLineEdit,QListWidget,QComboBox,QProgressBar, QDial)

from PyQt5.QtCore import Qt 

app = QApplication([])
window = QWidget()


window.resize(500,500)
window.move(460,125)

line = QLineEdit()
b1 = QPushButton("1")
b2 = QPushButton("2")
b3 = QPushButton("3")
b4 = QPushButton("4")
b5 = QPushButton("5")
b6 = QPushButton("6")
b7 = QPushButton("7")
b8 = QPushButton("8")
b9 = QPushButton("9")
b10 = QPushButton("0")
b11 = QPushButton("+")
b12 = QPushButton("-")
b13 = QPushButton("=")
b14 = QPushButton("*")
b15 = QPushButton("/")
b16 = QPushButton("C")

v = QVBoxLayout()

h1 = QHBoxLayout()
h1.addWidget(b1)
h1.addWidget(b4)
h1.addWidget(b7)
h1.addWidget(b10)

h2 = QHBoxLayout()
h2.addWidget(b2)
h2.addWidget(b5)
h2.addWidget(b8)
h2.addWidget(b15)

h3 = QHBoxLayout()
h3.addWidget(b3)
h3.addWidget(b6)
h3.addWidget(b9)
h3.addWidget(b16)

h4 = QHBoxLayout()
h4.addWidget(b11)
h4.addWidget(b12)
h4.addWidget(b14)
h4.addWidget(b13)

v.addWidget(line)
v.addLayout(h1)
v.addLayout(h2)
v.addLayout(h3)
v.addLayout(h4)

window.setLayout(v)
window.show()
app.exec()