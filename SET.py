# Sensor End Terminal

import sys, os
import csv
import json
import socket
from random import randint
from PyQt5 import QtGui, QtWidgets, uic



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('SET_UI.ui', self)
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.setWindowTitle("Sensor End Terminal")
        self.setFixedSize(913, 547)

        self.findUiDetails()
        self.show()

    def findUiDetails(self):

        self.button_edit = self.findChild(QtWidgets.QPushButton, 'button_edit')  # Find the button
        self.button_edit.clicked.connect(self.setup)  # Remember to pass the definition/method, not the return value!

        self.button_importCSV = self.findChild(QtWidgets.QPushButton, 'button_importCSV')  # Find the button
        self.button_importCSV.clicked.connect(self.importFromCSV)

        self.button_exportToCSV = self.findChild(QtWidgets.QPushButton, 'button_exportToCSV')  # Find the button
        self.button_exportToCSV.clicked.connect(self.setup)

        self.button_prev = self.findChild(QtWidgets.QPushButton, 'button_prev')  # Find the button
        self.button_prev.clicked.connect(self.setup)

        self.button_next = self.findChild(QtWidgets.QPushButton, 'button_next')  # Find the button
        self.button_next.clicked.connect(self.setup)

        self.button_save = self.findChild(QtWidgets.QPushButton, 'button_save')  # Find the button
        self.button_save.clicked.connect(self.setup)

        self.button_tx = self.findChild(QtWidgets.QPushButton, 'button_tx')  # Find the button
        self.button_tx.clicked.connect(self.setup)

        self.lineEdit_1 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_1')
        self.lineEdit_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        self.lineEdit_3 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_3')
        self.lineEdit_4 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        self.lineEdit_5 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_5')
        self.lineEdit_6 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_6')
        self.lineEdit_7 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_7')

        self.lineEdit_sensor_id = self.findChild(QtWidgets.QLineEdit, 'lineEdit_sensor_id')

        self.lineEdit_TGT_LOC_1 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_TGT_LOC_1')
        self.lineEdit_TGT_LOC_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_TGT_LOC_2')
        self.lineEdit_TGT_LOC_3 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_TGT_LOC_3')

        self.lineEdit_TGT_TYPE_1 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_TGT_TYPE_1')
        self.comboBox_TGT_TYPE = self.findChild(QtWidgets.QComboBox, 'comboBox_TGT_TYPE')
        self.comboBox_TGT_TYPE.setCurrentIndex(1)

        self.lineEdit_MOVE_1 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_MOVE_1')
        self.lineEdit_MOVE_2 = self.findChild(QtWidgets.QLineEdit, 'lineEdit_MOVE_2')
        self.lineEdit_MOVE_FROM = self.findChild(QtWidgets.QLineEdit, 'lineEdit_MOVE_FROM')
        self.lineEdit_MOVE_TO = self.findChild(QtWidgets.QLineEdit, 'lineEdit_MOVE_TO')

        self.lineEdit_Assessment = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Assessment')

        self.lineEdit_Remarks = self.findChild(QtWidgets.QLineEdit, 'lineEdit_Remarks')

        self.comboBox_TGT_ID_1 = self.findChild(QtWidgets.QComboBox, 'comboBox_TGT_ID_1')
        self.comboBox_TGT_ID_1.setCurrentIndex(1)

        self.pushButton_Attachment = self.findChild(QtWidgets.QLineEdit, 'pushButton_Attachment')

    def setup(self):

        if self.comboBox_TGT_TYPE.currentText() == 'Select Option Here' or \
                self.comboBox_TGT_ID_1.currentText() == 'Select Option Here':
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Selection Missing")
            msg.setText("Please Select form drop down option(s)")
            # msg.setIcon(QtWidgets.QMessageBox.warning(QtWidgets.QPushButton, "input", "input"))
            x = msg.exec_()
        else:
            global SET_dict
            SET_dict = {self.lineEdit_1.text(): self.lineEdit_sensor_id.text(),

                        "TGT_LOC 1": self.lineEdit_TGT_LOC_1.text(),
                        "TGT_LOC 2": self.lineEdit_TGT_LOC_2.text(),
                        "TGT_LOC 3": self.lineEdit_TGT_LOC_3.text(),

                        "TGT_TYPE_1": self.lineEdit_TGT_TYPE_1.text(),
                        "TGT_TYPE_OPTION": self.comboBox_TGT_TYPE.currentText(),

                        "MOVE_1": self.lineEdit_MOVE_1.text(),
                        "MOVE_2": self.lineEdit_MOVE_2.text(),
                        "MOVE FROM": self.lineEdit_MOVE_FROM.text(),
                        "MOVE TO": self.lineEdit_MOVE_TO.text(),

                        self.lineEdit_5.text(): self.lineEdit_Assessment.text(),
                        self.lineEdit_6.text(): self.lineEdit_Remarks.text(),
                        self.lineEdit_7.text(): self.comboBox_TGT_ID_1.currentText(),

                        }
            # print(SET_dict)

            # for key, value in SET_dict.items():
            #     print(key, value)

    # --------------------------------------------------
    # Transfer function
    def Transfer(self):
        pass

    def importFromCSV(self):
        # os.system('explorer.exe "C:/"')

        header = [
            ' SENSOR ID',
            'TGT_LOC 1',
            'TGT_LOC 2',
            'TGT_LOC 3',
            'TGT_TYPE_1',
            'TGT_TYPE_OPTION',
            'MOVE_1',
            'MOVE_2',
            'MOVE FROM',
            'MOVE TO',
            ' ASSESSMENT',
            ' REMARKS',
            ' TGT ID'
        ]


        tolist = [SET_dict]
        # print(tolist)


        # with open('Names.csv', 'a', newline='') as csvfile:
        #     print(csvfile.readline(self,1))

            # csvfile.seek(0)
            # head = f.readline()
            # print('printing header \n')
            # print(head)
            # csvfile.close()
            # writer = csv.DictWriter(csvfile, fieldnames=header)
            # if header
            # writer.writeheader()
            # writer.writerows(tolist)
            # csvfile.close()

        f = open('Names.csv', 'r')

        head = f.readline()
        list = [head]

       # // print(list[0])

        for x in list:
            global first
            first = x
            break

        # print(first)


