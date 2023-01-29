import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from form import Ui_MainWindow
from TimeDomainHRV import TimeDomainHRV

class HRV_GUI(QMainWindow):
    def __init__(self):
        super(HRV_GUI, self).__init__()

        # Set up ui from designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

        # Create our HRV instance
        self.myHRV = TimeDomainHRV()
        self.myHRV.compute()


    def initUI(self):
        self.ui.button1.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.ui.output_box_1.append(self.myHRV.print_s())
        self.ui.output_box_1.append('RICE')

 



app = QApplication(sys.argv)
window = HRV_GUI()
window.show()
sys.exit(app.exec_())
