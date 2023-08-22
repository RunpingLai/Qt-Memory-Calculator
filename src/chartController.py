import sys
import re
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,\
                            QLineEdit, QLabel, QPushButton,\
                            QFileDialog, QHBoxLayout, QGridLayout,\
                            QMessageBox, QSizePolicy)
from PyQt5.QtChart import QChart, QPieSeries, QChartView
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtCore import pyqtSignal, QObject, pyqtProperty

class myChart(QObject):
    # dataChanged = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._usedMem = 0
        self._totalMem = 1
        self._usedTLS = 0
        self._totalTLS = 1
        self._usedFIB = 0
        self._totalFIB = 1
        self.chartTotal, self.seriesTotal, self.chartTotal_view,\
            self.chartTLS, self.seriesTLS, self.chartTLS_view,\
            self.chartFIB, self.seriesFIB, self.chartFIB_view = self._init_chart()
        # self._update_chart()

    # Mem
    @property
    def usedMem(self):
        return self._usedMem
    
    @usedMem.setter
    def usedMem(self, value):
        self._usedMem = value
        self._update_chart()

    @property
    def totalMem(self):
        return self._totalMem
    
    @totalMem.setter
    def totalMem(self, value):
        self._totalMem = value
        self._update_chart()


    # TLS
    @property
    def usedTLS(self):
        return self._usedTLS
    
    @usedTLS.setter
    def usedTLS(self, value):
        self._usedTLS = value
        self._update_chart()

    @property
    def totalTLS(self):
        return self._totalTLS
    
    @totalTLS.setter
    def totalTLS(self, value):
        self._totalTLS = value
        self._update_chart()


    # FIB
    @property
    def usedFIB(self):
        return self._usedFIB
    
    @usedFIB.setter
    def usedFIB(self, value):
        self._usedFIB = value
        self._update_chart()

    @property
    def totalFIB(self):
        return self._totalFIB
    
    @totalFIB.setter
    def totalFIB(self, value):
        self._totalFIB = value
        self._update_chart()

    def _init_chart(self):

        # Mem
        seriesTotal = QPieSeries()
        unusedMem = self._totalMem - self._usedMem
        seriesTotal.append("Used Memory", self._usedMem)
        seriesTotal.append("Unused Memory", unusedMem)
        chartTotal = QChart()
        chartTotal.addSeries(seriesTotal)
        chartTotal.setTitle(f"Memory Usage: {self._usedMem}MB / {self._totalMem}MB")
        chartTotal_view = QChartView(chartTotal)
        chartTotal_view.setRenderHint(QPainter.Antialiasing)

        # TLS
        seriesTLS = QPieSeries()
        unusedTLS = self._totalTLS - self._usedTLS
        seriesTLS.append("Used TLS", self._usedTLS)
        seriesTLS.append("Unused TLS", unusedTLS)
        chartTLS = QChart()
        chartTLS.addSeries(seriesTLS)
        chartTLS.setTitle(f"TLS Usage: {self._usedTLS}MB / {self._totalTLS}MB")
        chartTLS_view = QChartView(chartTLS)
        chartTLS_view.setRenderHint(QPainter.Antialiasing)

        # FIB
        seriesFIB = QPieSeries()
        unusedFIB = self._totalFIB - self._usedFIB
        seriesFIB.append("Used FIB", self._usedFIB)
        seriesFIB.append("Unused FIB", unusedFIB)
        chartFIB = QChart()
        chartFIB.addSeries(seriesFIB)
        chartFIB.setTitle(f"FIB Usage: {self._usedFIB}MB / {self._totalFIB}MB")
        chartFIB_view = QChartView(chartFIB)
        chartFIB_view.setRenderHint(QPainter.Antialiasing)

        return chartTotal, seriesTotal, chartTotal_view,\
                chartTLS, seriesTLS, chartTLS_view,\
                chartFIB, seriesFIB, chartFIB_view
    
    def _update_chart(self):
        self.seriesTotal = QPieSeries()
        unusedMem = self._totalMem - self._usedMem
        self.seriesTotal.append("Used Memory", self._usedMem)
        self.seriesTotal.append("Unused Memory", unusedMem)
        self.chartTotal.setTitle(f"Memory Usage: {self._usedMem}MB / {self._totalMem}MB")
        self.chartTotal.removeAllSeries()
        self.chartTotal.addSeries(self.seriesTotal)

        self.seriesTLS = QPieSeries()
        unusedTLS = self._totalTLS - self._usedTLS
        self.seriesTLS.append("TLS", self._usedTLS)
        self.seriesTLS.append("Rest of Services", unusedTLS)
        self.chartTLS.setTitle(f"TLS/Serives Usage: {self._usedTLS}MB / {self._totalTLS}MB")
        self.chartTLS.removeAllSeries()
        self.chartTLS.addSeries(self.seriesTLS)

        self.seriesFIB = QPieSeries()
        unusedFIB = self._totalFIB - self._usedFIB
        self.seriesFIB.append("FIB", self._usedFIB)
        self.seriesFIB.append("Rest of Kernel-Heap", unusedFIB)
        self.chartFIB.setTitle(f"FIB/Kernel-Heap Usage: {self._usedFIB}MB / {self._totalFIB}MB")
        self.chartFIB.removeAllSeries()
        self.chartFIB.addSeries(self.seriesFIB)