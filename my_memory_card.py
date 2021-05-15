#создай приложение для запоминания информации
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox

#Создание окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

#Создание объектов
question = QLabel('Какой национальности не существует?')
reply = QPushButton('Ответить')

#Создание линий окна
v_line = QVBoxLayout()
h1_line = QHBoxLayout()
h2_line = QHBoxLayout()

#Первый групбокс
RadioGroupBox1 = QGroupBox('Варианты ответов')

answer1 = QRadioButton('Энцы')
answer2 = QRadioButton('Смурфы')
answer3 = QRadioButton('Чулымцы')
answer4 = QRadioButton('Алеуты')


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()



layout_ans2.addWidget(answer1)
layout_ans2.addWidget(answer2)
layout_ans3.addWidget(answer3)
layout_ans3.addWidget(answer4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox1.setLayout(layout_ans1)
 

#Второй групбокс
RadioGroupBox2 = QGroupBox('Результаты теста')
ver_never = QLabel('Правильно/Неправильно')
verno = QLabel('Правильно')
neverno = QLabel('Неправильно')


layout_ver = QVBoxLayout()
layout_ver_never = QHBoxLayout()
layout_help = QHBoxLayout()


layout_ver_never.addWidget(ver_never, alignment = Qt.AlignLeft)
layout_ver.addWidget(verno)
layout_ver.addWidget(neverno)


layout_ver.addLayout(layout_ver_never)
layout_ver.addLayout(layout_help)


RadioGroupBox2.setLayout(layout_ver)

#Склабывание всего на линии на экране
h1_line.addWidget(question, alignment = Qt.AlignHCenter)
v_line.addLayout(h1_line)
v_line.addWidget(RadioGroupBox1, alignment = Qt.AlignVCenter)
v_line.addWidget(RadioGroupBox2, alignment = Qt.AlignVCenter)
v_line.addWidget(reply, alignment = Qt.AlignVCenter)

#Обработчик событий 1
RadioGroupBox2.hide()
def show_result():
    RadioGroupBox1.hide()
    RadioGroupBox2.show()
    reply.setText('Следующий вопрос')
reply.clicked.connect(show_result)

#Обработчик событий 2
def show_question():
    RadioGroupBox2.hide()
    RadioGroupBox1.show()
    reply.setText('Ответить')
    RadioGroupBox1.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroupBox1.setExclusive(True)
reply.clicked.connect(show_question)

#Обработчик событий 3
def start_test():
    if reply.text == 'Ответить' :
        show_results
    else: reply.text == 'Следующий вопрос' 
        show_question


#ask()
def ask(question, r_answer, b_answer2, b_answer3, b_answer4):
    answer[1].setText('r_answer')
    answer[2].setText('b_answer2')
    answer[3].setText('b_answer3')
    answer[4].setText('b_answer4')
    answers = [r_answer, b_answer2, b_answer3, b_answer4]
    shuffle(answers)
'''

#chek_answer()
def check_answer():
    if r_answer.isChecked == True :
        pass
    else r_answer.isChecked == False :
        pass

def show_correct(res):
    pass'''


#Конец
main_win.setLayout(v_line)
main_win.show()
app.exec_()