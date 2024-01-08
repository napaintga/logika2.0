from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
from PyQt5.QtCore import Qt

app = QApplication([])
 
#головне вікно:
my_win = QWidget()
my_win.setWindowTitle('Лотерея')
my_win.move(100, 100)
my_win.resize(400, 200)


#віджети вікна: кнопка та напис
button = QPushButton('Випробувати удачу')
text = QLabel('Натисни, щоб взяти участь')
number1 = QLabel('?')
number2 = QLabel('?')


#розташування віджетів
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(number1, alignment = Qt.AlignCenter)
line.addWidget(number2, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)
 
#функція, яка генерує та показує числа
def start_lottery():
    n1 = randint(0, 9)
    n2 = randint(0, 9)
    number1.setText(str(n1))
    number2.setText(str(n2))
    if n1 == n2:
        text.setText('Ви виграли! Зіграйте знову')
    else:
        text.setText('Ви програли! Зіграйте знову')
 
#обробка натискання на кнопку
button.clicked.connect(start_lottery)


my_win.show()
app.exec_()
