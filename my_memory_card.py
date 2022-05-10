#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QPushButton, QMessageBox,QButtonGroup, QHBoxLayout, QWidget, QRadioButton, QLabel, QVBoxLayout
from random import randint
for random import shuffle
#создание приложения и главнго окна

app = QApplication([])

btn_OK = QPushButton('Ответить')
question = QLabel('вопрос1')

RadioGroupBox = QGroupBox('Варианты ответов:')

btn_answer1 = QRadioButton('ответ1')
btn_answer2 = QRadioButton('ответ2')
btn_answer3 = QRadioButton('ответ3')
btn_answer4 = QRadioButton('ответ4')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

layoutH1 = QHBoxLayout()   
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout()
layoutH2.addWidget(btn_answer1) 
layoutH2.addWidget(btn_answer2)
layoutH3.addWidget(btn_answer3) 
layoutH3.addWidget(btn_answer4)
 
layoutH1.addLayout(layoutH2)
layoutH1.addLayout(layoutH3)
RadioGroupBox.setLayout(layoutH1)
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана

def start_test():
    if 'Ответ' == obg.test():
        show_result()
    else:
        show_question()
obg.clicked.connect(start_test)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].serText(wrong2)
    answers[3].serText(wrong3)
    lb_Question.serText(question)
    lb_Correct.setText(right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')


main_win = QWidget()
#отображение окна приложения
main_win.setWindowTitle('чебурашка')
main_win.setLayout(layout_card)
main_win.show()
app.exec()