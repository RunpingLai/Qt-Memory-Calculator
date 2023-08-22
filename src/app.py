import sys
import re
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,\
                            QLineEdit, QLabel, QPushButton,\
                            QFileDialog, QHBoxLayout, QGridLayout,\
                            QMessageBox, QSizePolicy, QTextEdit)
from PyQt5.QtChart import QChart, QPieSeries, QChartView
from PyQt5.QtGui import QPainter, QTextCursor
from PyQt5.QtCore import Qt, QIODevice, QTextStream, QFile
import qdarkstyle
from uiIniter import init
from chartController import myChart

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.memory_chart = myChart()
        init(self)

    
    def getInt(self, text):
        if text and (text[:2] == "0x" or text[:2] == "0X"):
            return int(text, 16)
        elif text and (text[-1] == "k" or text[-1] == "K"):
            return int(text[:-1]) * 1024
        elif text:
            return int(text)
        else:
            return 0


    def update_result(self):
        totalMem = self.getInt(self.input_totalMem.text())
        kernelHeap = self.getInt(self.input_kernelHeap.text())
        DPQMemory = self.getInt(self.input_DPQMemory.text())
        IDPMemory = self.getInt(self.input_IDPMemory.text())
        services = self.getInt(self.input_services.text())
        INCOMING_16K_MBUF = self.getInt(self.input_INCOMING_16K_MBUF.text())
        SHARED_1K_MBUF = self.getInt(self.input_SHARED_1K_MBUF.text())
        SHARED_2K_MBUF = self.getInt(self.input_SHARED_2K_MBUF.text())
        SHARED_16K_MBUF = self.getInt(self.input_SHARED_16K_MBUF.text())
        SHARED_64K_MBUF = self.getInt(self.input_SHARED_64K_MBUF.text())
        RT_RT_event = self.getInt(self.input_RT_RT_event.text())
        PFE_RT_event = self.getInt(self.input_PFE_RT_event.text())
        uspMaxNatSession = self.getInt(self.input_uspMaxNatSession.text())
        uspFullSpuSessionSzInfo = self.getInt(self.input_uspFullSpuSessionSzInfo.text())
        uspMaxFcbEntries = self.getInt(self.input_uspMaxFcbEntries.text())
        uspMaxIpsecTunnels = self.getInt(self.input_uspMaxIpsecTunnels.text())
        uspMaxPktDropRingLen = self.getInt(self.input_uspMaxPktDropRingLen.text())
        uspMaxGates = self.getInt(self.input_uspMaxGates.text())
        uspMaxDsLiteSi = self.getInt(self.input_uspMaxDsLiteSi.text())
        uspIdpArenaMemory = self.getInt(self.input_uspIdpArenaMemory.text())
        uspMaxMacEntry = self.getInt(self.input_uspMaxMacEntry.text())
        uspLsysMaxNum = self.getInt(self.input_uspLsysMaxNum.text())


        kernelHeap = kernelHeap * 1024 * 1024
        DPQMemory = DPQMemory * 1024 * 1024
        IDPMemory = IDPMemory * 1024 * 1024
        services = services * 1024 * 1024

        PacketMBuf = INCOMING_16K_MBUF * 512
        RestMBUF = SHARED_1K_MBUF + SHARED_2K_MBUF + SHARED_16K_MBUF \
                    + SHARED_64K_MBUF + RT_RT_event + PFE_RT_event
        HostMBuf = (RestMBUF) * 512

        UserHeap = uspMaxNatSession * 768\
                + uspFullSpuSessionSzInfo * 72\
                + uspMaxFcbEntries * 136\
                + uspMaxIpsecTunnels * 45232\
                + uspMaxPktDropRingLen * 192\
                + uspMaxGates *193\
                + uspMaxDsLiteSi *40\
                + uspIdpArenaMemory *1024\
                + uspMaxMacEntry *196\
                + uspLsysMaxNum *51677

        usedMem = kernelHeap + \
                    DPQMemory + \
                    IDPMemory + \
                    services + \
                    PacketMBuf + \
                    HostMBuf + \
                    UserHeap
        usedMem_inKB = round(usedMem / 2**10, 2)
        usedMem_inMB = round(usedMem / 2**20, 2)
        usedMem_inGB = round(usedMem / 2**30, 2)

        # totalMem = totalMem
        totalMem_inKB = round(totalMem * 2**10, 2)
        totalMem_inMB = totalMem
        totalMem_inGB = round(totalMem / 2**10, 2)

        # Additional Check
        TLS_var = self.getInt(self.input_TLS.text())
        FIB_var = self.getInt(self.input_FIB.text())
        services_inMB = round(services / (2**20), 2)
        if TLS_var == 0:
            TLS_inMB = 0
        else:
            TLS_inMB = round((1.4) * 1024 + self.getInt(self.input_TLS.text()) * 82 / (2 ** 10), 2)
        kernelHeap_inMB = round(kernelHeap / (2**20), 2)
        if FIB_var == 0:
            FIB_inMB = 0
        else:
            FIB_inMB = round(600 + self.getInt(self.input_FIB.text()) * 460 / (2 ** 20), 2)

        self.usedMem_inKB.setText('usedMem_inKB Result: ' + str(usedMem_inKB))
        self.usedMem_inMB.setText('usedMem_inMB Result: ' + str(usedMem_inMB))
        self.usedMem_inGB.setText('usedMem_inGB Result: ' + str(usedMem_inGB))
        self.totalMem_inKB.setText('totalMem_inKB Result: ' + str(totalMem_inKB))
        self.totalMem_inMB.setText('totalMem_inMB Result: ' + str(totalMem_inMB))
        self.totalMem_inGB.setText('totalMem_inGB Result: ' + str(totalMem_inGB))

        self.services_inMB.setText('Services (MB): ' + str(services_inMB))
        self.TLS_1_2_inMB.setText('TLS_1.2 (MB): ' + str(TLS_inMB))
        self.kernelHeap_inMB.setText('Kernel Heap (MB): ' + str(kernelHeap_inMB))
        self.FIB_inMB.setText('FIB (MB): ' + str(FIB_inMB))

        # Draw Charts
        self.updateChart(usedMem_inMB, totalMem_inMB,\
                        TLS_inMB, services_inMB,\
                        FIB_inMB, kernelHeap_inMB)


    def load_conf_file(self):
        # 使用 QFileDialog 选择文件
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Load .conf File", "",
                                                   "Config Files (*.conf);;All Files (*)", options=options)
        if file_name:
            # For File Viewer
            file = QFile(file_name)
            if file.open(QIODevice.ReadOnly | QIODevice.Text):
                stream = QTextStream(file)
                # if not self.editor:
                    # self.editor = QTextEdit(self)
                    
                self.editor.setPlainText(stream.readAll())
                file.close()

            # For File Parser
            with open(file_name, 'r') as f:
                content = f.read()
                self.parse_conf_file(content)

    def parse_block(self, block):
        pattern = r'(\w+)\s*=\s*([^;#]+);'
        matches = re.findall(pattern, block)
        
        sub_result = {}
        for key, value in matches:
            key = key.strip()
            value = value.strip()


            # 尝试将value转化为整数
            if isinstance(value, str) and value.startswith(("0X", "0x")):
                try:
                    value = int(value, 16)
                except ValueError:
                    pass
            else:
                try:
                    value = int(value)
                except ValueError:
                    pass

            
            sub_result[key] = value

        return sub_result

    
    def parse_conf_file(self, content):
        # 主块的正则表达式
        main_pattern = r'(\w+):\s*\(\s*\{(.*?)\}\s*\);'
        
        # 子块的正则表达式
        sub_pattern = r'\{\s*(.*?)\s*\}[,;]?'

        matches = re.findall(main_pattern, content, re.DOTALL)
        
        result = {}
        for main_key, main_content in matches:
            sub_matches = re.findall(sub_pattern, main_content, re.DOTALL)
            
            if main_key == "Mem_List":
                pattern = r'^\s*(\w+)\s*=\s*(\d+);'
                matches = re.findall(pattern, main_content, re.MULTILINE)
                for (key, value) in matches:
                    if key == "Pfe_App_Mem":
                        result["Mem_List"] = {"Pfe_App_Mem": value}

            if main_key == "Segment_Mem_Limit":
                sub_result = {}
                sub_matches = re.findall(r'SegmentName\s*=\s*"([^"]+)"\s*;\s*Segment_Value\s*=\s*([^;]+)', main_content, re.DOTALL)
                for (key, val) in sub_matches:
                    sub_result[key] =  val
                    # if val and (val[:2] == "0x" or val[:2] == "0X"):
                    #     sub_result[key] =  int(val, 16)
                    # else:
                    #     sub_result[key] = int(val)
                result["Segment_Mem_Limit"] = sub_result
            
            if main_key == "Packet_Limit":
                sub_result = {}
                sub_matches = re.findall(r'PktName\s*=\s*"([^"]+)"\s*;\s*Pkt_Value\s*=\s*([^;]+)', main_content, re.DOTALL)
                for (key, val) in sub_matches:
                    if key not in sub_result:
                        sub_result[key] =  val
                result["Packet_Limit"] = sub_result

            if main_key == "Feature_Mem_Limit":
                sub_result = {}
                sub_matches = re.findall(r'FeatureName\s*=\s*"([^"]+)"\s*;.*?cfg_with_no_license\s*=\s*([^;]+)', main_content, re.DOTALL)
                for (key, val) in sub_matches:
                    sub_result[key] =  val

                result["Feature_Mem_Limit"] = sub_result

        self.input_totalMem.setText(str(result["Mem_List"].get("Pfe_App_Mem", 0)))
        self.input_kernelHeap.setText(str(result["Segment_Mem_Limit"].get("Kernel-Heap", 0)))
        self.input_DPQMemory.setText(str(result["Segment_Mem_Limit"].get("DPQ-Memory", 0)))
        self.input_IDPMemory.setText(str(result["Segment_Mem_Limit"].get("IDP-Memory", 0)))
        self.input_services.setText(str(result["Segment_Mem_Limit"].get("Services", 0)))
        self.input_INCOMING_16K_MBUF.setText(str(result["Packet_Limit"].get("INCOMING-16K-MBUF", 0)))
        self.input_SHARED_1K_MBUF.setText(str(result["Packet_Limit"].get("SHARED-1K-MBUF", 0)))
        self.input_SHARED_2K_MBUF.setText(str(result["Packet_Limit"].get("SHARED-2K-MBUF", 0)))
        self.input_SHARED_16K_MBUF.setText(str(result["Packet_Limit"].get("SHARED-16K-MBUF", 0)))
        self.input_SHARED_64K_MBUF.setText(str(result["Packet_Limit"].get("SHARED-64K-MBUF", 0)))
        self.input_RT_RT_event.setText(str(result["Packet_Limit"].get("RT-RT-event", 0)))
        self.input_PFE_RT_event.setText(str(result["Packet_Limit"].get("PFE-RT-event", 0)))
        self.input_uspMaxNatSession.setText(str(result["Feature_Mem_Limit"].get("usp_max_nat_session", 0)))
        self.input_uspFullSpuSessionSzInfo.setText(str(result["Feature_Mem_Limit"].get("usp_full_spu_session_sz_info", 0)))
        self.input_uspMaxFcbEntries.setText(str(result["Feature_Mem_Limit"].get("usp_max_fcb_entries", 0)))
        self.input_uspMaxIpsecTunnels.setText(str(result["Feature_Mem_Limit"].get("usp_max_ipsec_tunnels", 0)))
        self.input_uspMaxPktDropRingLen.setText(str(result["Feature_Mem_Limit"].get("usp_max_pkt_drop_ring_len", 0)))
        self.input_uspMaxGates.setText(str(result["Feature_Mem_Limit"].get("usp_max_gates", 0)))
        self.input_uspMaxDsLiteSi.setText(str(result["Feature_Mem_Limit"].get("usp_max_ds_lite_si", 0)))
        self.input_uspIdpArenaMemory.setText(str(result["Feature_Mem_Limit"].get("usp_idp_arena_memory", 0)))
        self.input_uspMaxMacEntry.setText(str(result["Feature_Mem_Limit"].get("usp_max_mac_entry", 0)))
        self.input_uspLsysMaxNum.setText(str(result["Feature_Mem_Limit"].get("usp_lsys_max_num", 0)))

        # return result


    def updateChart(self, usedMem, totalMem, usedTLS, totalTLS, usedFIB, totalFIB):
        self.memory_chart.usedMem = usedMem
        self.memory_chart.totalMem = totalMem
        self.memory_chart.usedTLS = usedTLS
        self.memory_chart.totalTLS = totalTLS
        self.memory_chart.usedFIB = usedFIB
        self.memory_chart.totalFIB = totalFIB

    def find_text(self):
        search_text = self.find_input.text()
        # Use the find method of QTextEdit to search for the text
        if not self.editor.find(search_text):
            # If the text is not found, move the cursor to the beginning and try again
            self.editor.moveCursor(QTextCursor.Start)

            self.editor.find(search_text)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    ex = App()
    ex.show()
    sys.exit(app.exec_())
