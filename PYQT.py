import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class App(QWidget):
        def     __init__(self):
                super().__init__()
                self.title='Hello World AI'
                self.showMaximized()
                self.initUI()

        def initUI(self):
                self.setWindowTitle(self.title)
                self.showMaximized()
                self.show()

if __name__=='__main__':
        app=QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec())



#reference website https://pythonspot.com/pyqt5-buttons/