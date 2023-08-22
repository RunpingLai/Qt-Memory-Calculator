from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,\
                            QLineEdit, QLabel, QPushButton,\
                            QFileDialog, QHBoxLayout, QGridLayout,\
                            QMessageBox, QSizePolicy, QTextEdit)
from PyQt5.QtChart import QChart, QPieSeries, QChartView
from PyQt5.QtGui import QPainter, QPixmap, QPalette
from PyQt5.QtCore import Qt



def init(app):
    # creating labels
    app.totalMem = QLabel("<font color=brown>Total Memory(MB)</font>")
    app.kernelHeap = QLabel("<font color=orange>Kernel-Heap(MB)</font>")
    app.DPQMemory = QLabel("<font color=orange>DPQ-Memory(MB)</font>")
    app.IDPMemory = QLabel("<font color=orange>IDP-Memory(MB)</font>")
    app.services = QLabel("<font color=orange>Services(MB)</font>")

    app.packetMBuf_section = QLabel("<font color=orange>Packet_Mbuf</font>")
    app.INCOMING_16K_MBUF = QLabel('INCOMING_16K_MBUF(512B)')

    app.hostMBuf_section = QLabel("<font color=orange>Host_Mbuf</font>")
    app.SHARED_1K_MBUF = QLabel('SHARED_1K_MBUF(512B)')
    app.SHARED_2K_MBUF = QLabel('SHARED_2K_MBUF(512B)')
    app.SHARED_16K_MBUF = QLabel('SHARED_16K_MBUF(512B)')
    app.SHARED_64K_MBUF = QLabel('SHARED_64K_MBUF(512B)')
    app.RT_RT_event = QLabel('RT_RT_event(512B)')
    app.PFE_RT_event = QLabel('PFE_RT_event(512B)')

    app.userHeap_section = QLabel("<font color=orange>User-Heap</font>")
    app.uspMaxNatSession = QLabel('usp_max_nat_session(768B)')
    app.uspFullSpuSessionSzInfo = QLabel('usp_full_spu_session_sz_info(72B)')
    app.uspMaxFcbEntries = QLabel('usp_max_fcb_entries(136B)')
    app.uspMaxIpsecTunnels = QLabel('usp_max_ipsec_tunnels(45232B)')
    app.uspMaxPktDropRingLen = QLabel('usp_max_pkt_drop_ring_len(192B)')
    app.uspMaxGates = QLabel('usp_max_gates(193B)')
    app.uspMaxDsLiteSi = QLabel('usp_max_ds_lite_si(40B)')
    app.uspIdpArenaMemory = QLabel('usp_idp_arena_memory(1024B)')
    app.uspMaxMacEntry = QLabel('usp_max_mac_entry(196B)')
    app.uspLsysMaxNum = QLabel('usp_lsys_max_num(51677B)')

    app.manual_input_section = QLabel("<font color=orange>Manual Input</font>")
    app.TLS = QLabel('TLS')
    app.FIB = QLabel('FIB')

    app.input_totalMem = QLineEdit()
    app.input_kernelHeap = QLineEdit()
    app.input_DPQMemory = QLineEdit()
    app.input_IDPMemory = QLineEdit()
    app.input_services = QLineEdit()
    app.input_INCOMING_16K_MBUF = QLineEdit()
    app.input_SHARED_1K_MBUF = QLineEdit()
    app.input_SHARED_2K_MBUF = QLineEdit()
    app.input_SHARED_16K_MBUF = QLineEdit()
    app.input_SHARED_64K_MBUF = QLineEdit()
    app.input_RT_RT_event = QLineEdit()
    app.input_PFE_RT_event = QLineEdit()
    app.input_uspMaxNatSession = QLineEdit()
    app.input_uspFullSpuSessionSzInfo = QLineEdit()
    app.input_uspMaxFcbEntries = QLineEdit()
    app.input_uspMaxIpsecTunnels = QLineEdit()
    app.input_uspMaxPktDropRingLen = QLineEdit()
    app.input_uspMaxGates = QLineEdit()
    app.input_uspMaxDsLiteSi = QLineEdit()
    app.input_uspIdpArenaMemory = QLineEdit()
    app.input_uspMaxMacEntry = QLineEdit()
    app.input_uspLsysMaxNum = QLineEdit()

    app.input_TLS = QLineEdit()
    app.input_FIB = QLineEdit()

    # Creating Result Label
    app.usedMem_inKB = QLabel('Used  Memory (KB)', app)
    app.usedMem_inMB = QLabel('Used  Memory (MB)', app)
    app.usedMem_inGB = QLabel('Used  Memory (GB)', app)
    app.totalMem_inKB = QLabel('Total Memory (KB)', app)
    app.totalMem_inMB = QLabel('Total Memory (MB)', app)
    app.totalMem_inGB = QLabel('Total Memory (GB)', app)

    app.services_inMB = QLabel('Services (MB)', app)
    app.TLS_1_2_inMB = QLabel('TLS_1.2 (MB)', app)
    app.kernelHeap_inMB = QLabel('Kernel Heap (MB)', app)
    app.FIB_inMB = QLabel('FIB (MB)', app)

    # Creating Calculating Button
    app.calc_btn = QPushButton('Calculate', app)
    app.calc_btn.clicked.connect(app.update_result)

    # Creating Load File Button
    app.load_conf_btn = QPushButton('Load .conf File', app)
    app.load_conf_btn.clicked.connect(app.load_conf_file)

    # Creating Layouts
    layout = QGridLayout()
    input_layout = QGridLayout()
    input2_layout = QGridLayout()
    output_layout = QVBoxLayout()

    
    previewer_layout = QVBoxLayout()
    previewerHeadline = QLabel("<font color=white>Conf Viewer</font>")
    previewerHeadline.setAutoFillBackground(True)
    previewerHeadline.setAlignment(Qt.AlignCenter)
    app.find_input = QLineEdit(app)
    app.find_input.setPlaceholderText("Enter text to search...")
    app.find_button = QPushButton("Find", app)
    app.editor = QTextEdit(app)
    app.editor.setReadOnly(True)

    previewer_layout.addWidget(previewerHeadline)
    previewer_layout.addWidget(app.editor)
    previewer_layout.addWidget(app.find_input)
    previewer_layout.addWidget(app.find_button)
    app.find_button.clicked.connect(app.find_text)

    head_widget = QLabel("<font color=white style='font-size:24px';>PFE Memory Calculator - SRX Platform Team</font>")

    
    app.chart_layout0 = QVBoxLayout()
    app.chart_layout0.addWidget(app.memory_chart.chartTotal_view)
    # app.chart_layout0.addStretch()
    app.chart_layout1 = QVBoxLayout()
    app.chart_layout1.addWidget(app.memory_chart.chartTLS_view)
    app.chart_layout2 = QVBoxLayout()
    app.chart_layout2.addWidget(app.memory_chart.chartFIB_view)
    # layout.addLayout(input_layout, 0, 0)
    # layout.addLayout(input2_layout, 0, 1)
    # layout.addLayout(output_layout, 0, 2)
    # layout.addLayout(app.chart_layout0, 1, 0)
    # layout.addLayout(app.chart_layout1, 1, 1)
    # layout.addLayout(app.chart_layout2, 1, 2)

    
    input_layout.addWidget(app.totalMem, 0, 0)
    input_layout.addWidget(app.input_totalMem, 0, 1)
    input_layout.addWidget(app.kernelHeap, 1, 0)
    input_layout.addWidget(app.input_kernelHeap, 1, 1)
    input_layout.addWidget(app.DPQMemory, 2, 0)
    input_layout.addWidget(app.input_DPQMemory, 2, 1)
    input_layout.addWidget(app.IDPMemory, 3, 0)
    input_layout.addWidget(app.input_IDPMemory, 3, 1)
    input_layout.addWidget(app.services, 4, 0)
    input_layout.addWidget(app.input_services, 4, 1)

    input_layout.addWidget(app.packetMBuf_section, 5, 0)
    input_layout.addWidget(app.INCOMING_16K_MBUF, 6, 0)
    input_layout.addWidget(app.input_INCOMING_16K_MBUF, 6, 1)

    input_layout.addWidget(app.hostMBuf_section, 7, 0)
    input_layout.addWidget(app.SHARED_1K_MBUF, 8, 0)
    input_layout.addWidget(app.input_SHARED_1K_MBUF, 8, 1)
    input_layout.addWidget(app.SHARED_2K_MBUF, 9, 0)
    input_layout.addWidget(app.input_SHARED_2K_MBUF, 9, 1)
    input_layout.addWidget(app.SHARED_16K_MBUF, 10, 0)
    input_layout.addWidget(app.input_SHARED_16K_MBUF, 10, 1)
    input_layout.addWidget(app.SHARED_64K_MBUF, 11, 0)
    input_layout.addWidget(app.input_SHARED_64K_MBUF, 11, 1)
    input_layout.addWidget(app.RT_RT_event, 12, 0)
    input_layout.addWidget(app.input_RT_RT_event, 12, 1)
    input_layout.addWidget(app.PFE_RT_event, 13, 0)
    input_layout.addWidget(app.input_PFE_RT_event, 13, 1)

    input2_layout.addWidget(app.userHeap_section, 0, 0)
    input2_layout.addWidget(app.uspMaxNatSession, 1, 0)
    input2_layout.addWidget(app.input_uspMaxNatSession, 1, 1)
    input2_layout.addWidget(app.uspFullSpuSessionSzInfo, 2, 0)
    input2_layout.addWidget(app.input_uspFullSpuSessionSzInfo, 2, 1)
    input2_layout.addWidget(app.uspMaxFcbEntries, 3, 0)
    input2_layout.addWidget(app.input_uspMaxFcbEntries, 3, 1)
    input2_layout.addWidget(app.uspMaxIpsecTunnels, 4, 0)
    input2_layout.addWidget(app.input_uspMaxIpsecTunnels, 4, 1)
    input2_layout.addWidget(app.uspMaxPktDropRingLen, 5, 0)
    input2_layout.addWidget(app.input_uspMaxPktDropRingLen, 5, 1)
    input2_layout.addWidget(app.uspMaxGates, 6, 0)
    input2_layout.addWidget(app.input_uspMaxGates, 6, 1)
    input2_layout.addWidget(app.uspMaxDsLiteSi, 7, 0)
    input2_layout.addWidget(app.input_uspMaxDsLiteSi, 7, 1)
    input2_layout.addWidget(app.uspIdpArenaMemory, 8, 0)
    input2_layout.addWidget(app.input_uspIdpArenaMemory, 8, 1)
    input2_layout.addWidget(app.uspMaxMacEntry, 9, 0)
    input2_layout.addWidget(app.input_uspMaxMacEntry, 9, 1)
    input2_layout.addWidget(app.uspLsysMaxNum, 10, 0)
    input2_layout.addWidget(app.input_uspLsysMaxNum, 10, 1)
    input2_layout.addWidget(app.manual_input_section, 11, 0)
    input2_layout.addWidget(app.TLS, 12, 0)
    input2_layout.addWidget(app.input_TLS, 12, 1)
    input2_layout.addWidget(app.FIB, 13, 0)
    input2_layout.addWidget(app.input_FIB, 13, 1)

    output_layout.addWidget(app.usedMem_inKB)
    output_layout.addWidget(app.usedMem_inMB)
    output_layout.addWidget(app.usedMem_inGB)
    output_layout.addWidget(app.totalMem_inKB)
    output_layout.addWidget(app.totalMem_inMB)
    output_layout.addWidget(app.totalMem_inGB)

    output_layout.addWidget(app.services_inMB)
    output_layout.addWidget(app.TLS_1_2_inMB)
    output_layout.addWidget(app.kernelHeap_inMB)
    output_layout.addWidget(app.FIB_inMB)

    output_layout.addWidget(app.calc_btn)
    output_layout.addWidget(app.load_conf_btn)

    layout.addWidget(head_widget, 0, 0, 1, 4)
    layout.addLayout(input_layout, 1, 0)
    layout.addLayout(input2_layout, 1, 1)
    layout.addLayout(output_layout, 1, 2)
    layout.addLayout(app.chart_layout0, 2, 0)
    layout.addLayout(app.chart_layout1, 2, 1)
    layout.addLayout(app.chart_layout2, 2, 2)
    layout.addLayout(previewer_layout, 1,3,2,1)
    # layout.addWidget(app.editor, 0, 3, 2, 1)


    app.setLayout(layout)

    # Setting Window
    app.setWindowTitle('Memory Calculator')
    app.setGeometry(200, 200, 1200, 800)