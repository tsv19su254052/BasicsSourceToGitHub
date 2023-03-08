import pandas
import matplotlib.pyplot as plt
import numpy
import scipy.io
import sys
import os
#from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt import FigureCanvasQT as FigureCanvas
from matplotlib.figure import Figure
#from PyQt4.QtGui import *
#from PyQt4 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets


plt.style.use('ggplot')


def Extract_Data(name):
    #setting up lists
    Stim_trig = []
    Stim_order = []
    Sch_wav = []
    data = scipy.io.loadmat(name)
    for k, v in data.items():
        #Sends Sch_wav data to a list
        if "Sch_wav" in k:
            for d in (((v[0])[0])[4]):
                Sch_wav.append(d[0])
        #Sends StimTrig to a list
        if k=="StimTrig":
            for g in (((v[0])[0])[4]):
                Stim_trig.append(g[0])
            Stim_trig.append(Stim_trig[-1]+1)
        #Sends Stim order to a list
            for w in (((v[0])[0])[5]):
                Stim_order.append(w[0])
    superdata = []
    #Prepares grouping stimuli and trigger
    for i in range(len(Stim_trig)-1):
        fire = []
        for p in Sch_wav:
            if p > Stim_trig[i] and p < Stim_trig[i+1]:
                fire.append(p - Stim_trig[i])
        superdata.append([Stim_order[i],fire])
    #sorts all the data
    superdata.sort()
    alladdedup = list[list[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[62]]
    count = 0
    for d in superdata:
        if d[0] == (alladdedup[count])[0]:
            for j in d[1]:
                ((alladdedup)[count]).append(j)
        else:
            count += 1
    #places time stamps of triggers in lists for each trigger
    for l in alladdedup:
        l.pop(0)
        l.sort()
        #removes title and sorts data
    ffmsb = []
    #finds number of firings for each milisecond bin
    for v in alladdedup:
        fmsb = []
        for b in range(1000):
            msbc = b/1000
            msb = []
            for t in v:
                if t > msbc and t < msbc + 0.001:
                    msb.append(t)
            fmsb.append(len(msb))
        ffmsb.append(fmsb)
    #returns list of stimuli firings per milisecond bin
    return(ffmsb)


class DisplayWidget(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(DisplayWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.main_frame = QtWidgets.QWidget()
        self.canvas = PlotCanvas(self)
        self.canvas.setParent(self.main_frame)
        self.one = QtWidgets.QPushButton('Intensity 1')
        self.two = QtWidgets.QPushButton('Intensity 2')
        self.three = QtWidgets.QPushButton('Intensity 3')
        self.four = QtWidgets.QPushButton('Intensity 4')
        self.five = QtWidgets.QPushButton('Intensity 5')
        self.six = QtWidgets.QPushButton('Intensity 6')
        self.seven = QtWidgets.QPushButton('Intensity 7')
        self.eight = QtWidgets.QPushButton('Intensity 8')
        self.nine = QtWidgets.QPushButton('Intensity 9')
        self.ten = QtWidgets.QPushButton('Intensity 10')
        self.one.connect(self.one, QtCore.SIGNAL('clicked()'), self.setIntensity_one)
        self.two.connect(self.two, QtCore.SIGNAL('clicked()'), self.setIntensity_two)
        self.three.connect(self.three, QtCore.SIGNAL('clicked()'), self.setIntensity_three)
        self.four.connect(self.four, QtCore.SIGNAL('clicked()'), self.setIntensity_four)
        self.five.connect(self.five, QtCore.SIGNAL('clicked()'), self.setIntensity_five)
        self.six.connect(self.six, QtCore.SIGNAL('clicked()'), self.setIntensity_six)
        self.seven.connect(self.seven, QtCore.SIGNAL('clicked()'), self.setIntensity_seven)
        self.eight.connect(self.eight, QtCore.SIGNAL('clicked()'), self.setIntensity_eight)
        self.nine.connect(self.nine, QtCore.SIGNAL('clicked()'), self.setIntensity_nine)
        self.ten.connect(self.ten, QtCore.SIGNAL('clicked()'), self.setIntensity_ten)
        grid = QtGui.QGridLayout()
        grid.addWidget(self.canvas, 1, 0, 10, 10)  # the matplotlib canvas
        grid.addWidget(self.one, 0, 0)
        grid.addWidget(self.two, 0, 1)
        grid.addWidget(self.three, 0, 2)
        grid.addWidget(self.four, 0, 3)
        grid.addWidget(self.five, 0, 4)
        grid.addWidget(self.six, 0, 5)
        grid.addWidget(self.seven, 0, 6)
        grid.addWidget(self.eight, 0, 7)
        grid.addWidget(self.nine, 0, 8)
        grid.addWidget(self.ten, 0, 9)
        self.main_frame.setLayout(grid)
        self.setCentralWidget(self.main_frame)
        self.setWindowTitle('Neurons')
        self.showMaximized()

    def setIntensity_one(self):
        self.data(intensity = 1)

    def setIntensity_two(self):
        self.data(intensity = 2)

    def setIntensity_three(self):
        self.data(intensity = 3)

    def setIntensity_four(self):
        self.data(intensity = 4)

    def setIntensity_five(self):
        self.data(intensity = 5)

    def setIntensity_six(self):
        self.data(intensity = 6)

    def setIntensity_seven(self):
        self.data(intensity = 7)

    def setIntensity_eight(self):
        self.data(intensity = 8)

    def setIntensity_nine(self):
        self.data(intensity = 9)

    def setIntensity_ten(self):
        self.data(intensity = 10)

    def data(self, intensity):
        stimuli = (Extract_Data("654508_rec02_all.mat")[intensity])
        numberlist = []
        for i in range(1000):
            numberlist.append(i/1000)
        d = pandas.Series(stimuli, index = numberlist)
        self.df = pandas.DataFrame(d)
        self.axes.cla()
        self.canvas.plot_data_frame(self.df)


class PlotCanvas(FigureCanvas, DisplayWidget):
    def __init__(self, parent = None, width = 12, height = 9):
        self.fig = Figure(figsize = (width, height))
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtCore.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot_data_frame(self, df):
        df.plot( ax = self.axes,
            kind = 'line',
            title = 'Number of neurons firing',
            legend = False,
            xlim = (0, 1))
        self.draw()


if __name__ == "__main__":
    #app = QtWidgets.QApplication([])
    app = QtWidgets.QApplication(sys.argv)
    widget = DisplayWidget()
    widget.show()
    app.exec_()
