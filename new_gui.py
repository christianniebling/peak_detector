import sys
from PyQt5.QtWidgets import QApplication, QGraphicsWidget, QMainWindow, QFileDialog
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


    def initUI(self):
        self.ui.button1.clicked.connect(self.button1_clicked)
        self.ui.button2.clicked.connect(self.button2_clicked)
        self.ui.button3.clicked.connect(self.button3_clicked)
        self.ui.button4.clicked.connect(self.button4_clicked)
        self.region = pyqtgraph.LinearRegionItem(brush=(225, 225, 0), hoverBrush=(225, 0, 225), pen={'color': 'r', 'width': 10}, hoverPen='b')
        self.ui.graph_widget.addItem(self.region)
        self.ui.file_location_box.setPlainText("data/TEST.acq")

        # self.ui.graph_widget.scene().sigMouseMoved.connect(self.mouseMovedEvent)
        # self.ui.graph_widget.scene().sigMouseClicked.connect(self.mouseClickedEvent)
        # TODO: set the brush
        # self.region.setBrush((225,225,0), width=10)

    def button1_clicked(self):
        self.myHRV.init_data()
        self.myHRV.compute()
        self.ui.output_box_1.append(self.myHRV.print_s())
        self.ui.graph_widget.plot(self.myHRV.time, self.myHRV.ECG_data)

    def button2_clicked(self):
        self.myHRV.set_region(self.region.getRegion())

    def button3_clicked(self):
        # TODO: make sure it only opens the correct files or promts the user at least
        fname = QFileDialog.getOpenFileName(self, 'Open ECG file')
        self.ui.file_location_box.setPlainText(fname[0])
        self.myHRV.set_input_file(fname[0])

    def button4_clicked(self):
        pulled_text = self.ui.file_location_box.toPlainText()
        self.myHRV.set_input_file(pulled_text)


    def mouseMovedEvent(self):
        print('moved')
 
    def mouseClickedEvent(self):
        print('meow')



app = QApplication(sys.argv)
window = HRV_GUI()
window.show()
sys.exit(app.exec_())
