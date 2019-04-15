import sys
from PyQt5 import QtWidgets
from main import Ui_MainWindow

#Main fonksiyonu programın hayatına başladığı yerdir
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
