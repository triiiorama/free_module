import sys
from PyQt5 import QtWidgets
# Импортируем наш интерфейс из файла
from free_modules_gui import *
from free_modules import *


class GUI(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# События нажатия на кнопку
		self.ui.pushButton.clicked.connect(self.get_free_modules_here)
    
    # Функция которая выполняется при нажатии на кнопку
	def get_free_modules_here(self):
		module = self.ui.lineEdit.text()
		modules = get_free_modules(module)
		self.ui.textEdit_2.setText(modules)

  
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mywin = GUI()
	mywin.show()
	sys.exit(app.exec_())
