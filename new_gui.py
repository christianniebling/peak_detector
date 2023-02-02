import sys
from PyQt5.QtWidgets import QApplication, QGraphicsWidget, QMainWindow
from pyqtgraph import PlotWidget, plot
import pyqtgraph
from form import Ui_MainWindow
from TimeDomainHRV import TimeDomainHRV
import pyqtgraph as pg

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
        self.ui.button1.clicked.connect(self.button1_clicked)
        self.ui.button2.clicked.connect(self.button2_clicked)
        self.region = pyqtgraph.LinearRegionItem()
        self.ui.graph_widget.addItem(self.region)

        #brush = pyqtgraph.mkBrush
        self.region.setBrush((255, 255, 0))

    def button1_clicked(self):
        self.ui.output_box_1.append(self.myHRV.print_s())
        self.ui.graph_widget.plot(self.myHRV.time, self.myHRV.ECG_data)

    def button2_clicked(self):
        print(self.region.getRegion())

 



app = QApplication(sys.argv)
window = HRV_GUI()
window.show()
sys.exit(app.exec_())