app = QtWidgets.QApplication(sys.argv)
window = Ui()

app.exec_()
# ----------------------------------------

# ----------------------------------------
# edit = QtWidgets.QPushButton('button_edit')
# edit.setText("NSg")

# dir_path = QFileDialog.getExistingDirectory(self, "Choose Directory", "E:\\")
# os.system('explorer.exe "C:/users/%username%/Desktop/"')



# def keyPressEvent(self, e):
#     if e.key() == Qt.Key_Escape:
#         self.close()


# def mouseMoveEvent(self, e):
#     x = e.x()
#     y = e.y()
#
#     text = f'x: {x},  y: {y}'
#     self.label.setText(text)


# self.lineEdit_2.text(): {"TGT_LOC 1": self.lineEdit_TGT_LOC_1.text(),
#                                                  "TGT_LOC 2": self.lineEdit_TGT_LOC_2.text(),
#                                                  "TGT_LOC 3": self.lineEdit_TGT_LOC_3.text()},
#
#                         self.lineEdit_3.text(): {"TGT_TYPE_1": self.lineEdit_TGT_TYPE_1.text(),
#                                                  "TGT_TYPE_OPTION": self.comboBox_TGT_TYPE.currentText()},
#
#
#                         self.lineEdit_4.text(): {"MOVE_1": self.lineEdit_MOVE_1.text(),
#                                                  "MOVE_2": self.lineEdit_MOVE_2.text(),
#                                                  "MOVE FROM": self.lineEdit_MOVE_FROM.text(),
#                                                  "MOVE TO": self.lineEdit_MOVE_TO.text()},

#
# for key, value in SET_dict.items():
#     list = [key, value]
#     csv_writer.writerow(list)
