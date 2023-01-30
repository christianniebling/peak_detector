import sys
from PyQt5.QtWidgets import QApplication, QGraphicsWidget, QMainWindow
from pyqtgraph import PlotWidget, plot
from form import Ui_MainWindow
from TimeDomainHRV import TimeDomainHRV
import pyqtgraph as pg
from main import Time, ECG_Data

class HRV_GUI(QMainWindow):
    def __init__(self):
        super(HRV_GUI, self).__init__()

        # Set up ui from designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        # self.ui.graph_widget.plot(hour, temperature)

        self.initUI()

        # Create our HRV instance
        self.myHRV = TimeDomainHRV()
        self.myHRV.compute()


    def initUI(self):
        self.ui.button1.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.ui.output_box_1.append(self.myHRV.print_s())
        self.ui.output_box_1.append('RICE')
        self.ui.graph_widget.plot(Time, ECG_Data)

 



app = QApplication(sys.argv)
window = HRV_GUI()
window.show()
sys.exit(app.exec_())
