import sys
from PyQt5.QtWidgets import QApplication, QGraphicsWidget, QMainWindow, QFileDialog
from pyqtgraph import PlotWidget, plot
import pyqtgraph
from form import Ui_MainWindow
import graph
from TimeDomainHRV import TimeDomainHRV
import pyqtgraph as pg
import defaults

# This value has to take into account the sliders min/max values
SLIDE_SCALE_FACTOR = 100

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
        # TODO: look into creating lambda functions to reduce methods created
        self.ui.button1.clicked.connect(self.button1_clicked)
        self.ui.button2.clicked.connect(self.button2_clicked)
        self.ui.button3.clicked.connect(self.button3_clicked)
        self.ui.button4.clicked.connect(self.button4_clicked)
        self.ui.button5.clicked.connect(self.button5_clicked)
        self.region = pyqtgraph.LinearRegionItem(brush=(255, 251, 100, 140) , hoverBrush=(225, 40, 40, 140), pen={'color': (255, 89, 89, 200), 'width': 5}, hoverPen='r')
        self.ui.graph_widget.addItem(self.region)
        self.ui.file_location_box.setPlainText(defaults.ecg_file_path) # todo: const file
        self.region.sigRegionChanged.connect(self.region_selection_change)

        # Setup for tab2 
        self.ui.slider1.setValue(defaults.BP_height)
        self.ui.slider1_box.setValue(defaults.BP_height)
        self.ui.slider2.setValue(defaults.BP_distance)
        self.ui.slider2_box.setValue(defaults.BP_distance)
        # Sliders dont take floats? :(
        self.ui.slider3.setValue(int(defaults.ECG_height * SLIDE_SCALE_FACTOR))  
        self.ui.slider3_box.setValue(defaults.ECG_height)
        self.ui.slider4.setValue(defaults.ECG_distance)
        self.ui.slider4_box.setValue(defaults.ECG_distance)
        self.ui.slider1.valueChanged.connect(self.slider1_moved)
        self.ui.slider1_box.valueChanged.connect(self.slider1_box_changed)
        self.ui.slider2.valueChanged.connect(self.slider2_moved)
        self.ui.slider2_box.valueChanged.connect(self.slider2_box_changed)
        self.ui.slider3.valueChanged.connect(self.slider3_moved)
        self.ui.slider3_box.valueChanged.connect(self.slider3_box_changed)
        self.ui.slider4.valueChanged.connect(self.slider4_moved)
        self.ui.slider4_box.valueChanged.connect(self.slider4_box_changed)

    def button1_clicked(self):
        self.myHRV.calculate_peaks()
        self.myHRV.compute()
        self.ui.output_box_1.append(self.myHRV.print_s())
        self.ui.graph_widget.plot(self.myHRV.time, self.myHRV.ECG_data)
        # self.ui.graph_widget.plot(self.myHRV.peaks, self.myHRV.ECG_data[self.myHRV.peaks], symbol = 'x')

    def button2_clicked(self):
        r = self.region.getRegion()
        if (r[0] < self.myHRV.time[0] or r[1] > self.myHRV.time[-1]):
            self.ui.output_box_1.append("Region selected is out of bounds of the signal. Please select a valid region of time.")
        else:
            self.myHRV.set_region(r)
            self.ui.output_box_1.append("Region set from: " + str(r[0]) + " to: " + str(r[1]))

    def button3_clicked(self):
        # TODO: make sure it only opens the correct files or promts the user at least
        fname = QFileDialog.getOpenFileName(self, 'Open ECG file')
        self.ui.file_location_box.setPlainText(fname[0])
        self.myHRV.set_input_file(fname[0])

    def button4_clicked(self):
        pulled_text = self.ui.file_location_box.toPlainText()
        self.myHRV.set_input_file(pulled_text)
    
    def button5_clicked(self):
        # new_window = QMainWindow
        # temp = graph.Ui_MainWindow()
        # temp.setupUi(new_window)
        # new_window.show()

        print('sefs')

    def slider1_moved(self):
        self.ui.slider1_box.setValue(self.ui.slider1.value())
        self.myHRV.set_BP_height(self.ui.slider1.value())

    def slider1_box_changed(self):
        self.ui.slider1.setValue(self.ui.slider1_box.value())
        self.myHRV.set_BP_height(self.ui.slider1_box.value())

    def slider2_moved(self):
        self.ui.slider2_box.setValue(self.ui.slider2.value())
        self.myHRV.set_BP_distance(self.ui.slider2.value())

    def slider2_box_changed(self):
        self.ui.slider2.setValue(self.ui.slider2_box.value())
        self.myHRV.set_BP_distance(self.ui.slider2_box.value())

    def slider3_moved(self):
        self.ui.slider3_box.setValue(self.ui.slider3.value() / SLIDE_SCALE_FACTOR)
        self.myHRV.set_ECG_height(self.ui.slider3.value() / SLIDE_SCALE_FACTOR)

    def slider3_box_changed(self):
        self.ui.slider3.setValue(int(self.ui.slider3_box.value() * SLIDE_SCALE_FACTOR))
        self.myHRV.set_ECG_height(self.ui.slider3_box.value())

    def slider4_moved(self):
        self.ui.slider4_box.setValue(self.ui.slider4.value())
        self.myHRV.set_ECG_distance(self.ui.slider4.value())

    def slider4_box_changed(self):
        self.ui.slider4.setValue(self.ui.slider4_box.value())
        self.myHRV.set_ECG_distance(self.ui.slider4_box.value())

    def region_selection_change(self):
        r = self.region.getRegion()
        self.ui.label_10.setText(str(r[0]))
        self.ui.label_11.setText(str(r[1]))
    
app = QApplication(sys.argv)
window = HRV_GUI()
window.show()
sys.exit(app.exec_())
